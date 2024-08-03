# Importing modules
from fastapi import FastAPI
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Defining app name
sarcasm_detection=FastAPI()

# Importing models
baseline_model = joblib.load('./models/baseline_model.pkl')

# Importing dataframe
df = pd.read_csv('./clean_data/sarcasm_headlines_v2_clean.csv')

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
    # Vectorizing the data
    tfid_vectorizer = TfidfVectorizer(max_df = 0.75, max_features = 5000, ngram_range=(1,2))
    weighted_words = pd.DataFrame(tfid_vectorizer.fit_transform(df['cleaned_headline']).toarray(), 
                                columns=tfid_vectorizer.get_feature_names_out())

    # Defining X and y, and splitting dataset to train/test
    X = weighted_words
    y = df['is_sarcastic']
    _, X_test, _, y_test = train_test_split(X, y, random_state=42, test_size=.2)
    score = baseline_model.score(X_test, y_test)
    return {'Baseline model score': round(score, 4)}