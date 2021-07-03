from fastapi import APIRouter, Request, Depends, Body, Response

from app.proxy import proxy
from app.users import models

routes = APIRouter(prefix="/api")

@routes.post("/users")
async def post(request: Request, data: models.User, response: Response):
    # Data validation
    validated_data = data.is_valid()
    request = proxy.RequestProxy(request, response)

    # Proxy request
    response_user = await request.post(validated_data)    
    return response_user