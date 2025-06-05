from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.credit import CreditScoreResponse
from app.core.dependencies import get_db, get_current_user

router = APIRouter()

@router.get("/credit_score", response_model=CreditScoreResponse)
def get_credit_score(user = Depends(get_current_user), db: Session = Depends(get_db)):
    score = 650 + (user.successful_trades * 2) - (user.failed_trades * 3)
    score = max(300, min(850, score))
    return {"user_id": user.id, "credit_score": score}
