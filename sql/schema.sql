
-- ============================================
-- PostgreSQL schema for FINTECH-MOBILE-BANKING-REVIEWS
-- ============================================

-- --------------------------------------------
-- Banks table: unique list of banking apps
-- --------------------------------------------
CREATE TABLE IF NOT EXISTS banks (
    bank_id        SERIAL PRIMARY KEY,
    bank_name      TEXT UNIQUE NOT NULL,
    app_name       TEXT
);

-- --------------------------------------------
-- Reviews table: cleaned + enriched review data
-- --------------------------------------------
CREATE TABLE IF NOT EXISTS reviews (
    review_id         SERIAL PRIMARY KEY,
    bank_id           INT NOT NULL REFERENCES banks(bank_id) ON DELETE CASCADE,
    review_text       TEXT,
    rating            NUMERIC(2,1),            -- supports stars like 1–5 or 4.5
    review_date       DATE,
    sentiment_label   TEXT,                    -- e.g., positive/neutral/negative
    sentiment_score   NUMERIC(6,5),            -- e.g., 0.12345
    source            TEXT                     -- e.g., PlayStore/AppStore
);

-- --------------------------------------------
-- Constraints
-- --------------------------------------------
ALTER TABLE reviews
    ADD CONSTRAINT rating_range_chk
    CHECK (rating IS NULL OR (rating >= 0 AND rating <= 5));

-- --------------------------------------------
-- Indexes for performance
-- --------------------------------------------
-- Fast join/filter by bank
CREATE INDEX IF NOT EXISTS idx_banks_bank_name
    ON banks (bank_name);

CREATE INDEX IF NOT EXISTS idx_reviews_bank_id
    ON reviews (bank_id);

-- Aggregations and filtering by rating/date
CREATE INDEX IF NOT EXISTS idx_reviews_rating
    ON reviews (rating);

CREATE INDEX IF NOT EXISTS idx_reviews_review_date
    ON reviews (review_date);
