from fastapi import FastAPI
from pydantic import BaseModel
from util import load_model_data, score_answer  # Corrected import

app = FastAPI()

# Load keyword_weights and default_weight on startup
model_data = load_model_data()
keyword_weights = model_data['keyword_weights']
default_weight = model_data['default_weight']


# Define request and response models
class AnswerRequest(BaseModel):
    answer: str


class AnswerScoreResponse(BaseModel):
    score: float


@app.post("/score_answer", response_model=AnswerScoreResponse)
async def score_answer_endpoint(request: AnswerRequest):
    score = score_answer(request.answer, keyword_weights, default_weight)
    return AnswerScoreResponse(score=score)
