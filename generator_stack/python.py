from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_python_cv_template():
    # Generate a simple Python CV template with some variability
    name = "Bob Johnson"
    birth_date = "June 15, 1985"
    contact = "bobjohnson@email.com | (555) 987-6543"

    # Add more skills as needed
    skills = ["Python", "Django", "Flask", "Data Analysis", "Machine Learning"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2003-2007
    - Master of Science in Software Engineering, University ABC, 2008-2010

    Skills:
    {", ".join(skills)}

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
