from sklearn.feature_extraction.text import TfidfVectorizer

def vectorize_text(resume_text, job_description):

    texts = [resume_text, job_description]

    vectorizer = TfidfVectorizer()

    vectors = vectorizer.fit_transform(texts)

    return vectors