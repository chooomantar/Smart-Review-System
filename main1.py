from flask import Flask, jsonify, send_from_directory
import pandas as pd
from textblob import TextBlob
import logging

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.DEBUG)

# Serve the main HTML file
@app.route('/')
def index():
    return send_from_directory('', 'index1.html')

# Serve any other static files (CSS, JS, etc.)
@app.route('/<path:path>')
def static_files(path):
    return send_from_directory('', path)

def summarize_reviews():
    try:
        # Load reviews from CSV
        df = pd.read_csv('product_review.csv')
        logging.debug(f"DataFrame loaded with {len(df)} reviews.")
        
        # Ensure there are reviews to process
        if df.empty:
            return {"summary": "No reviews available."}
        
        # Extract reviews
        reviews = df['REVIEW_SUMMARY'].tolist()
        logging.debug(f"Reviews extracted: {reviews}")

        # Analyze sentiment
        positive_reviews = [review for review in reviews if TextBlob(review).sentiment.polarity > 0]
        negative_reviews = [review for review in reviews if TextBlob(review).sentiment.polarity <= 0]

        logging.debug(f"Positive reviews: {positive_reviews}")
        logging.debug(f"Negative reviews: {negative_reviews}")

        # Function to concatenate reviews until a minimum word count is met
        def concatenate_reviews(reviews, min_words):
            summary = []
            total_words = 0
            for review in reviews:
                if total_words >= min_words:
                    break
                words = review.split()
                summary.extend(words)
                total_words += len(words)
            return " ".join(summary)
        
        # Generate summaries
        positive_summary = concatenate_reviews(positive_reviews, 150) if positive_reviews else "No positive reviews."
        negative_summary = concatenate_reviews(negative_reviews, 150) if negative_reviews else "No negative reviews."

        # Format output
        result = {
            "summary": (
                f"Customers said that {positive_summary}. "
                f"However, they also said that {negative_summary}."
            )
        }
        
        return result
    except Exception as e:
        logging.error(f"Exception occurred: {e}")
        return {"error": f"Error during summarization: {str(e)}"}

@app.route('/summarize', methods=['GET'])
def summarize():
    summary = summarize_reviews()
    return jsonify(summary)

if __name__ == '__main__':
    app.run(debug=True)
