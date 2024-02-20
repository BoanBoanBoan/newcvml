from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_middle_specialist_cv_template():
    # Generate a CV template for a middle specialist with 2-3 years experience
    name = "Charlie Middle"
    birth_date = "September 5, 1995"
    contact = "charliemiddle@email.com | (555) 234-5678"

    # Add more skills as needed for middle specialists
    skills = ["Python Development", "Web Technologies", "Database Management", "Problem Solving", "Collaboration"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2012-2016

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Middle Python Developer, Company XYZ, 2016-present
    - Junior Software Engineer, Company ABC, 2014-2016

    Projects:
    - Contributed to the development of web applications using Python.
    - Assisted in database management tasks.

    Certifications:
    - Python Developer Certification

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
    output_folder = "middle_specialist_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_middle_specialist_cv_template()
        pdf_filename = os.path.join(output_folder, f"Middle_Specialist_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
