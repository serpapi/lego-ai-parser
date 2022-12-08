from fastapi import FastAPI
from app.schemas import Targets
from app.classify.classify import Classify

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/classify")
def classify(targets: Targets):
    classifier = Classify()
    return classifier.classify(targets = targets)