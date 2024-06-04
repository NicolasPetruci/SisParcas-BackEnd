from typing import Callable
from flask import request as FlaskRequest
from src.presentation.http_types import HttpRequest, HttpResponse
from .auth import decode_token
from src.errors import handle_errors, HttpError

def request_adapter_no_token(request: FlaskRequest, controller: Callable) -> HttpResponse:

    body = None
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
    return http_response

def request_adapter(request: FlaskRequest, controller: Callable) -> HttpResponse:

    token = None
    
    try:
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
    except Exception as exception:
        return handle_errors(exception)
    
    try:
        body = None
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
        return http_response
    except Exception as exception:
        return handle_errors(exception)

     