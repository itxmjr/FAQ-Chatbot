from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from .chatbot import FAQChatbot, get_default_bot

app = FastAPI(
    title="FAQ Chatbot API",
    description="Backend API for the FAQ Chatbot, serving Next.js and other clients.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    answer: str
    matched_question: Optional[str] = None
    confidence_score: float

@app.get("/")
async def root():
    return {"message": "Welcome to the FAQ Chatbot API", "status": "online"}

@app.post("/ask", response_model=QueryResponse)
async def ask_question(request: QueryRequest):
    bot = get_default_bot()
    answer, matched_q, score = bot.get_answer(request.question)
    
    return QueryResponse(
        answer=answer,
        matched_question=matched_q if matched_q else None,
        confidence_score=score
    )

@app.get("/categories", response_model=List[str])
async def get_categories():
    bot = get_default_bot()
    return bot.get_categories()

@app.get("/suggestions", response_model=List[str])
async def get_suggestions(n: int = 3):
    bot = get_default_bot()
    return bot.get_random_questions(n)

@app.get("/all")
async def get_all_faqs():
    bot = get_default_bot()
    return bot.get_all_faqs()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
