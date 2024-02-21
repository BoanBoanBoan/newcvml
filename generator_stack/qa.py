from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import qa_skills


def generate_qa_cv_template():
    name = "Alice Williams"
    contact = "alicewilliams@email.com | (555) 123-9876"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
   {education_prog_or_not()}

    Skills:
    QA, 
    {qa_skills()}

    Work Experience:
    - QA Engineer, Company XYZ, 2012-present
    - Software Tester, Company ABC, 2009-2012

    Projects:
    - Conducted manual testing for various software applications.
    - Developed and executed test plans and test cases.

    Certifications:
    - ISTQB Certified Tester

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
    output_folder = "qa_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_qa_cv_template()
        pdf_filename = os.path.join(output_folder, f"QA_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
