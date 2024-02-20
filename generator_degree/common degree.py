from reportlab.pdfgen import canvas
import os
from random import shuffle, choice


def generate_common_master_degree_specialist_cv_template():
    # Generate a CV template for a specialist with a master's degree in a common non-computer field
    name = "Jessica Professional"
    birth_date = "April 25, 1987"
    contact = "jessicaprofessional@email.com | (555) 567-8901"

    # Add more skills as needed for specialists with a master's degree in another field
    skills = ["Research", "Project Management", "Data Analysis", "Communication", "Team Leadership"]
    shuffle(skills)  # Shuffle the skills for variability

    # List of possible degree fields
    possible_degree_fields = [
        "Business Administration",
        "Public Administration",
        "Marketing",
        "Finance",
        "Human Resources",
        "Economics",
        "International Relations",
        # Add more degree fields as needed
    ]

    # Shuffle the degree fields for variability
    shuffle(possible_degree_fields)

    # Select a degree field for the current CV
    degree_field = choice(possible_degree_fields)

    # Add certifications related to the degree field
    certifications = "Project Management Professional (PMP)"

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of [Common Field], University XYZ, 2005-2009
    - Master of {degree_field}, Important University ABC, 2010-2012

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Senior Specialist, Company XYZ, 2012-present
    - Project Manager, Organization ABC, 2009-2012

    Projects:
    - Led and managed various projects in {degree_field}.
    - Conducted in-depth research and analysis.

    Certifications:
    - {certifications}

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
    output_folder = "common_master_degree_specialist_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_common_master_degree_specialist_cv_template()
        pdf_filename = os.path.join(output_folder, f"Common_Master_Degree_Specialist_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
