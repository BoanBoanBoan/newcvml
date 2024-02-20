from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


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

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

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
