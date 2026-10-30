from pydantic import BaseModel, Field
from typing import Literal


class RegisterRequest(BaseModel):
    name: str = Field(..., min_length=2, max_length=100)
    email: str = Field(..., min_length=5, max_length=150)
    password: str = Field(..., min_length=6, max_length=100)


class LoginRequest(BaseModel):
    email: str
    password: str


class StudentData(BaseModel):
    age: int = Field(..., ge=10, le=100)
    gender: Literal["Male", "Female"]
    country: str
    academic_level: Literal["Undergraduate", "Graduate", "High School"]
    most_used_platform: Literal[
        "Facebook", "LinkedIn", "Instagram", "Snapchat", "Twitter",
        "YouTube", "TikTok", "LINE", "KakaoTalk", "VKontakte",
        "WhatsApp", "WeChat"
    ]
    purpose_of_use: Literal[
        "Networking", "Education", "Entertainment", "News"
    ]
    avg_daily_usage_hours: float = Field(..., ge=0, le=24)
    daily_unlocks: int = Field(..., ge=0)
    study_hours: float = Field(..., ge=0, le=24)
    physical_activity_hours: float = Field(..., ge=0, le=24)
    sleep_hours_per_night: float = Field(..., ge=0, le=24)
    stress_level: Literal["Medium", "Low", "Very High", "High"]


class PredictionResponse(BaseModel):
    predected_mental_health_score: float
