import os
from flask import Flask, render_template, request
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return textz

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

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        new_cv_file = request.files['new_cv_path']
        new_cv_path = 'samples_of_pdf/' + new_cv_file.filename
        new_cv_file.save(new_cv_path)

        jd_file = request.files['jd_file']
        jd_path = 'samples_of_pdf/' + jd_file.filename
        jd_file.save(jd_path)

        new_cv_text = extract_text_from_pdf(new_cv_path)
        jd_text = extract_text_from_pdf(jd_path)

        new_cv_text = ' '.join(new_cv_text.split())
        jd_text = ' '.join(jd_text.split())

        new_cv_tfidf = tfidf_vectorizer.transform([new_cv_text])
        jd_tfidf = tfidf_vectorizer.transform([jd_text])

        most_similar_tag_cv = predict_category(new_cv_tfidf, tfidf_matrix, resume_data_common)
        most_similar_tag_jd = predict_category(jd_tfidf, tfidf_matrix, resume_data_common)

        if most_similar_tag_cv is not None and most_similar_tag_jd is not None:
            return render_template('result.html', category_cv=most_similar_tag_cv, category_jd=most_similar_tag_jd)
        else:
            return render_template('result.html', category_cv='Unknown', category_jd='Unknown')

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
