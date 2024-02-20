from reportlab.pdfgen import canvas
import os
from random import sample, choice


def generate_frontend_react_cv_template():
    name = "Olivia Brown"
    contact = "oliviabrown@email.com | (555) 789-1234"

    skills = ["React", "React Native", "JavaScript", "JSX", "Component-Based Architecture",
              "State Management (Redux, MobX)", "Hooks", "Functional Components", "Class Components", "Virtual DOM",
              "React Router", "Redux Thunk", "Redux Saga", "Context API", "Styled Components", "Material-UI",
              "Bootstrap", "CSS Modules", "CSS-in-JS", "Responsive Design", "RESTful APIs", "GraphQL", "Axios",
              "Fetch API", "Form Handling (Formik, React Hook Form)", "Server-Side Rendering (SSR)",
              "Next.js", "Gatsby", "React Testing Library", "Jest", "Enzyme", "Storybook",  "Git", "SVN",
              "Agile Methodologies", "Scrum", "Kanban", "CI/CD", "Docker", "AWS Amplify", "Firebase",
              "Authentication and Authorization", "OAuth 2.0", "JSON Web Tokens (JWT)", "Progressive Web Apps (PWAs)",
              "Single Page Applications (SPAs)", "Error Handling", "Debugging", "Performance Optimization",
              "Code Splitting", "Internationalization (i18n)", "Unit Testing", "Integration Testing",
              "End-to-End Testing (E2E)", "Cross-Browser Compatibility", "Web Accessibility (a11y)",
              "SEO Best Practices"]

    shuffled_skills = sample(skills, len(skills))

    if "React" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "React")

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
    React, 
    {additional_skills_str_formatted}

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
