# 🧮 Scientific Calculator CI/CD Pipeline 🚀

## 📌 Project Overview

This project demonstrates a complete **DevOps CI/CD pipeline** for a Python-based **Scientific Calculator** application.

The pipeline automates the process of:

✅ Building the application
✅ Running unit tests
✅ Creating a Docker container
✅ Pushing the image to Docker Hub
✅ Deploying the application using Ansible
✅ Sending build notifications via email

The goal of this project is to show how **DevOps tools automate the software development lifecycle**.

---

## 🛠️ Technologies Used

⚙️ **Python** – Application development
📂 **Git** – Version control
🌐 **GitHub** – Remote repository
🤖 **Jenkins** – CI/CD automation server
🐳 **Docker** – Containerization
📦 **Docker Hub** – Container registry
📡 **Ansible** – Automated deployment
🌍 **Ngrok** – Exposes local Jenkins server for GitHub webhooks

---

## 📂 Project Structure

```
scientific-calculator/

cal.py
test_calculator.py
Dockerfile
Jenkinsfile
deploy.yml
README.md
.gitignore
```

---

## 🧮 Application Features

The scientific calculator supports the following operations:

➕ Power calculation
√ Square root
📊 Natural logarithm
🔢 Factorial

Additional features:

✔ Input validation
✔ Error handling
✔ Logging support

---

## 🔄 CI/CD Pipeline Workflow

The CI/CD pipeline automates the following process:

1️⃣ Developer pushes code to **GitHub**
2️⃣ GitHub triggers **Jenkins pipeline using Webhook**
3️⃣ Jenkins executes multiple pipeline stages

### Jenkins Pipeline Stages

```
Install Dependencies
⬇
Run Unit Tests
⬇
Docker Login
⬇
Build Docker Image
⬇
Push Docker Image to Docker Hub
⬇
Deploy using Ansible
⬇
Send Email Notification
```

This automation ensures that **every code change is tested and deployed automatically**.

---

## 🐳 Docker Image

### 📦 Docker Hub Repository

https://hub.docker.com/r/kabubabu/scientific-calculator

### ⬇ Pull the Image

```
docker pull kabubabu/scientific-calculator:latest
```

### ▶ Run the Container

```
docker run -it kabubabu/scientific-calculator
```

---

## 🚀 Deployment Using Ansible

Deployment is automated using an **Ansible playbook**.

### ▶ Run Deployment

```
ansible-playbook -i inventory deploy.yml
```

### 🔧 The playbook performs:

1️⃣ Pull latest Docker image
2️⃣ Stop existing container (if running)
3️⃣ Run new container with updated image

This ensures the **latest version of the application is always deployed automatically**.

---

## 📧 Email Notification

Jenkins sends email notifications after pipeline execution.

Notifications include:

📩 Build Success
📩 Build Failure

This helps developers **monitor the pipeline status in real time**.

---

## 🖥️ Run Application Locally

### ▶ Run Calculator

```
python3 cal.py
```

### 🧪 Run Unit Tests

```
python3 -m unittest test_calculator.py
```

### 🐳 Build Docker Image

```
docker build -t kabubabu/scientific-calculator .
```

### ▶ Run Docker Container

```
docker run -it kabubabu/scientific-calculator
```

---

## 🔗 Project Links

🌐 **GitHub Repository**

https://github.com/Coder-Galaxy/scientific-calculator

🐳 **Docker Hub Repository**

https://hub.docker.com/r/kabubabu/scientific-calculator

---

## 📊 CI/CD Architecture

```
Developer
⬇
GitHub Repository
⬇
Jenkins Pipeline
⬇
Build Docker Image
⬇
Push to Docker Hub
⬇
Deploy using Ansible
⬇
Run Docker Container
```

---

## ✅ Conclusion

This project successfully demonstrates how a **complete CI/CD pipeline** can automate the software delivery process.

By integrating **GitHub, Jenkins, Docker, Docker Hub, and Ansible**, the entire workflow from **code commit to deployment** is automated.

This approach improves:

⚡ Development speed
🔒 Reliability
🚀 Deployment efficiency

---

## ⭐ Author

👨‍💻 **Piyush Singh**
DevOps Mini Project



