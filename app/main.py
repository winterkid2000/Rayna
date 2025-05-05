from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.chat_engine import get_rayna_reply

app = FastAPI()

# CORS 설정 (웹 프론트와 연결 가능하게)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_input = data.get("message", "")
    reply = get_rayna_reply(user_input)
    return {"rayna_reply": reply}

