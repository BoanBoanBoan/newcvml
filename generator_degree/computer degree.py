from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_master_degree_specialist_cv_template():
    # Generate a CV template for a specialist with an important master's degree in computer science
    name = "David Expert"
    birth_date = "October 20, 1988"
    contact = "davidexpert@email.com | (555) 345-6789"

    # Add more skills as needed for specialists with a master's degree
    skills = ["Advanced Python Programming", "Machine Learning", "Data Analysis", "Research", "Team Collaboration"]
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
    - Master of Science in Computer Science, Important University ABC, 2011-2013

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Senior Python Developer, Company XYZ, 2013-present
    - Research Scientist, Research Institute ABC, 2010-2013

    Projects:
    - Led machine learning projects for predictive analytics.
    - Conducted advanced research in the field of computer science.

    Certifications:
    - Certified Expert in Python
    - Master's Degree in Computer Science

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
    output_folder = "master_degree_specialist_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_master_degree_specialist_cv_template()
        pdf_filename = os.path.join(output_folder, f"Master_Degree_Specialist_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
