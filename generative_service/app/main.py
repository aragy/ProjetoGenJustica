from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from .model_handler import generate_response

app = FastAPI()


router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/generate/")
async def generate_text(request: PromptRequest):
    try:
        response = generate_response(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)
