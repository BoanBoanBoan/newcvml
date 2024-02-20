from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


def generate_golang_cv_template():
    name = "Alice Smith"
    contact = "alicesmith@email.com | (555) 123-4567"

    skills = ["Go", "Golang", "Concurrency", "HTTP", "JSON", "Database", "RESTful APIs", "Websockets",
        "Testing", "Modules", "Configuration", "Microservices", "Image Manipulation", "Templates",
        "Monitoring and Logging", "Docker", "Kubernetes", "Encryption", "Archives", "File System",
        "Networking", "Regular Expressions", "Exception Handling", "Command Line Development"]

    shuffled_skills = sample(skills, len(skills))

    if "Go" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "Go")

    additional_skills = shuffled_skills[1:9]
    additional_skills_str = ",\n".join(additional_skills)
    additional_skills_str_formatted = additional_skills_str.replace('\n', '\n    ')

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    Go,
    {additional_skills_str_formatted}

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
