CREATE TABLE banks (
    bank_id SERIAL PRIMARY KEY,
    bank_name TEXT UNIQUE NOT NULL,
    app_name TEXT
);

CREATE TABLE reviews (
    review_id SERIAL PRIMARY KEY,
    bank_id INT REFERENCES banks(bank_id),
    review_text TEXT,
    rating FLOAT CHECK (rating >= 0 AND rating <= 5),
    review_date DATE,
    sentiment_label TEXT,
    sentiment_score FLOAT,
    source TEXT
);
