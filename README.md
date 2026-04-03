# 🚀 AI-Assisted DevOps Pipeline

A friendly **DevOps project** built from scratch using **Node.js, Docker, GitHub Actions, Terraform, and Python**.

This project demonstrates how modern DevOps workflows can be improved with an **AI-style troubleshooting layer** that helps analyze common CI/CD, Docker, and Terraform issues.

---

## 📌 Project Overview

This project includes:

- ✅ A simple Node.js web application
- ✅ Docker containerization
- ✅ GitHub Actions CI pipeline
- ✅ Terraform infrastructure practice
- ✅ AI-style log analysis for common DevOps issues

The goal is to show how **engineering expertise + intelligent tooling** can improve troubleshooting and infrastructure workflows.

---

## 🏗️ Architecture Flow

```text
Developer Push
   ↓
GitHub Actions CI
   ↓
Docker Build
   ↓
AI Log Analyzer
   ↓
Terraform IaC
```

---

## 🛠️ Tech Stack

- **Node.js** → sample application
- **Docker** → containerization
- **GitHub Actions** → CI pipeline
- **Terraform** → infrastructure as code
- **Python** → AI-style log analyzer
- **WSL + Ubuntu** → development environment

---

## 📂 Project Structure

```text
ai-devops-pipeline/
├── ai/
│   ├── log_analyzer.py
│   ├── sample.log
│   ├── ci_error.log
│   └── terraform_error.log
├── terraform/
│   ├── main.tf
│   └── example.txt
├── .github/
│   └── workflows/
│       ├── ci.yml
│       └── ai-log-check.yml
├── Dockerfile
├── index.js
├── package.json
├── .gitignore
└── README.md
```

---

## ▶️ Run the App Locally

Install dependencies:

```bash
npm install
```

Run the app:

```bash
node index.js
```

Visit:

```text
http://localhost:3000
```

---

## 🐳 Run with Docker

Build the image:

```bash
docker build -t ai-devops-app .
```

Run the container:

```bash
docker run -p 3000:3000 ai-devops-app
```

---

## ⚙️ CI Pipeline

The GitHub Actions CI workflow automatically:

- installs dependencies
- validates app startup
- builds the Docker image

Workflow file:

```text
.github/workflows/ci.yml
```

---

## 🤖 AI Log Analyzer

The Python log analyzer reviews sample CI/CD and Terraform errors and suggests likely fixes.

Example usage:

```bash
python3 ai/log_analyzer.py ai/ci_error.log
```

Example output:

```text
Possible Node.js dependency issue. Check package.json and run npm install.
```

Supported checks:

- Node.js dependency issues
- Docker build failures
- Terraform configuration errors
- Port conflicts

---

## 🌍 Terraform Practice

The Terraform module currently creates a local file resource to simulate infrastructure management.

Run:

```bash
cd terraform
terraform init
terraform plan
terraform apply
```

This validates Terraform setup before moving to cloud infrastructure.

---

## 🎯 Why This Project Matters

This project reflects a real-world DevOps mindset:

> combining reliable engineering workflows with intelligent analysis tools to accelerate debugging, infrastructure validation, and delivery confidence.

It demonstrates:

- CI/CD automation
- containerized deployment
- infrastructure as code
- AI-assisted troubleshooting
- DevOps workflow thinking

---

## 🚀 Future Improvements

Planned upgrades:

- AWS deployment with Terraform
- EC2 provisioning
- GitHub Actions deployment workflow
- real AI API integration
- monitoring with Prometheus/Grafana
- automated Terraform error detection in CI
