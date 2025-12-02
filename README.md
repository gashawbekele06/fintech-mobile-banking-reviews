# Bank Reviews Analysis Project

## Overview

This project analyzes customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Awash Bank**
- **Amhara Bank**

The goal is to help banks improve their mobile apps by identifying pain points, satisfaction drivers, and feature requests.

---

## Project Structure

# Bank Reviews Project: PostgreSQL Setup & Data Insertion

This guide explains how to set up PostgreSQL, apply the schema, and load cleaned review data into the database.

## 1. Install PostgreSQL

Follow the official instructions for your OS: [PostgreSQL Downloads](https://www.postgresql.org/download/)

## 2. Create the Database

```bash
# Log in to PostgreSQL and create the database
createdb -h localhost -U postgres bank_reviews
```

## 3. Apply Schema

Run the provided `schema.sql` file to create tables and indexes:

```bash
psql -h localhost -U postgres -d bank_reviews -f schema.sql
```

## 4. Insert Cleaned Review Data

Use the Python script `store_reviews_postgres.py` to insert reviews and banks:

```bash
# Activate your virtual environment if needed
source venv/bin/activate

# Run the script
python store_reviews_postgres.py
```

This script:

- Connects to the `bank_reviews` database
- Creates `banks` and `reviews` tables if they don't exist
- Inserts at least 400 reviews from `data/processed/reviews_with_sentiment.csv`

## 5. Verify Data Integrity

Run these queries in `psql`:

```sql
-- Count reviews per bank
SELECT bank_name, COUNT(*) FROM reviews JOIN banks USING(bank_id) GROUP BY bank_name;

-- Average rating across all reviews
SELECT AVG(rating) FROM reviews;
```

## Notes

- Update `DB_USER`, `DB_PASSWORD`, and other connection parameters in `store_reviews_postgres.py`.
- Ensure the CSV file `reviews_with_sentiment.csv` exists in `data/processed/`.
