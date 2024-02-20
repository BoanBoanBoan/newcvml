from reportlab.pdfgen import canvas
import os
from random import sample, choice


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

    bachelor_non_programming = [
        "Bachelor of Arts in Psychology, Harvard University, USA, 2012-2016",
        "Bachelor of Science in Economics, London School of Economics and Political Science, UK, 2013-2017",
        "Bachelor of Business Administration, University of Melbourne, Australia, 2014-2018",
        "Bachelor of Laws, Université Paris 1 Panthéon-Sorbonne, France, 2015-2019",
        "Bachelor of Medicine, University of Toronto, Canada, 2016-2020",
        "Bachelor of Education, University of Cape Town, South Africa, 2017-2021",
        "Bachelor of Architecture, Technical University of Munich, Germany, 2018-2022",
        "Bachelor of Fine Arts, Tokyo University of the Arts, Japan, 2019-2023",
        "Bachelor of Social Work, University of São Paulo, Brazil, 2020-2024",
        "Bachelor of Science in Nursing, University of Auckland, New Zealand, 2021-2025"
    ]

    bachelor_programming = [
        "Bachelor of Science in Computer Science, Massachusetts Institute of Technology, USA, 2012-2016",
        "Bachelor of Engineering in Software Engineering, University of Cambridge, UK, 2013-2017",
        "Bachelor of Technology in Computer Engineering, University of New South Wales, Australia, 2014-2018",
        "Bachelor of Computer Science and Engineering, ETH Zurich, Switzerland, 2015-2019",
        "Bachelor of Science in Information Technology, University of Waterloo, Canada, 2016-2020",
        "Bachelor of Science in Computer Engineering, National University of Singapore, Singapore, 2017-2021",
        "Bachelor of Computer Applications, Indian Institute of Technology Bombay, India, 2018-2022",
        "Bachelor of Software Engineering, University of Auckland, New Zealand, 2019-2023",
        "Bachelor of Information Technology, Technical University of Munich, Germany, 2020-2024",
        "Bachelor of Computer Science, University of São Paulo, Brazil, 2021-2025"
    ]

    master_non_programming = [
        "Master of Business Administration, Harvard Business School, USA, 2012-2014",
        "Master of Laws, University of Oxford, UK, 2013-2015",
        "Master of International Business, HEC Paris, France, 2014-2016",
        "Master of Science in Finance, London School of Economics and Political Science, UK, 2015-2017",
        "Master of Public Health, University of Melbourne, Australia, 2016-2018",
        "Master of Arts in Education, University of British Columbia, Canada, 2017-2019",
        "Master of Architecture, ETH Zurich, Switzerland, 2018-2020",
        "Master of Fine Arts, Tokyo University of the Arts, Japan, 2019-2021",
        "Master of Social Work, University of São Paulo, Brazil, 2020-2022",
        "Master of Health Administration, University of Auckland, New Zealand, 2021-2023"
    ]

    master_programming = [
        "Master of Science in Computer Science, Stanford University, USA, 2012-2014",
        "Master of Engineering in Software Engineering, University College London, UK, 2013-2015",
        "Master of Technology in Computer Engineering, University of Sydney, Australia, 2014-2016",
        "Master of Computer Science and Engineering, EPFL, Switzerland, 2015-2017",
        "Master of Science in Information Technology, University of Toronto, Canada, 2016-2018",
        "Master of Science in Computer Engineering, Nanyang Technological University, Singapore, 2017-2019",
        "Master of Computer Applications, Indian Institute of Technology Delhi, India, 2018-2020",
        "Master of Software Engineering, University of Auckland, New Zealand, 2019-2021",
        "Master of Information Technology, Technical University of Munich, Germany, 2020-2022",
        "Master of Computer Science, University of São Paulo, Brazil, 2021-2023"
    ]

    bachelor_degree = choice([bachelor_non_programming, bachelor_programming])
    master_degree = choice([master_non_programming, master_programming])
    education = choice(bachelor_degree) + "\n" + "    " + choice(master_degree)

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
   {education}

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
