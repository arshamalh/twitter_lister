from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routes import get_liked_tweets

api_app = FastAPI(title="api app")

api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app.include_router(get_liked_tweets.router)

app = FastAPI(title="main app")

app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="ui/public", html=True), name="ui")
