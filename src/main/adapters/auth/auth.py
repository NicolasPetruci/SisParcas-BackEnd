import jwt
from decouple import config
from passlib.context import CryptContext
from src.main.adapters.auth import Payload

pwd_context = CryptContext(
    schemes=["pbkdf2_sha256"],
    default="pbkdf2_sha256",
    pbkdf2_sha256__default_rounds=30000,
)

def encrypt_password(password):
    return pwd_context.encrypt(password)

def check_encrypted_password(password, hashed):
    return pwd_context.verify(password, hashed)


def encode_token(payload:Payload) -> str:
    salt = config("SECRET_WEB", default="SisParcas", cast=str)
    return jwt.encode(payload.to_json(), salt, algorithm="HS256")


def decode_token(token):
    salt = config("SECRET_WEB", default="SisParcas", cast=str)
    try:
        decode = jwt.decode(token, salt, algorithms="HS256")
        return decode
    except Exception as e:
        raise e