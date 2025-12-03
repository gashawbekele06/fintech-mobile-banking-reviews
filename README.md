# FINTECH Mobile Banking Reviews

## Overview

This project analyzes customer satisfaction with mobile banking apps by collecting and processing user reviews from the Google Play Store for Ethiopian banks:

- **Commercial Bank of Ethiopia (CBE)**
- **Bank of Abyssinia**
- **Dashen Bank**

## Business Objective

Omega Consultancy is supporting banks to improve their mobile apps to enhance customer retention and satisfaction. This project analyzes user reviews from Google Play Store for three banking apps. The goal is to collect, preprocess, and store reviews, perform sentiment and thematic analysis, and derive actionable insights for app improvement.

---

## Key Features

- **Data Collection:** Scrape reviews for three major banking apps using `google-play-scraper`.
- **Preprocessing:** Clean and normalize review data for analysis.
- **Sentiment Analysis:** Use advanced NLP models (DistilBERT) and compare with simpler methods (VADER/TextBlob).
- **Thematic Analysis:** Identify recurring themes using TF-IDF and clustering.
- **Database Integration:** Store cleaned data in PostgreSQL for persistence.
- **Visualization:** Generate plots for sentiment trends, rating distributions, and keyword clouds.

---

## 📂 Folder Structure

```
FINTECH-MOBILE-BANKING-REVIEWS/
│
├── .vscode/              # VS Code settings
├── data/                 # Raw and processed datasets
├── insights_outputs/     # Insights and analysis outputs
├── notebooks/            # Jupyter notebooks for experiments
├── outputs/              # Generated plots and reports
├── sql/                  # SQL scripts and database schema
├── src/                  # Source code for scraping, analysis, and DB integration
├── venv/                 # Python virtual environment
├── .env                  # Environment variables (database credentials, API keys)
├── .gitignore            # Git ignore file
├── LICENSE               # Project license (Apache-2.0)
├── README.md             # Project documentation
├── requirements.txt      # Python dependencies
└── reviews_final_fallback.csv  # Final cleaned dataset
```

## **Deliverables and Tasks**

### Data Collection and Preprocessing

- **Git Setup**
  - Create a GitHub repository.
  - Include `.gitignore` and `requirements.txt`.
  - Use `task-1` branch; commit frequently with meaningful messages.
- **Web Scraping**
  - Use `google-play-scraper` to collect reviews, ratings, dates, and app names for **three banks**.
  - Target **400+ reviews per bank** (≥1,200 total).
- **Preprocessing**
  - Remove duplicates, handle missing data.
  - Normalize dates (format: `YYYY-MM-DD`).
  - Save as CSV with columns: `review`, `rating`, `date`, `bank`, `source`.

### Sentiment and Thematic Analysis

#### Tasks

- **Sentiment Analysis**
  - Use `distilbert-base-uncased-finetuned-sst-2-english` or simpler libraries like VADER/TextBlob.
  - Aggregate by bank and rating.
- **Thematic Analysis**
  - Extract keywords and n-grams using TF-IDF or spaCy.
  - Group related keywords into **3–5 themes per bank** (e.g., UI, reliability, customer support).
- **Pipeline**
  - Preprocess text (tokenization, stop-word removal, lemmatization).
  - Save results as CSV: `review_id`, `review_text`, `sentiment_label`, `sentiment_score`, `theme(s)`.

### Store Cleaned Data in PostgreSQL

#### Tasks

- Install PostgreSQL and create `bank_reviews` database.
- Define schema:
  - **Banks Table:** `bank_id (PK)`, `bank_name`, `app_name`.
  - **Reviews Table:** `review_id (PK)`, `bank_id (FK)`, `review_text`, `rating`, `review_date`, `sentiment_label`, `sentiment_score`, `source`.
- Insert cleaned data using Python (`psycopg2` or SQLAlchemy).
- Verify data integrity with SQL queries.

### Insights and Recommendations

#### Tasks

- Identify ≥2 drivers and pain points per bank.
- Compare banks and suggest ≥2 improvements per bank.
- Create 3–5 plots (Matplotlib/Seaborn): sentiment trends, rating distributions, keyword clouds.
- Note potential review biases.

## Setup Instructions

## Installation

1. **Clone the repository:**

```bash
git clone https://github.com/gashawbekele06/fintech-mobile-banking-reviews.git
cd fintech-mobile-banking-reviews
```

2. **Install dependencies:**

```bash
pip install -r requirements.txt
```

3. **Set up PostgreSQL:**

- Install PostgreSQL and create a database named `bank_reviews`.
- Update connection details in `src/db_config.py`.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

---

## License

This project is licensed under the Apache-2.0 License.
