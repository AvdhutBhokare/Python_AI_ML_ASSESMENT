# How to Run the Code

## Setup Instructions

### 1. Install Python
Make sure you have Python 3.8 or higher installed on your system.

### 2. Install Dependencies
Open terminal/command prompt and navigate to the project directory, then run:

```bash
pip install -r requirements.txt
```

Or install individually:
```bash
pip install numpy pandas scikit-learn tensorflow google-generativeai matplotlib
```

### 3. API Key Setup (For Scenarios 9 & 10)
For Gemini API scenarios, you need to:
1. Get a Gemini API key from https://makersuite.google.com/app/apikey
2. Replace `"YOUR_API_KEY_HERE"` in the following files:
   - `scenario_09_gemini_api_json.py`
   - `scenario_10_summarization.py`

## Running Individual Scenarios

Navigate to the project directory and run any scenario:

```bash
python scenario_01_data_validation.py
python scenario_02_logging_decorator.py
python scenario_03_missing_value_handling.py
python scenario_04_text_preprocessing.py
python scenario_05_hyperparameter_tuning.py
python scenario_06_custom_evaluation_metric.py
python scenario_07_image_augmentation.py
python scenario_08_model_callbacks.py
python scenario_09_gemini_api_json.py
python scenario_10_summarization.py
```

## Running All Scenarios

On Linux/Mac:
```bash
for file in scenario_*.py; do echo "Running $file"; python "$file"; echo ""; done
```

On Windows (PowerShell):
```powershell
Get-ChildItem scenario_*.py | ForEach-Object { Write-Host "Running $($_.Name)"; python $_.FullName; Write-Host "" }
```

## Notes

- Scenarios 1-8 don't require any API keys and will run immediately
- Scenarios 9-10 require a valid Gemini API key
- Some scenarios may take a few seconds to complete (especially ML training scenarios)
- TensorFlow warnings about GPU can be ignored if you're running on CPU

## Troubleshooting

**ImportError**: Make sure all dependencies are installed
```bash
pip install -r requirements.txt
```

**API Key Error**: Ensure you've replaced `"YOUR_API_KEY_HERE"` with your actual Gemini API key

**TensorFlow Warnings**: These are normal and can be ignored for learning purposes
