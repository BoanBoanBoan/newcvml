from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import python_skills


def generate_python_cv_template():
    name = "Bob Johnson"
    contact = "bobjohnson@email.com | (555) 987-6543"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    Python, 
    {python_skills()}

    Work Experience:
    - Python Developer, Company XYZ, 2010-present
    - Software Engineer, Company ABC, 2007-2010

    Projects:
    - Developed web applications using Django and Flask.
    - Implemented data analysis solutions using Python.

    Certifications:
    - Certified Python Developer

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
    output_folder = "python_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_python_cv_template()
        pdf_filename = os.path.join(output_folder, f"Python_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
