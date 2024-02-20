from reportlab.pdfgen import canvas
import os
from random import sample, choice


def generate_java_cv_template():
    name = "John Doe"
    contact = "johndoe@email.com | (123) 456-7890"

    skills = ["Java", "Object-Oriented Programming", "Java Virtual Machine (JVM)", "Java Development Kit (JDK)",
              "Java Standard Edition (Java SE)", "Java Enterprise Edition (Java EE)", "Spring Framework", "Spring Boot",
              "Hibernate", "JPA (Java Persistence API)", "Servlets", "JSP (JavaServer Pages)", "JavaFX", "Swing",
              "Maven", "Gradle", "JUnit", "TestNG", "Mockito", "RESTful Web Services", "SOAP Web Services",
              "Microservices", "Spring Security", "JWT (JSON Web Tokens)", "Authentication and Authorization",
              "JDBC (Java Database Connectivity)", "SQL", "NoSQL Databases", "JMS (Java Message Service)", "JAX-RS",
              "JAX-WS", "XML Processing (DOM, SAX, JAXB)", "JSON Processing (Jackson, Gson)", "Design Patterns",
              "Concurrency", "Multithreading", "Networking", "Socket Programming", "Swing GUI Development",
              "JavaFX GUI Development", "Logging (SLF4J, Log4j)", "Dependency Injection",
              "Aspect-Oriented Programming (AOP)", "Java EE Containers (Tomcat, Jetty, WildFly, GlassFish)",
              "Build Automation", "Continuous Integration (Jenkins, Bamboo)", "Containerization (Docker)",
              "Cloud Platforms (AWS, Azure, Google Cloud)", "Monitoring and Performance Tuning",
              "Security Best Practices", "Unit Testing", "Integration Testing",
              "Code Quality Tools (SonarQube, PMD, FindBugs)", "Version Control Systems (Git, SVN)",
              "Agile Methodologies (Scrum, Kanban)"]

    shuffled_skills = sample(skills, len(skills))

    if "Java" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "Java")

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
    Java, 
    {additional_skills_str_formatted}

    Work Experience:
    - Java Developer, Company XYZ, 2019-present
    - Software Engineer, Company ABC, 2016-2019

    Projects:
    - Developed a scalable web application using Spring Boot.
    - Implemented database optimizations for improved performance.

    Certifications:
    - Oracle Certified Professional, Java SE 8 Programmer

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
    output_folder = "java_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_java_cv_template()
        pdf_filename = os.path.join(output_folder, f"Java_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
