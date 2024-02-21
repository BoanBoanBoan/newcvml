from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import java_skills


def generate_java_cv_template():
    name = "John Doe"
    contact = "johndoe@email.com | (123) 456-7890"



    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    Java, 
    {java_skills()}

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
