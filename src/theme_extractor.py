
"""
Theme Extractor for Bank Reviews Analysis Project
Uses TF-IDF for keyword extraction and clusters keywords into themes.
"""

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from config import DATA_PATHS


class ThemeExtractor:
    def __init__(self):
        self.sentiment_path = DATA_PATHS['sentiment_results']
        self.final_path = DATA_PATHS['final_results']
        self.themes = {
            'Login Issues': ['login', 'password', 'authentication', 'sign in'],
            'Transaction Speed': ['slow', 'delay', 'transfer', 'loading'],
            'UI/UX': ['interface', 'design', 'navigation', 'layout'],
            'Feature Requests': ['feature', 'update', 'fingerprint', 'option'],
            'Customer Support': ['support', 'help', 'service', 'response']
        }

    def load_data(self):
        if not os.path.exists(self.sentiment_path):
            raise FileNotFoundError(f"Sentiment results file not found at {self.sentiment_path}")
        print(f"Loading sentiment results from {self.sentiment_path}...")
        return pd.read_csv(self.sentiment_path)

    def extract_keywords(self, df, max_features=100):
        print("Extracting keywords using TF-IDF...")
        vectorizer = TfidfVectorizer(stop_words='english', max_features=max_features)
        tfidf_matrix = vectorizer.fit_transform(df['review_text'].astype(str))
        keywords = vectorizer.get_feature_names_out()
        return keywords

    def assign_themes(self, df):
        print("Assigning themes to reviews...")
        assigned_themes = []
        for text in df['review_text'].astype(str):
            text_lower = text.lower()
            matched = []
            for theme, keywords in self.themes.items():
                if any(word in text_lower for word in keywords):
                    matched.append(theme)
            assigned_themes.append(", ".join(matched) if matched else "Other")
        df['themes'] = assigned_themes
        return df

    def save_results(self, df):
        os.makedirs(os.path.dirname(self.final_path), exist_ok=True)
        df.to_csv(self.final_path, index=False)
        print(f"✅ Final results with themes saved to {self.final_path}")

    def run(self):
        df = self.load_data()
        self.extract_keywords(df)
        df = self.assign_themes(df)
        self.save_results(df)
        print(f"Total reviews processed: {len(df)}")
        return df


def main():
    extractor = ThemeExtractor()
    extractor.run()


if __name__ == "__main__":
    main()
