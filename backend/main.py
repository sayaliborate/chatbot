from fastapi import FastAPI
from pydantic import BaseModel
from chatbot import get_response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
import webbrowser

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
def chat(request: ChatRequest):
    return {"reply": get_response(request.message)}

# Serve frontend UI
@app.get("/")
def serve_ui():
    return FileResponse("ui.html")

# Auto-open browser when backend starts
@app.on_event("startup")
def open_browser():
    webbrowser.open("http://127.0.0.1:8000")
