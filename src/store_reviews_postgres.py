
"""
store_reviews_postgres.py

This script connects to a PostgreSQL database, creates schema for banks and reviews,
and inserts ALL cleaned review data from CSV using dynamic path resolution.
"""

import psycopg2
import pandas as pd
from pathlib import Path

# Database connection parameters
DB_NAME = "bank_reviews"
DB_USER = "postgres"
DB_PASSWORD = "13621"
DB_HOST = "localhost"
DB_PORT = "5432"

# Locate CSV dynamically
cwd = Path.cwd()
project_root = cwd.parent if cwd.name == "notebooks" else next((p for p in cwd.parents if (p / "src").exists()), cwd)
CSV_PATH = project_root / "data" / "processed" / "reviews_with_sentiment.csv"
print(f"Resolved CSV path: {CSV_PATH}")


def get_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )


def create_tables(conn):
    with conn.cursor() as cur:
        cur.execute("""
        CREATE TABLE IF NOT EXISTS banks (
            bank_id SERIAL PRIMARY KEY,
            bank_name TEXT UNIQUE NOT NULL,
            app_name TEXT
        );
        """)
        cur.execute("""
        CREATE TABLE IF NOT EXISTS reviews (
            review_id SERIAL PRIMARY KEY,
            bank_id INT REFERENCES banks(bank_id),
            review_text TEXT,
            rating FLOAT,
            review_date DATE,
            sentiment_label TEXT,
            sentiment_score FLOAT,
            source TEXT
        );
        """)
        conn.commit()
        print("✅ Tables created successfully")


def insert_data(conn):
    df = pd.read_csv(CSV_PATH)
    print(f"Total reviews to insert: {len(df)}")

    with conn.cursor() as cur:
        # Insert unique banks and get their IDs
        banks = df['bank_name'].unique()
        bank_ids = {}
        for bank in banks:
            cur.execute("""
                INSERT INTO banks (bank_name, app_name)
                VALUES (%s, %s)
                ON CONFLICT (bank_name) DO NOTHING
                RETURNING bank_id
            """, (bank, None))
            result = cur.fetchone()
            if result:
                bank_ids[bank] = result[0]
            else:
                # Fetch existing bank_id if already inserted
                cur.execute("SELECT bank_id FROM banks WHERE bank_name=%s", (bank,))
                bank_ids[bank] = cur.fetchone()[0]

        # Prepare review data for batch insert
        review_records = [
            (
                bank_ids[row['bank_name']],
                row['review_text'],
                row.get('rating', None),
                row.get('review_date', None),
                row.get('sentiment_label', None),
                row.get('sentiment_score', None),
                row.get('source', None)
            )
            for _, row in df.iterrows()
        ]

        # Batch insert reviews
        cur.executemany("""
            INSERT INTO reviews (bank_id, review_text, rating, review_date, sentiment_label, sentiment_score, source)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, review_records)

        conn.commit()
        print(f"✅ Inserted {len(review_records)} reviews successfully")


def verify_data(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT bank_name, COUNT(*) FROM reviews JOIN banks USING(bank_id) GROUP BY bank_name")
        print("\nReviews per bank:")
        for row in cur.fetchall():
            print(row)

        cur.execute("SELECT AVG(rating) FROM reviews")
        avg_rating = cur.fetchone()[0]
        print(f"\nAverage rating: {avg_rating}")


if __name__ == "__main__":
    conn = get_connection()
    create_tables(conn)
    insert_data(conn)
    verify_data(conn)
    conn.close()
