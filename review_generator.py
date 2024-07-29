import pandas as pd
import random

# Define number of reviews per type
num_reviews = 500  # 500 positive and 500 negative to make 1000 reviews

# Sample positive and negative reviews
positive_reviews = [
    "The product is fantastic and exceeded my expectations.",
    "I am extremely satisfied with this purchase.",
    "Great value for the money.",
    "The quality is top-notch and the design is sleek.",
    "Excellent product, would highly recommend."
] * (num_reviews // 5)

negative_reviews = [
    "The product did not meet my expectations.",
    "It arrived damaged and was not usable.",
    "Very poor quality and overpriced.",
    "The item was defective and I had to return it.",
    "Not as described and very disappointing."
] * (num_reviews // 5)

# Ensure the lists are exactly the right length
positive_reviews = positive_reviews[:num_reviews]
negative_reviews = negative_reviews[:num_reviews]

# Shuffle the reviews to mix positive and negative
all_reviews = positive_reviews + negative_reviews
random.shuffle(all_reviews)

# Create DataFrame
df = pd.DataFrame({
    "REVIEW_NUMBER": range(1, len(all_reviews) + 1),
    "REVIEW_SUMMARY": all_reviews
})

# Save to CSV
df.to_csv(r'C:\Users\HP\Desktop\Yaohan-Vishleshan\Smart Review System\product_review.csv', index=False)
