from reportlab.pdfgen import canvas
import os
from random import shuffle


def generate_dotnet_cv_template():
    # Generate a simple .NET CV template with some variability
    name = "Jane Doe"
    birth_date = "February 2, 1995"
    contact = "janedoe@email.com | (987) 654-3210"

    # Add more skills as needed
    skills = [".NET Framework", "C#", "ASP.NET", "MVC", "Entity Framework"]
    shuffle(skills)  # Shuffle the skills for variability

    # Rest of the template
    template = f"""
    Curriculum Vitae

    Personal Information:
    Name: {name}
    Date of Birth: {birth_date}
    Contact: {contact}

    Education:
    - Bachelor of Science in Computer Science, University XYZ, 2013-2017
    - Master of Science in Software Engineering, University ABC, 2018-2020

    Skills:
    {", ".join(skills)}

    Work Experience:
    - .NET Developer, Company XYZ, 2020-present
    - Software Engineer, Company ABC, 2017-2020

    Projects:
    - Developed web applications using ASP.NET MVC.
    - Implemented data access layer using Entity Framework.

    Certifications:
    - Microsoft Certified: Azure Developer Associate

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
    output_folder = "dotnet_dev_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_dotnet_cv_template()
        pdf_filename = os.path.join(output_folder, f"DotNet_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
