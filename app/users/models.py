from fastapi import HTTPException
from pydantic import BaseModel

class User(BaseModel):
    name: str
    job: str

    def is_valid(self) -> dict:
        if (self.name.strip() == ""):      
            raise HTTPException(status_code=400, detail="The username can not be empty")
        
        if (self.job.strip() == ""):      
            raise HTTPException(status_code=400, detail="The job can not be empty")
        
        return {"name": self.name, "job": self.job}
