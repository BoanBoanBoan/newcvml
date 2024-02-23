from flask import Flask, request, render_template
import os
import openai
from PyPDF2 import PdfReader
from openai import OpenAI
from werkzeug.utils import secure_filename

from congig import api_key

client = OpenAI(api_key=api_key)

app = Flask(__name__)


def extract_text_from_pdf(pdf_path):
    text = ''
    with open(pdf_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        for page in pdf_reader.pages:
            text += page.extract_text() or ''  # Adding fallback for pages without text
    return text


def analyze_resume_with_job_description(cv_text, jd_text):
    prompt = f"Analyze this resume against the job description: \n\nJob Description:\n{jd_text}\n\nResume:\n{cv_text}\n\nProvide a percentage match and recommendations for improvement."

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": prompt},
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    )

    return response.choices[0].message.content


@app.route('/upload', methods=['POST'])
def upload_files():
    if request.method == 'POST':
        cv_file = request.files['cv']
        jd_file = request.files['jd']

        cv_path = os.path.join('uploads', secure_filename(cv_file.filename))
        jd_path = os.path.join('uploads', secure_filename(jd_file.filename))

        cv_file.save(cv_path)
        jd_file.save(jd_path)

        cv_text = extract_text_from_pdf(cv_path)
        jd_text = extract_text_from_pdf(jd_path)

        cv_text_clean = ' '.join(cv_text.split())
        jd_text_clean = ' '.join(jd_text.split())

        analysis_result = analyze_resume_with_job_description(cv_text_clean, jd_text_clean)

        return analysis_result

if __name__ == '__main__':
    app.run(debug=True)