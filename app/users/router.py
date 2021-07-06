from fastapi import APIRouter, Request, Depends, Body, Response
from pydantic import BaseModel

from app.proxy import proxy
from app.users import models

routes = APIRouter(prefix="/api")

@routes.post("{path:path}")
async def post(request: Request, response: Response):
    proxy_request = proxy.RequestProxy(request, response)

    # Proxy request
    data = await request.json()
    response_user = await proxy_request.post(data)    
    return response_user