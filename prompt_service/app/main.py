from fastapi import FastAPI, APIRouter, HTTPException
from pydantic import BaseModel
from .prompt_engineer import process_prompt


app = FastAPI()

router = APIRouter()

class PromptRequest(BaseModel):
    prompt: str

@router.post("/process_prompt/")
async def process_and_forward_prompt(request: PromptRequest):
    try:
        # Processa o prompt e encaminha para o serviço generative_service
        response = process_prompt(request.prompt)
        return {"response": response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)