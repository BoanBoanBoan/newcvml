from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_devops_cv_template():
    # Generate a simple DevOps CV template with some variability
    name = "Michael Johnson"
    birth_date = "April 25, 1984"
    contact = "michaeljohnson@email.com | (555) 789-1234"

    # Add more skills as needed
    skills = ["Continuous Integration", "Containerization (Docker)", "Configuration Management (Ansible)",
              "Cloud Services (AWS, Azure)", "Monitoring and Logging"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Engineering, University XYZ, 2002-2006
    - Master of Science in DevOps Engineering, University ABC, 2007-2009

    Skills:
    {", ".join(skills)}

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
    output_folder = "devops_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_devops_cv_template()
        pdf_filename = os.path.join(output_folder, f"DevOps_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
