from reportlab.pdfgen import canvas
import os
from dict_for_cv.education_info import education_prog_or_not
from dict_for_cv.skills_info import business_analytics_skills


def generate_business_analytics_cv_template():
    name = "Eva Miller"
    contact = "evamiller@email.com | (555) 456-7890"

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

    Skills:
    Microsoft Power BI, 
    {business_analytics_skills()}
    

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
