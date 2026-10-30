from sqlalchemy import (
    Column, BigInteger, Integer, String, Double, DateTime, ForeignKey
)
from sqlalchemy.sql import func
from database import Base


# class User(Base):
#     __tablename__ = "users"

#     id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)
#     name = Column(String(100), nullable=False)
#     email = Column(String(150), unique=True, nullable=False, index=True)
#     password = Column(String(255), nullable=False)
#     created_at = Column(DateTime, server_default=func.now(), nullable=False)

class User(Base):
    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True,
        index=True
    )

    name = Column(
        String(100),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False,
        index=True
    )

    password = Column(
        String(255),
        nullable=False
    )

    role = Column(
        String(20),
        nullable=False,
        default="STUDENT",
        server_default="STUDENT"
    )

    created_at = Column(
        DateTime,
        server_default=func.now(),
        nullable=False
    )

class PredictionHistory(Base):
    __tablename__ = "prediction_history"

    id = Column(BigInteger, primary_key=True, autoincrement=True, index=True)

    user_id = Column(
        BigInteger,
        ForeignKey("users.id", ondelete="CASCADE"),
        nullable=False,
        index=True
    )

    # These columns match the MySQL table definition:
    # all are nullable except id, user_id and created_at.
    age = Column(Integer, nullable=True)
    gender = Column(String(20), nullable=True)
    country = Column(String(100), nullable=True)
    academic_level = Column(String(50), nullable=True)
    most_used_platform = Column(String(100), nullable=True)
    purpose_of_use = Column(String(100), nullable=True)

    avg_daily_usage_hours = Column(Double, nullable=True)
    daily_unlocks = Column(Integer, nullable=True)
    study_hours = Column(Double, nullable=True)
    physical_activity_hours = Column(Double, nullable=True)
    sleep_hours_per_night = Column(Double, nullable=True)
    stress_level = Column(String(50), nullable=True)

    mental_health_score = Column(Double, nullable=True)

    created_at = Column(
        DateTime,
        server_default=func.current_timestamp(),
        nullable=False
    )
