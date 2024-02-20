from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_frontend_react_cv_template():
    # Generate a simple Frontend React Developer CV template with some variability
    name = "Olivia Brown"
    birth_date = "November 18, 1992"
    contact = "oliviabrown@email.com | (555) 789-1234"

    # Add more skills as needed
    skills = ["React.js", "JavaScript", "HTML5", "CSS3", "Responsive Web Design"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2010-2014
    - Master of Science in Web Development, University ABC, 2015-2017

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Frontend Developer, Company XYZ, 2017-present
    - Web Developer, Company ABC, 2014-2017

    Projects:
    - Developed user interfaces using React.js for modern web applications.
    - Implemented responsive and cross-browser compatible designs.

    Certifications:
    - React Developer Certification

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
    output_folder = "frontend_react_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_frontend_react_cv_template()
        pdf_filename = os.path.join(output_folder, f"Frontend_React_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
