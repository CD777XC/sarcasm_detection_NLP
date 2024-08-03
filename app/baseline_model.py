# Importing basic modules
import pandas as pd
import time

# Importing model modules
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
import joblib

#### BASELINE MODEL SCRIPT - RETURNING .PKL MODEL ####

print('##### Building baseline model... 🛠️ #####')
start = time.time()

# Importing dataframe
df = pd.read_csv('./clean_data/sarcasm_headlines_v2_clean.csv')

# Vectorizing the data
tfid_vectorizer = TfidfVectorizer(max_df = 0.75, max_features = 5000, ngram_range=(1,2))
weighted_words = pd.DataFrame(tfid_vectorizer.fit_transform(df['cleaned_headline']).toarray(), 
                              columns=tfid_vectorizer.get_feature_names_out())

# Defining X and y, and splitting dataset to train/test
X = weighted_words
y = df['is_sarcastic']
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=.2)

# Instanciating LogisticRegression model
log_reg = LogisticRegression(n_jobs=-1)

baseline_model = log_reg.fit(X=X_train, y=y_train)

joblib.dump(baseline_model, './models/baseline_model.pkl')

end = time.time()

print('##### Baseline model built successfuly ✅ #####')
print('##### File saved at: ./models #####')
print(f'---{round(end-start, 2)} seconds---')