# Importing modules
from fastapi import FastAPI

# Defining app name
sarcasm_detection=FastAPI()

# Defining root endpoint
@sarcasm_detection.get('/')
def index():
    return {'Project': 'Sarcasm news headline detection',
            'Description': 'Using NLP to detect sarcasm in news headlines in order to avoid misinformation. Data collected on Kaggle. Please see README.md file at github project repository: https://github.com/CD777XC/sarcasm_detection_NLP'}

