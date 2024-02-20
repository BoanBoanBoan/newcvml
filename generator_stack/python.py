from reportlab.pdfgen import canvas
import os
from random import sample, choice
from education_info import education_prog_or_not


def generate_python_cv_template():
    name = "Bob Johnson"
    contact = "bobjohnson@email.com | (555) 987-6543"

    skills = ["Python", "Object-Oriented Programming", "Functional Programming",
              "NumPy", "Pandas", "Matplotlib", "Seaborn", "Scikit-learn", "TensorFlow", "Keras", "PyTorch",
              "NLTK (Natural Language Toolkit)", "SpaCy", "Gensim", "Django", "Flask", "FastAPI", "SQLAlchemy",
              "MySQL", "PostgreSQL", "SQLite", "MongoDB", "Redis", "Celery", "Asyncio", "RESTful APIs", "GraphQL",
              "Beautiful Soup", "Scrapy", "Tkinter", "PyQt", "PyQt5", "PyGTK", "unittest", "pytest", "Selenium",
              "CI/CD ", "Docker", "Kubernetes", "AWS", "Azure", "GCP", "Microservices", "Concurrency and Parallelism",
              "Multiprocessing", "Threading", "Asynchronous Programming", "Socket Programming", "Networking",
              "Regular Expressions", "Data Analysis", "Data Visualization", "Machine Learning", "Deep Learning",
              "Natural Language Processing (NLP)",  "Computer Vision", "Web", "Agile Methodologies", "Scrum", "Kanban",
              "Git", "SVN", "GitHub", "GitLab", "Bitbucket"]

    shuffled_skills = sample(skills, len(skills))

    if "Python" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "Python")

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
    Python, 
    {additional_skills_str_formatted}

    Work Experience:
    - Python Developer, Company XYZ, 2010-present
    - Software Engineer, Company ABC, 2007-2010

    Projects:
    - Developed web applications using Django and Flask.
    - Implemented data analysis solutions using Python.

    Certifications:
    - Certified Python Developer

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
    output_folder = "python_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_python_cv_template()
        pdf_filename = os.path.join(output_folder, f"Python_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
