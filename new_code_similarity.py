import os
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


# Example usage
root_directories = {
    'Frontend React': "generator_stack/frontend_react_pdfs",
    'QA': "generator_stack/qa_pdfs",
    'DevOps': "generator_stack/devops_pdfs",
    'Business Analytics': "generator_stack/business_analytics_pdfs",
    '.NET': "generator_stack/dotnet_dev_pdfs",
    'Golang': "generator_stack/golang_dev_pdfs",
    'Python': "generator_stack/python_dev_pdfs",
    'Java': "generator_stack/java_dev_pdfs",
}


def predict_category(new_cv_tfidf, tfidf_matrix, data):
    cosine_similarities = cosine_similarity(new_cv_tfidf, tfidf_matrix)
    most_similar_index = cosine_similarities.argmax()
    if most_similar_index < len(data):
        return data[most_similar_index][1]
    return None


# Example usage
resume_data_common = []

for role, directory in root_directories.items():
    for filename in os.listdir(directory):
        if filename.endswith(".pdf"):
            resume_path = os.path.join(directory, filename)
            text = extract_text_from_pdf(resume_path)
            resume_data_common.append((text, role))

# Train TF-IDF vectorizer on training data
tfidf_vectorizer = TfidfVectorizer()
tfidf_matrix = tfidf_vectorizer.fit_transform([text for text, _ in resume_data_common])

# Example usage for predicting category
new_cv_path = "JD.pdf"
new_cv_text = extract_text_from_pdf(new_cv_path)
new_cv_text = ' '.join(new_cv_text.split())

# Transform the new CV
new_cv_tfidf = tfidf_vectorizer.transform([new_cv_text])

# Predict category using TF-IDF and cosine similarity
most_similar_tag = predict_category(new_cv_tfidf, tfidf_matrix, resume_data_common)

if most_similar_tag is not None:
    print(f"The predicted category for the new CV is: {most_similar_tag}")






