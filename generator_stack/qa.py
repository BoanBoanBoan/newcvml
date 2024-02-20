from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_qa_cv_template():
    # Generate a simple QA CV template with some variability
    name = "Alice Williams"
    birth_date = "September 10, 1987"
    contact = "alicewilliams@email.com | (555) 123-9876"

    # Add more skills as needed
    skills = ["Manual Testing", "Test Planning", "Defect Tracking", "Test Case Design", "Regression Testing"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2005-2009
    - Master of Science in Software Quality Assurance, University ABC, 2010-2012

    Skills:
    {", ".join(skills)}

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
