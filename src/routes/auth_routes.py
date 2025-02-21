from fastapi import APIRouter

auth_routes = APIRouter()

@auth_routes.get('/me')
def get_all_users():
    return {"Hello": "World"} 


@auth_routes.post('/sign-up')
def get_all_users():
    return {"Hello": "World"} 


@auth_routes.post('/login')
def get_all_users():
    return {"Hello": "World"} 


@auth_routes.post('/logout')
def get_all_users():
    return {"Hello": "World"} 