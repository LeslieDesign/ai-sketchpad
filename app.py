from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
import openai, os
from dotenv import load_dotenv

# ── env & client ───────────────────────────────────────────
load_dotenv()  # pulls OPENAI_API_KEY from .env
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# ── FastAPI init ───────────────────────────────────────────
app = FastAPI(title="NeuroGuideAI API", version="0.1.0")

class ChatRequest(BaseModel):
    prompt: str
    max_tokens: int | None = 150

class ChatResponse(BaseModel):
    answer: str

# ── route ──────────────────────────────────────────────────
@app.post("/ask", response_model=ChatResponse)
def ask_ai(req: ChatRequest):
    try:
        completion = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": req.prompt}],
            temperature=0.3,
            max_tokens=req.max_tokens,
        )
        return {"answer": completion.choices[0].message.content.strip()}

    except openai.OpenAIError as e:
        # surfaces API errors nicely to the front-end
        raise HTTPException(status_code=500, detail=str(e))
