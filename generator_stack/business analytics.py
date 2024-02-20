from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_business_analytics_cv_template():
    # Generate a simple Business Analytics CV template with some variability
    name = "Eva Miller"
    birth_date = "October 12, 1989"
    contact = "evamiller@email.com | (555) 456-7890"

    # Add more skills as needed
    skills = ["Data Analysis", "Statistical Modeling", "Business Intelligence", "Data Visualization",
              "Predictive Analytics"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Business Administration, University XYZ, 2007-2011
    - Master of Science in Business Analytics, University ABC, 2012-2014

    Skills:
    {", ".join(skills)}

    Work Experience:
    - Business Analyst, Company XYZ, 2014-present
    - Data Analyst, Company ABC, 2011-2014

    Projects:
    - Conducted data analysis to drive business decisions.
    - Developed predictive models for sales forecasting.

    Certifications:
    - Certified Business Analytics Professional (CBAP)

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
    output_folder = "business_analytics_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_business_analytics_cv_template()
        pdf_filename = os.path.join(output_folder, f"Business_Analytics_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
