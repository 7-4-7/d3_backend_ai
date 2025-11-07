from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from typing import Dict, List
class DescriptionModel(BaseModel):
    user_id : str
    skill_set : List[Dict]
    
app = FastAPI()

@app.get("/")
def health_check():
    return {
        "Message" : "ALIVEEEEE"
    }

@app.post("/embed_description")
async def description_emebedding(data : DescriptionModel):
    payload = await request.json()
    if description == '':
        raise HTTPException(status_code=401, detail="Description can't be none")
    
    
    
    