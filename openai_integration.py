import os
import streamlit as st
import pypdf
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from openai import OpenAI

client = OpenAI(api_key="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")


# Function to extract text from a PDF file
def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = pypdf.PdfReader(file)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return text


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

# Streamlit code starts here
st.title('Category Prediction')

new_cv_file = st.file_uploader("Upload new CV (PDF)", type=['pdf'])
jd_file = st.file_uploader("Upload Job Description (PDF)", type=['pdf'])

if st.button('Predict'):
    if new_cv_file is not None and jd_file is not None:
        new_cv_path = 'samples_of_pdf/' + new_cv_file.name
        jd_path = 'samples_of_pdf/' + jd_file.name

        new_cv_text = extract_text_from_pdf(new_cv_path)
        jd_text = extract_text_from_pdf(jd_path)

        new_cv_text = ' '.join(new_cv_text.split())
        jd_text = ' '.join(jd_text.split())

        new_cv_tfidf = tfidf_vectorizer.transform([new_cv_text])
        jd_tfidf = tfidf_vectorizer.transform([jd_text])

        most_similar_tag_cv = predict_category(new_cv_tfidf, tfidf_matrix, resume_data_common)
        most_similar_tag_jd = predict_category(jd_tfidf, tfidf_matrix, resume_data_common)

        if most_similar_tag_cv is not None and most_similar_tag_jd is not None:
            st.write('The predicted category for the new CV is:', most_similar_tag_cv)
            st.write('The predicted category for the Job Description is:', most_similar_tag_jd)
        else:
            st.write('The predicted category for the new CV is: Unknown')
            st.write('The predicted category for the Job Description is: Unknown')

        prompt = f"Analyze this resume against the job description: \n\nJob Description:\n{jd_text}\n\nResume:\n{new_cv_text}\n\nProvide a percentage match and recommendations for improvement."

        analyze_button = st.button('Analyze')

analyze_button = st.button('Analyze')

if analyze_button:

    if new_cv_file is not None and jd_file is not None:

        prompt = f"Analyze this resume against the job description: \n\nJob Description:\n{jd_text}\n\nResume:\n{new_cv_text}\n\nProvide a percentage match and recommendations for improvement."

        # Sending the prompt to the OpenAI API
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt},
                {"role": "system", "content": "You are a helpful assistant."}
            ]
        )

        # Displaying the response in the Streamlit app
        st.write(response.choices[0].message.content)
    else:
        st.write("Please make sure both the job description and resume are entered before analyzing.")
















from openai import OpenAI

client = OpenAI(api_key="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")

# Example of a complex input prompt. In practice, you'd construct this based on user input or file content.
job_description = "Here's the job description..."
resume = "Here's the resume..."
prompt = f"Analyze this resume against the job description: \n\nJob Description:\n{job_description}\n\nResume:\n{resume}\n\nProvide a percentage match and recommendations for improvement."

while True:
    user_input = input("Enter 'analyze' to evaluate the resume or 'quit' to exit: ")
    if user_input.lower() == 'quit':
        break

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    )

    print(response.choices[0].message.content)
