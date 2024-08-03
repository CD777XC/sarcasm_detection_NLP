# Importing modules
from fastapi import FastAPI
import joblib
from test_model import baseline_model_score

# Defining app name
sarcasm_detection=FastAPI()

# Importing models
baseline_model = joblib.load('./models/baseline_model.pkl')

# Defining root endpoint
@sarcasm_detection.get('/')
def index():
    return {'Project': 'Sarcasm news headline detection',
            'Description': 'Using NLP to detect sarcasm in news headlines in order to avoid misinformation. Data collected on Kaggle. Please see README.md file at github project repository: https://github.com/CD777XC/sarcasm_detection_NLP'}

@sarcasm_detection.get('/health')
def health():
    return {'API working': 'Yes'}

@sarcasm_detection.post('/baseline_score')
def baseline_score():
    score = baseline_model_score(baseline_model=baseline_model)
    return {'Baseline model score': score}