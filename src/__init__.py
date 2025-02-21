from fastapi import FastAPI
from src.routes.auth_routes import auth_routes

version = "v1"

description = """
A REST API for a book review web service.

This REST API is able to;
- Create Read Update And delete books
- Add reviews to books
- Add tags to Books e.t.c.
    """

version_prefix =f"/api/{version}"

app = FastAPI(
    title="Demo App",
    description=description,
    version=version,
    )

app.include_router(auth_routes, prefix=f'{version_prefix}/auth', tags="auth")
