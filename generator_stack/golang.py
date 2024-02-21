from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import golang_skills


def generate_golang_cv_template():
    name = "Alice Smith"
    contact = "alicesmith@email.com | (555) 123-4567"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    Go,
    {golang_skills()}

    Work Experience:
    - Golang Developer, Company XYZ, 2013-present
    - Software Engineer, Company ABC, 2010-2013

    Projects:
    - Developed scalable backend services using Go and microservices architecture.
    - Implemented efficient data processing pipelines.

    Certifications:
    - Google Certified Professional - Associate Cloud Engineer

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
    output_folder = "golang_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_golang_cv_template()
        pdf_filename = os.path.join(output_folder, f"Golang_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
