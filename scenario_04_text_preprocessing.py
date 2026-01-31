"""
Scenario 4: Text Pre-processing
Task: Clean a text column in a DataFrame by:
1. Converting to lowercase.
2. Removing special characters (e.g., !, @).
3. Tokenizing the text.
"""

import pandas as pd
import re

# Example input data
data = {
    "id": [1, 2, 3, 4],
    "text": [
        "Hello World! How are you?",
        "Python is AMAZING @2024",
        "Data Science & Machine Learning!!!",
        "Clean YOUR data#properly."
    ]
}

df = pd.DataFrame(data)

def clean_text(text):
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters (keep only letters, numbers, and spaces)
    text = re.sub(r'[^a-z0-9\s]', '', text)
    
    # Tokenize the text (split by spaces)
    tokens = text.split()
    
    return tokens

# Apply cleaning function to text column
df['cleaned_tokens'] = df['text'].apply(clean_text)

# Output
print("Original DataFrame:")
print(df[['id', 'text']])
print("\nCleaned and Tokenized:")
print(df[['id', 'cleaned_tokens']])
