from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class LikedTweetsRequest(BaseModel):
    search_query: str

router.post("/get_liked_tweets")
def get_liked_tweets(request: LikedTweetsRequest):
    return request.search_query