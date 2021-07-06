from fastapi import HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str
    job: str
