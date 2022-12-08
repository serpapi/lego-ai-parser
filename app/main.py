from fastapi import FastAPI
from app.schemas import Targets
from app.classify.classify import Classify

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "To learn more about the Daath AI Parser, please visit https://github.com/kagermanov27/daath-ai-parser/"}

@app.post("/classify")
def classify(targets: Targets):
    classifier = Classify()
    return classifier.classify(targets = targets)