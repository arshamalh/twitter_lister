from fastapi import APIRouter
from pydantic import BaseModel
from database import get_liked_tweets_db

router = APIRouter()


class LikedTweetsRequest(BaseModel):
    search_query: str


@router.post("/get_liked_tweets")
def get_liked_tweets(request: LikedTweetsRequest):
    return {"code": 200, "data": get_liked_tweets_db()}
