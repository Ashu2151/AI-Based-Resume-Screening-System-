import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('english'))

def preprocess_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)

    words = word_tokenize(text)

    filtered_words = [
        word for word in words
        if word not in stop_words
        and len(word) > 2
    ]

    return " ".join(filtered_words)
