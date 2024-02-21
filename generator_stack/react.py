from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import qa_skills


def generate_frontend_react_cv_template():
    name = "Olivia Brown"
    contact = "oliviabrown@email.com | (555) 789-1234"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    React, 
    {qa_skills()}

    Work Experience:
    - Frontend Developer, Company XYZ, 2017-present
    - Web Developer, Company ABC, 2014-2017

    Projects:
    - Developed user interfaces using React.js for modern web applications.
    - Implemented responsive and cross-browser compatible designs.

    Certifications:
    - React Developer Certification

    References:
    Available upon request.
    """

    return template


def create_pdf(filename, content):
    c = canvas.Canvas(filename)
    c.setFont("Helvetica", 12)  # Adjust the font as needed

    # Split the content into lines and add them to the PDF
    lines = content.split('\n')
    y_position = 750
    for line in lines:
        c.drawString(20, y_position, line)
        y_position -= 12  # Adjust the line spacing as needed

    c.save()


def generate_pdfs():
    output_folder = "frontend_react_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_frontend_react_cv_template()
        pdf_filename = os.path.join(output_folder, f"Frontend_React_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
