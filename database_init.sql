CREATE DATABASE IF NOT EXISTS mental_health_db;
USE mental_health_db;

-- Users table is created by the application/your existing database setup.
-- Prediction history table:
CREATE TABLE IF NOT EXISTS prediction_history (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NOT NULL,

    age INT,
    gender VARCHAR(20),
    country VARCHAR(100),
    academic_level VARCHAR(50),
    most_used_platform VARCHAR(100),
    purpose_of_use VARCHAR(100),

    avg_daily_usage_hours DOUBLE,
    daily_unlocks INT,
    study_hours DOUBLE,
    physical_activity_hours DOUBLE,
    sleep_hours_per_night DOUBLE,
    stress_level VARCHAR(50),

    mental_health_score DOUBLE,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    CONSTRAINT fk_prediction_user
        FOREIGN KEY (user_id)
        REFERENCES users(id)
        ON DELETE CASCADE
);
