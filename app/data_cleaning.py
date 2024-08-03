# Import basic modules
import pandas as pd
import time

# Language Processing packages/modules
import word2vec as w2v
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords 
import nltk
import string
import text_unidecode as unidecode
from nltk.stem import WordNetLemmatizer 

# Data loading packages/modules
import json

# Ensuring required NLTK content is downloaded
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

#### DATA CLEANING SCRIPT - RETURNING CLEAN DATA ####

print('##### Starting data cleaning... 🧹 #####')
start = time.time()

# Loading data
df = pd.read_json('./raw_data/sarcasm_headlines_v2.json', lines=True)
df.drop(columns='article_link', inplace=True)

def clean_text(sentence):
    # Return a sentenced cleaned and ready to be vectorized

    # Lowercase the sentence
    sentence = sentence.lower()

    # Removes digit
    sentence = ''.join(char for char in sentence if not char.isdigit())

    # Removes punctuation and symbols
    for punct in string.punctuation:
        sentence = sentence.replace(punct, '')

    # Strip white spaces at the beginning and end of sentence
    sentence = sentence.strip()
    
    # Tokenizing
    sentence = word_tokenize(sentence)
    
    # Lemmatize verbs and nouns
    lemmatizer = WordNetLemmatizer()
    sentence = [lemmatizer.lemmatize(word, pos='v') for word in sentence]
    sentence = [lemmatizer.lemmatize(word, pos='n') for word in sentence]

    # Returning sentence as a string
    cleaned_sentence = ' '.join(sentence)
    return cleaned_sentence

df['cleaned_headline'] = df['headline'].apply(clean_text)

df.drop(columns='headline', inplace=True)

df.to_csv('./clean_data/sarcasm_headlines_v2_clean.csv', index=False)

end = time.time()

print('##### Data cleaned successfuly ✅ #####')
print('##### File saved at: ./clean_data #####')
print(f'---{round(end-start, 2)} seconds---')
