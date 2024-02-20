from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


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

    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Contact: {contact}

    Education:
    {education_prog_or_not()}

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
