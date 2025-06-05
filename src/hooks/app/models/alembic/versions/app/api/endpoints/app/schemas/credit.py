from pydantic import BaseModel

class CreditScoreResponse(BaseModel):
    user_id: int
    credit_score: int
