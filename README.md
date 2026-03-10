# Scientific Calculator CI/CD Pipeline

## 📌 Project Overview

This project demonstrates a complete **DevOps CI/CD pipeline** for a Python-based Scientific Calculator application. The pipeline automates the process of building, testing, containerizing, publishing, and deploying the application using modern DevOps tools.

The objective of this project is to showcase how DevOps practices can improve software delivery by automating the entire development lifecycle.

---

## 🛠 Technologies Used

- **Python** – Application development
- **Git & GitHub** – Version control and source repository
- **Jenkins** – CI/CD automation server
- **Docker** – Containerization of the application
- **Docker Hub** – Container registry for storing images
- **Ansible** – Automated deployment
- **Ngrok** – Exposes local Jenkins server for webhook triggering

---

## 📂 Project Structure


scientific-calculator/
│
├── cal.py # Scientific calculator application
├── test_calculator.py # Unit tests for calculator functions
├── Dockerfile # Docker container configuration
├── Jenkinsfile # Jenkins CI/CD pipeline definition
├── deploy.yml # Ansible playbook for deployment
├── .gitignore # Ignore unnecessary files
└── README.md # Project documentation


---

## 🧮 Application Features

The scientific calculator supports the following operations:

- Square Root
- Factorial
- Natural Logarithm (ln)
- Power (x^y)

It also includes:

- Input validation
- Error handling
- Logging support

---

## 🔁 CI/CD Pipeline Workflow

The pipeline automates the following steps:

1. Developer pushes code to **GitHub**
2. GitHub triggers **Jenkins pipeline using Webhook**
3. Jenkins performs the following stages:


Install Dependencies
↓
Run Unit Tests
↓
Docker Login
↓
Build Docker Image
↓
Push Image to Docker Hub
↓
Deploy Container using Ansible
↓
Send Email Notification


---

## 🐳 Docker Image

Docker Hub Repository:


https://hub.docker.com/r/kabubabu/scientific-calculator


Pull the image manually:

```bash
docker pull kabubabu/scientific-calculator:latest

Run the container:

docker run -it kabubabu/scientific-calculator
🚀 Deployment Using Ansible

Deployment is automated using the Ansible playbook:

ansible-playbook -i inventory deploy.yml

The playbook performs:

Pull latest Docker image

Stop existing container

Run updated container

📧 Email Notification

Jenkins sends email notifications after pipeline execution:

Build Success

Build Failure

This helps developers monitor pipeline status.

⚙️ How to Run Locally
Run the Calculator
python3 cal.py
Run Unit Tests
python3 -m unittest test_calculator.py
Build Docker Image
docker build -t kabubabu/scientific-calculator .
Run Docker Container
docker run -it kabubabu/scientific-calculator
🔗 Project Links

GitHub Repository:

https://github.com/Coder-Galaxy/scientific-calculator

Docker Hub Repository:

https://hub.docker.com/r/kabubabu/scientific-calculator
📊 CI/CD Architecture

Developer
↓
GitHub Repository
↓
Jenkins Pipeline
↓
Docker Image Build
↓
Docker Hub Registry
↓
Ansible Deployment
↓
Running Container

✅ Conclusion

This project successfully demonstrates the implementation of a complete DevOps CI/CD pipeline for a Python application. By integrating GitHub, Jenkins, Docker, Docker Hub, and Ansible, the entire workflow from code commit to deployment is automated.

This approach improves development speed, reliability, and deployment efficiency.


---
