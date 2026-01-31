"""
Scenario 9: Gemini API JSON Response
Task: Use the Gemini API to generate a response in JSON format for the query: 
"List 3 benefits of Python for data science." Handle cases where the response isn't valid JSON.
"""

import google.generativeai as genai
import json
import os

# Configure Gemini API
api_key = "YOUR_API_KEY_HERE"  # Replace with your actual API key
genai.configure(api_key=api_key)

# Create model
model = genai.GenerativeModel('gemini-pro')

# Query
query = "List 3 benefits of Python for data science. Return the response in JSON format with a 'benefits' key containing an array of objects, each with 'title' and 'description' fields."

try:
    # Generate response
    response = model.generate_content(query)
    response_text = response.text
    
    print("Raw Response:")
    print(response_text)
    print("\n" + "="*50 + "\n")
    
    # Try to parse JSON
    try:
        # Clean response (remove markdown code blocks if present)
        cleaned_text = response_text.strip()
        if cleaned_text.startswith("```json"):
            cleaned_text = cleaned_text[7:]
        if cleaned_text.startswith("```"):
            cleaned_text = cleaned_text[3:]
        if cleaned_text.endswith("```"):
            cleaned_text = cleaned_text[:-3]
        cleaned_text = cleaned_text.strip()
        
        # Parse JSON
        json_response = json.loads(cleaned_text)
        
        print("Parsed JSON Response:")
        print(json.dumps(json_response, indent=2))
        
        # Access the benefits
        if 'benefits' in json_response:
            print("\n" + "="*50 + "\n")
            print("Benefits of Python for Data Science:")
            for i, benefit in enumerate(json_response['benefits'], 1):
                print(f"\n{i}. {benefit.get('title', 'N/A')}")
                print(f"   {benefit.get('description', 'N/A')}")
        
    except json.JSONDecodeError as e:
        print(f"Error: Response is not valid JSON")
        print(f"JSON Error: {e}")
        print("\nFallback - Displaying raw text response:")
        print(response_text)
        
except Exception as e:
    print(f"Error calling Gemini API: {e}")
