from fastapi import Depends, FastAPI, Request
from auth.auth_bearer import JWTBearer
from auth import jwt_token_handler


app = FastAPI()


@app.get("/",status_code=200, dependencies=[Depends(JWTBearer())])
async def root():
    return {"message": "Hello World"}


@app.get("/hello",status_code=200, dependencies=[Depends(JWTBearer())])
async def root():
    return {"message": "Hello World"}


@app.get("/items/{id}", status_code=200, dependencies=[Depends(JWTBearer())])
async def read_item(request: Request, id: str):
    return {"message": "Hello World"}



@app.post('/token')
def create_token(request:Request):
    payload_data= {"teste":"teste", "user":"fulano"}
    token = jwt_token_handler.generate_token(payload_data)
    return({'token': token})



