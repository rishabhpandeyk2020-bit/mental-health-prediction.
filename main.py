from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from database import engine, Base
from models import User, PredictionHistory

from routers.auth_router import router as auth_router
from routers.prediction_router import router as prediction_router
from routers.history_router import router as history_router
from routers.user_router import router as user_router
from routers.dashboard_router import router as dashboard_router

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Mental Health Prediction API",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://127.0.0.1:5500",
        "http://localhost:5500"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

app.include_router(auth_router)
app.include_router(prediction_router)
app.include_router(history_router)

app.include_router(user_router)
app.include_router(dashboard_router)


@app.get("/")
def home():
    return {
        "message": "Mental Health Prediction API is running"
    }
