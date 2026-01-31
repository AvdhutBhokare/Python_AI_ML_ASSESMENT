"""
Scenario 1: Data Validation
Task: Write a function validate_data(data) that checks if a list of dictionaries 
contains valid integer values for the "age" key. Return a list of invalid entries.
"""

def validate_data(data):
    invalid_entries = []
    
    for entry in data:
        if 'age' not in entry or not isinstance(entry['age'], int) or isinstance(entry['age'], bool):
            invalid_entries.append(entry)
    
    return invalid_entries


# Example input data
data = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": "25"},
    {"name": "Charlie", "age": 35},
    {"name": "Diana", "age": 28.5}
]

# Function call
result = validate_data(data)

# Output
print(result)
