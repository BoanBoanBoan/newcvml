from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_senior_specialist_cv_template():
    # Generate a CV template for a senior specialist with 5 years+ experience
    name = "Alice Senior"
    birth_date = "March 10, 1980"
    contact = "alicesenior@email.com | (555) 123-4567"

    # Add more skills as needed for senior specialists
    skills = ["Expert in Python", "Web Development", "Data Science", "Team Leadership", "Project Management"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 1998-2002
    - Master of Science in Software Engineering, University ABC, 2003-2005

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Senior Python Developer, Company XYZ, 2005-present
    - Lead Software Engineer, Company ABC, 2002-2005

    Projects:
    - Led development teams for high-impact projects.
    - Implemented advanced solutions in Python for complex challenges.

    Certifications:
    - Certified Senior Python Developer

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
    output_folder = "senior_specialist_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_senior_specialist_cv_template()
        pdf_filename = os.path.join(output_folder, f"Senior_Specialist_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
