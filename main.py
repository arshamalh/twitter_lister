from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

from routes import routes_group_1, routes_group_2

api_app = FastAPI(title="api app")

api_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

api_app.include_router(routes_group_1.router)
api_app.include_router(routes_group_2.router)

app = FastAPI(title="main app")

app.mount("/api", api_app)
app.mount("/", StaticFiles(directory="ui", html=True), name="ui")