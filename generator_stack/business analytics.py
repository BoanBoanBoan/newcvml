from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


def generate_business_analytics_cv_template():
    name = "Eva Miller"
    contact = "evamiller@email.com | (555) 456-7890"

    skills = ["Microsoft Power BI", "Data Analysis", "Statistical Modeling", "Business Intelligence",
              "Data Visualization", "Predictive Analytics", "Microsoft Excel", "Tableau", "QlikView",
              "SAS", "Statistical Analysis System", "Python", "Pandas", "NumPy", "Matplotlib", "R", "dplyr",
              "ggplot2", "tidyr", "Google Analytics", "SAP BusinessObjects", "IBM Cognos Analytics",
              "SQL", "Database Management", "Machine Learning", "Data Mining", "ETL (Extract, Transform, Load)",
              "Data Warehousing", "Data Cleaning", "Data Governance", "Hadoop", "Spark", "Big Data Analytics",
              "Natural Language Processing (NLP)", "Time Series Analysis", "Regression Analysis", "Decision Trees",
              "Cluster Analysis", "A/B Testing", "Financial Modeling", "Risk Analysis", "Market Research",
              "Customer Segmentation", "Dashboard Design", "Report Automation", "KPI Tracking",
              "Storytelling with Data"]

    shuffled_skills = sample(skills, len(skills))

    if "Microsoft Power BI" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "Microsoft Power BI")

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
    Microsoft Power BI, 
    {additional_skills_str_formatted}
    

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
