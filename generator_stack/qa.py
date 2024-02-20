from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


def generate_qa_cv_template():
    name = "Alice Williams"
    contact = "alicewilliams@email.com | (555) 123-9876"

    skills = [ "Software Testing", "Test Planning", "Test Case Design", "Test Execution",
               "Defect Reporting and Tracking", "Manual Testing", "Automated Testing", "Selenium WebDriver", "TestNG",
               "JUnit", "Cucumber", "Behavior-Driven Development (BDD)", "Gherkin Syntax", "API Testing", "Postman",
               "REST Assured", "Load Testing", "Performance Testing", "JMeter", "Gatling", "Security Testing",
               "OWASP ZAP", "Burp Suite", "Mobile Testing", "Appium", "Test Automation Frameworks",
               "Keyword-Driven Testing", "Data-Driven Testing", "Page Object Model (POM)", "TestNG Annotations",
               "Continuous Integration/Continuous Deployment (CI/CD)", "Jenkins", "Git", "GitHub", "GitLab",
               "Version Control Systems", "Agile Methodologies", "Scrum", "Kanban", "Defect Management Tools",
               "JIRA", "Bugzilla", "Test Management Tools", "TestRail", "Zephyr", "HP ALM", "Test Documentation",
               "Test Plans", "Test Cases", "Test Scripts", "Test Reports", "Regression Testing",
               "User Acceptance Testing (UAT)", "Exploratory Testing", "Cross-Browser Testing",
               "Cross-Platform Testing", "Localization Testing", "Internationalization Testing",
               "Accessibility Testing", "Usability Testing", "Smoke Testing", "Sanity Testing", "White Box Testing",
               "Black Box Testing", "Gray Box Testing", "QA"
]
    shuffled_skills = sample(skills, len(skills))

    if "QA" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "QA")

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
    QA, 
    {additional_skills_str_formatted}

    Work Experience:
    - QA Engineer, Company XYZ, 2012-present
    - Software Tester, Company ABC, 2009-2012

    Projects:
    - Conducted manual testing for various software applications.
    - Developed and executed test plans and test cases.

    Certifications:
    - ISTQB Certified Tester

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
    output_folder = "qa_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_qa_cv_template()
        pdf_filename = os.path.join(output_folder, f"QA_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
