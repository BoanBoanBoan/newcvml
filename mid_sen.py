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


# Function to predict category using TF-IDF and cosine similarity
def predict_category(new_cv_tfidf, tfidf_matrix, data):
    cosine_similarities = cosine_similarity(new_cv_tfidf, tfidf_matrix)
    most_similar_index = cosine_similarities.argmax()
    if most_similar_index < len(data):
        return data[most_similar_index][1]
    return None


# Example usage
root_directories = {
    'Senior Specialist': "generator_pos/senior_specialist_pdfs",
    'Middle Specialist': "generator_pos/middle_specialist_pdfs",
}

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
new_cv_path = "JD (1).pdf"
new_cv_text = extract_text_from_pdf(new_cv_path)
new_cv_text = ' '.join(new_cv_text.split())

# Check if the word "computer science" or similar is present in the new CV
if "senior" in new_cv_text.lower() or "team lead" in new_cv_text.lower():
    most_similar_tag = 'Senior Specialist'
    confidence_percentage = 100.0
else:
    # Transform the new CV
    new_cv_tfidf = tfidf_vectorizer.transform([new_cv_text])

    # Predict category using TF-IDF and cosine similarity
    most_similar_tag = predict_category(new_cv_tfidf, tfidf_matrix, resume_data_common)

if most_similar_tag is not None:
    print(f"The predicted category for the new CV is: {most_similar_tag}")
