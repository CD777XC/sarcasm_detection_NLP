# Importing modules
import joblib
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split

# Loading models
baseline_model = joblib.load('./models/baseline_model.pkl')

# Importing dataframe
df = pd.read_csv('./clean_data/sarcasm_headlines_v2_clean.csv')

# Vectorizing the data
tfid_vectorizer = TfidfVectorizer(max_df = 0.75, max_features = 5000, ngram_range=(1,2))
weighted_words = pd.DataFrame(tfid_vectorizer.fit_transform(df['cleaned_headline']).toarray(), 
                              columns=tfid_vectorizer.get_feature_names_out())

# Defining X and y, and splitting dataset to train/test
X = weighted_words
y = df['is_sarcastic']
_, X_test, _, y_test = train_test_split(X, y, random_state=42, test_size=.2)

def baseline_model_score(baseline_model):
    score = baseline_model.score(X_test, y_test)
    return round(score, 4)

print(baseline_model_score(baseline_model=baseline_model))