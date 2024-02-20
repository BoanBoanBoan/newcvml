from reportlab.pdfgen import canvas
import os
from random import sample
from education_info import education_prog_or_not


def generate_devops_cv_template():
    name = "Michael Johnson"
    contact = "michaeljohnson@email.com | (555) 789-1234"

    skills = ["Linux/Unix Administration", "Shell Scripting", "Networking Concepts",
              "VMware", "VirtualBox", "Hyper-V", "Docker", "Kubernetes", "Ansible", "Chef", "Puppet", "Terraform",
              "AWS CloudFormation", "CI/CD", "Git", "SVN", "Prometheus", "Grafana", "ELK Stack", "Splunk", "Logstash",
              "AWS", "Azure", "Google Cloud Platform", "Kubernetes", "Docker Swarm", "Nomad", "Jenkins", "CircleCI",
              "Travis CI", "Firewalls", "VPNs", "Encryption", "Python", "Bash", "PowerShell", "MySQL", "PostgreSQL",
              "MongoDB", "Nginx", "HAProxy", "Scrum", "Kanban"]

    shuffled_skills = sample(skills, len(skills))
    if "CI/CD" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "CI/CD")

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
    CI/CD,
    {additional_skills_str_formatted}

    Work Experience:
    - DevOps Engineer, Company XYZ, 2009-present
    - System Administrator, Company ABC, 2006-2009

    Projects:
    - Implemented CI/CD pipelines for automated software delivery.
    - Managed infrastructure using configuration management tools.

    Certifications:
    - AWS Certified DevOps Engineer - Professional

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
    output_folder = "devops_pdfs"
    os.makedirs(output_folder, exist_ok=True)

    for i in range(1, 1001):
        cv_template = generate_devops_cv_template()
        pdf_filename = os.path.join(output_folder, f"DevOps_CV_{i}.pdf")
        create_pdf(pdf_filename, cv_template)


if __name__ == "__main__":
    generate_pdfs()
