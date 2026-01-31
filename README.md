# Python & AIML Knowledge Assessment

This repository contains solutions to various Python and AI/ML scenarios covering data validation, decorators, data preprocessing, machine learning, deep learning, and generative AI.

## 📋 Table of Contents

1. [Scenario 1: Data Validation](#scenario-1-data-validation)
2. [Scenario 2: Logging Decorator](#scenario-2-logging-decorator)
3. [Scenario 3: Missing Value Handling](#scenario-3-missing-value-handling)
4. [Scenario 4: Text Pre-processing](#scenario-4-text-pre-processing)
5. [Scenario 5: Hyperparameter Tuning](#scenario-5-hyperparameter-tuning)
6. [Scenario 6: Custom Evaluation Metric](#scenario-6-custom-evaluation-metric)
7. [Scenario 7: Image Augmentation Pipeline](#scenario-7-image-augmentation-pipeline)
8. [Scenario 8: Model Callbacks](#scenario-8-model-callbacks)
9. [Scenario 9: Gemini API JSON Response](#scenario-9-gemini-api-json-response)
10. [Scenario 10: Summarization with Constraints](#scenario-10-summarization-with-constraints)

## 🚀 Requirements

```bash
pip install -r requirements.txt
```

## 📁 Project Structure

```
python-aiml-assessment/
├── README.md
├── requirements.txt
├── scenario_01_data_validation.py
├── scenario_02_logging_decorator.py
├── scenario_03_missing_value_handling.py
├── scenario_04_text_preprocessing.py
├── scenario_05_hyperparameter_tuning.py
├── scenario_06_custom_evaluation_metric.py
├── scenario_07_image_augmentation.py
├── scenario_08_model_callbacks.py
├── scenario_09_gemini_api_json.py
└── scenario_10_summarization.py
```

## 📝 Scenario Descriptions

### Scenario 1: Data Validation
Validates integer values in the "age" key of a list of dictionaries and returns invalid entries.

### Scenario 2: Logging Decorator
Creates a decorator that logs execution time of functions.

### Scenario 3: Missing Value Handling
Handles missing values in a dataset using median (normal distribution) or mode (skewed distribution).

### Scenario 4: Text Pre-processing
Cleans text data by converting to lowercase, removing special characters, and tokenizing.

### Scenario 5: Hyperparameter Tuning
Uses GridSearchCV to find optimal hyperparameters for Random Forest classifier.

### Scenario 6: Custom Evaluation Metric
Implements weighted accuracy metric with different class weights.

### Scenario 7: Image Augmentation Pipeline
Creates an image augmentation pipeline using TensorFlow/Keras with rotations, flips, and zoom.

### Scenario 8: Model Callbacks
Implements EarlyStopping callback for neural network training.

### Scenario 9: Gemini API JSON Response
Uses Gemini API to generate JSON responses with error handling.

### Scenario 10: Summarization with Constraints
Summarizes text with word limit constraints using Gemini API.

## 🏃 Running the Scripts

Each scenario is in a separate Python file. Run them individually:

```bash
python scenario_01_data_validation.py
python scenario_02_logging_decorator.py
# ... and so on
```

## 👤 Author

Created for Python & AIML Knowledge Assessment

## 📄 License

This project is for educational purposes.
