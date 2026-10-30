from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USERNAME = "root"
DB_PASSWORD = "admin"
DB_HOST = "localhost"
DB_PORT = "3306"
DB_NAME = "mental_health_db"

DATABASE_URL = (
    f"mysql+pymysql://"
    f"{DB_USERNAME}:{DB_PASSWORD}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(
    DATABASE_URL,
    echo=True,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
