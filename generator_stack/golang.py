from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_golang_cv_template():
    # Generate a simple Go CV template with some variability
    name = "Alice Smith"
    birth_date = "March 5, 1988"
    contact = "alicesmith@email.com | (555) 123-4567"

    # Add more skills as needed
    skills = ["Go", "Concurrency", "RESTful APIs", "Databases", "Testing"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2006-2010
    - Master of Science in Software Engineering, University ABC, 2011-2013

    Skills:
    {", ".join(skills)}

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
