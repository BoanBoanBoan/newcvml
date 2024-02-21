from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import dotnet_skills


def generate_dotnet_cv_template():
    name = "Michael Johnson"
    contact = "michaeljohnson@email.com | (555) 789-1234"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    C#,
    {dotnet_skills()}

    Work Experience:
    - DevOps Engineer, Company XYZ, 2009-present
    - System Administrator, Company ABC, 2006-2009

    Projects:
    - Implemented CI/CD pipelines for automated software delivery.
    - Managed infrastructure using configuration management tools.

    Certifications:
    - AWS Certified DevOps Engineer - Professional

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
    output_folder = "dotnet_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_dotnet_cv_template()
        pdf_filename = os.path.join(output_folder, f"DotNet_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
