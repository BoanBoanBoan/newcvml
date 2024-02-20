from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_java_cv_template():
    # Generate a simple Java CV template with some variability
    name = "John Doe"
    birth_date = "January 1, 1990"
    contact = "johndoe@email.com | (123) 456-7890"

    # Add more skills as needed
    skills = ["Java", "Object-Oriented Programming", "Spring Framework", "Database Management", "Problem Solving"]
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
    - Master of Science in Software Engineering, University ABC, 2017-2019

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Java Developer, Company XYZ, 2019-present
    - Software Engineer, Company ABC, 2016-2019

    Projects:
    - Developed a scalable web application using Spring Boot.
    - Implemented database optimizations for improved performance.

    Certifications:
    - Oracle Certified Professional, Java SE 8 Programmer

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
    output_folder = "java_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_java_cv_template()
        pdf_filename = os.path.join(output_folder, f"Java_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
