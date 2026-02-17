# Scientific Calculator - DevOps Mini Project

## 📌 Project Overview

This project demonstrates a complete CI/CD pipeline for a Python-based Scientific Calculator application using:

- GitHub (Version Control)
- Jenkins (Continuous Integration)
- Docker (Containerization)
- Docker Hub (Image Registry)
- Ansible (Deployment Automation)

The goal of this project is to automate the process of building, testing, containerizing, and deploying the application.

---

## 🛠 Technologies Used

- Python 3
- Jenkins
- Docker
- Docker Hub
- Ansible
- Git & GitHub

---

## 📂 Project Structure
.
├── cal.py
├── test_calculator.py
├── Dockerfile
├── Jenkinsfile
├── deploy.yml
├── inventory
├── requirements.txt
└── README.md


---

## 🔁 CI/CD Pipeline Flow

1. Developer pushes code to GitHub.
2. Jenkins automatically:
   - Installs dependencies
   - Runs unit tests
   - Logs into Docker Hub
   - Builds Docker image
   - Pushes image to Docker Hub
3. Ansible:
   - Pulls latest image
   - Stops old container
   - Runs new container

---

## 🐳 Docker Image

Docker Hub Repository:

kabubabu/scientific-calculator


The image is tagged as:



latest


---

## 🚀 How To Run Manually

### Run Application Locally



python3 cal.py


### Run Unit Tests

python3 -m unittest test_calculator.py


### Build Docker Image

docker build -t kabubabu/scientific-calculator .


### Run Docker Container

docker run -it kabubabu/scientific-calculator


### Deploy Using Ansible

ansible-playbook -i inventory deploy.yml


---

## 🧠 Architecture

Developer
↓
GitHub
↓
Jenkins (CI)
↓
Docker Hub
↓
Ansible
↓
Running Container


---

## ✅ Features Implemented

- Scientific calculator functionality
- Logging support
- Unit testing
- Automated CI pipeline
- Docker image creation
- Secure credential handling
- Automated deployment using Ansible

---

## 📊 Conclusion

This project successfully demonstrates a full DevOps lifecycle implementation, including CI/CD automation from development to deployment.