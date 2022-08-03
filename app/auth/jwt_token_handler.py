from datetime import datetime, timedelta
from functools import wraps
from fastapi import HTTPException, Header
import jwt
import pytz
import setup.config as config

def generate_token(payload_data:dict):
    payload_data["exp"] = datetime.now(tz=pytz.timezone('America/Sao_Paulo')) + timedelta(minutes=config.TOKEN_DURATION_MINUTES)
    return {"access_token": jwt.encode(payload_data, config.API_SECRET_KEY, config.ALGORITHM)}

def get_token_payload(token):
    token_payload = jwt.decode(token, config.API_SECRET_KEY, config.ALGORITHM)
    return token_payload