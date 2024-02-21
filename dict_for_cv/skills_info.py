from random import sample


def business_analytics_skills():
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
    additional_business_analytics_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_business_analytics_skills


def devops_skills():
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
    additional_devops_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_devops_skills


def dotnet_skills():
    skills = ["C#", "C# Programming", ".NET Framework", "ASP.NET", "ASP.NET Core", "MVC", "Web API",
    "Entity Framework", "LINQ", "SQL Server", "RESTful API Design", "Unit Testing", "Dependency Injection",
    "Software Design Patterns", "Git", "Agile Methodologies", "Continuous Integration", "Containerization (Docker)",
    "Configuration Management (Ansible)", "Cloud Services (AWS, Azure)", "Monitoring and Logging"]

    shuffled_skills = sample(skills, len(skills))
    if "C#" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "C#")

    additional_skills = shuffled_skills[1:9]
    additional_skills_str = ",\n".join(additional_skills)
    additional_dotnet_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_dotnet_skills


def golang_skills():
    skills = ["Go", "Golang", "Concurrency", "HTTP", "JSON", "Database", "RESTful APIs", "Websockets",
        "Testing", "Modules", "Configuration", "Microservices", "Image Manipulation", "Templates",
        "Monitoring and Logging", "Docker", "Kubernetes", "Encryption", "Archives", "File System",
        "Networking", "Regular Expressions", "Exception Handling", "Command Line Development"]

    shuffled_skills = sample(skills, len(skills))

    if "Go" not in shuffled_skills:
        shuffled_skills.pop()
        shuffled_skills.insert(0, "Go")

    additional_skills = shuffled_skills[1:9]
    additional_skills_str = ",\n".join(additional_skills)
    additional_golang_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_golang_skills


def java_skills():
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
    additional_java_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_java_skills


def python_skills():
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
    additional_python_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_python_skills


def qa_skills():
    skills = ["Software Testing", "Test Planning", "Test Case Design", "Test Execution",
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
    additional_qa_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_qa_skills


def react_skills():
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
    additional_react_skills = additional_skills_str.replace('\n', '\n    ')

    return additional_react_skills