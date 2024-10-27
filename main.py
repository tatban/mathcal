from fastapi import FastAPI
from eval_logic import eval_text_question

app = FastAPI()


@app.get("/")
async def root():
    return "mathcal server is running"


@app.get("/mathcal/{question}")
async def calculate(question: str):
    res = eval_text_question(question)
    return {
        "question": question,
        "result": res
    }
