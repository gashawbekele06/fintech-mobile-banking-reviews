
"""
Sentiment Analyzer for Bank Reviews Analysis Project
Uses HuggingFace DistilBERT model for sentiment classification.
"""

import os
import pandas as pd
from transformers import pipeline
from config import DATA_PATHS


class SentimentAnalyzer:
    def __init__(self):
        self.processed_path = DATA_PATHS['processed_reviews']
        self.sentiment_path = DATA_PATHS['sentiment_results']
        print("Loading sentiment analysis model...")
        self.model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")

    def load_data(self):
        if not os.path.exists(self.processed_path):
            raise FileNotFoundError(f"Processed reviews file not found at {self.processed_path}")
        print(f"Loading processed reviews from {self.processed_path}...")
        return pd.read_csv(self.processed_path)

    def analyze_sentiment(self, df):
        print("Performing sentiment analysis...")
        sentiments = []
        for text in df['review_text']:
            if isinstance(text, str) and text.strip():
                result = self.model(text[:512])[0]  # Limit to 512 tokens
                sentiments.append({
                    'label': result['label'],
                    'score': result['score']
                })
            else:
                sentiments.append({'label': 'NEUTRAL', 'score': 0.0})

        df['sentiment_label'] = [s['label'] for s in sentiments]
        df['sentiment_score'] = [s['score'] for s in sentiments]
        return df

    def save_results(self, df):
        os.makedirs(os.path.dirname(self.sentiment_path), exist_ok=True)
        df.to_csv(self.sentiment_path, index=False)
        print(f"✅ Sentiment analysis results saved to {self.sentiment_path}")

    def run(self):
        df = self.load_data()
        df = self.analyze_sentiment(df)
        self.save_results(df)
        print(f"Total reviews analyzed: {len(df)}")
        return df


def main():
    analyzer = SentimentAnalyzer()
    analyzer.run()


if __name__ == "__main__":
    main()
