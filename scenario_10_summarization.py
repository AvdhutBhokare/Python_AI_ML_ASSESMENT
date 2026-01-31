"""
Scenario 10: Summarization with Constraints
Task: Write a prompt to summarize a news article into 2 sentences. 
If the summary exceeds 50 words, truncate it to the nearest complete sentence.
"""

import google.generativeai as genai

# Configure Gemini API
api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel('gemini-pro')

# Example news article
news_article = """
Scientists have discovered a new species of deep-sea fish in the Mariana Trench, 
living at depths exceeding 8,000 meters. The fish, named Pseudoliparis swirei, 
has adapted to extreme pressure and darkness. Researchers from the University of 
Washington used advanced submersibles to capture footage of the species. This 
discovery highlights the biodiversity of unexplored ocean regions and raises 
questions about life in extreme environments. The findings were published in the 
journal Nature and could help scientists understand evolutionary adaptations.
"""

# Create prompt for summarization
prompt = f"""
Summarize the following news article in exactly 2 sentences. 
Keep the summary concise and informative.

Article:
{news_article}

Provide only the 2-sentence summary, nothing else.
"""

# Generate summary
response = model.generate_content(prompt)
summary = response.text.strip()

# Count words and check if exceeds 50 words
words = summary.split()
word_count = len(words)

print("Original Summary:")
print(summary)
print(f"\nWord Count: {word_count}")

# If summary exceeds 50 words, truncate to nearest complete sentence
if word_count > 50:
    truncated = []
    current_count = 0
    sentences = summary.split('. ')
    
    for sentence in sentences:
        sentence_words = sentence.split()
        if current_count + len(sentence_words) <= 50:
            truncated.append(sentence)
            current_count += len(sentence_words)
        else:
            break
    
    final_summary = '. '.join(truncated)
    if not final_summary.endswith('.'):
        final_summary += '.'
    
    print("\n" + "="*50)
    print("Truncated Summary (≤50 words):")
    print(final_summary)
    print(f"\nNew Word Count: {len(final_summary.split())}")
else:
    print("\n" + "="*50)
    print("Summary is within 50-word limit. No truncation needed.")
