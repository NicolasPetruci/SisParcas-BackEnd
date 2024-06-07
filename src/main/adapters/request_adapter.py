from typing import Callable
from flask import request as FlaskRequest
from src.presentation.http_types import HttpRequest, HttpResponse
from .auth import decode_token, Payload
from src.errors import handle_errors, HttpError

def get_token(request):
    token = None
    raw_token = ""
    if request.headers.get("token"):
        raw_token = request.headers.get("token")
    elif request.headers.get("Token"):
        raw_token = request.headers.get("Token")
    elif request.headers.get("Authorization"):
        raw_token = request.headers.get("Authorization").split()[1]
    else: 
        raise HttpError(HttpError.error_401())
    token = decode_token(raw_token)
    if token is None:
        raise HttpError(HttpError.error_401())
    return Payload(token["username"], token["cargo"], token["id"])
   
def request_adapter_no_token(request: FlaskRequest, controller: Callable) -> HttpResponse:

    body = None
    try:
        if request.data: 
            body = request.json

        http_request = HttpRequest(
            body=body,
            headers=request.headers,
            query_params=request.args,
            path_params=request.view_args,
            url=request.full_path
        )

        http_response = controller(http_request)
        http_response.headers.add("Access-Control-Allow-Origin", "*")
        http_response.headers.add("Access-Control-Allow-Headers", "*")
        http_response.headers.add("Access-Control-Allow-Methods", "*")
        return http_response
    except Exception as exception:
        return handle_errors(exception)

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:

    token = get_token(request)
    
    return request_adapter_no_token(request, controller)

def request_adapter_dono(request: FlaskRequest, controller: Callable) -> HttpResponse:

    token = get_token(request)

    if(token.cargo != "DONO"):
        raise HttpError(HttpError.error_401())
    
    return request_adapter_no_token(request, controller)
    
def request_adapter_adm(request: FlaskRequest, controller: Callable) -> HttpResponse:

    token = get_token(request)

    if(token.cargo == "DEFAULT"):
        raise HttpError(HttpError.error_401())
    
    return request_adapter_no_token(request, controller)