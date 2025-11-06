from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/feed")
def get_feed():
    return {
        "daily": [
            {"title": "LangGraph 框架", "desc": "多智能体工作流", "link": "https://github.com/langchain-ai/langgraph"},
            {"title": "DeepSeek-R1", "desc": "大模型压缩技术", "link": "https://huggingface.co/deepseek-ai"}
        ]
    }

