from fastapi import Depends, FastAPI, Request
from services.user import UserService
from auth.auth_bearer import JWTBearer
from auth import jwt_token_handler


app = FastAPI()


@app.get("/",status_code=200)
async def root(token_payload = Depends(JWTBearer())):
    print(token_payload)
    return {"message": "Hello World"}

@app.get("/hello",status_code=200)
async def root(token_payload = Depends(JWTBearer())):
    return {"message": "Hello World"}

@app.get("/users", status_code=200)
async def get_all_users(token_payload = Depends(JWTBearer()), page:int = 1, pageSize:int = 10):
    return UserService.getAll(page=page, pageSize=pageSize)

@app.get("/users/{id}", status_code=200, dependencies=[Depends(JWTBearer())])
async def read_item(request: Request, id: int):
    return UserService.getById(id)


@app.post('/token')
def create_token(request:Request):
    payload_data= {"teste":"teste", "user":"fulano"}
    token = jwt_token_handler.generate_token(payload_data)
    return({'token': token})



