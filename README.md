# CI/CD Pipeline with Security Scanning

![CI/CD Status](https://github.com/JoeMachiato/First-CI-CD-Pipeline/actions/workflows/cicd.yml/badge.svg)

## Overview
Automated pipeline for a Python-based microservice. The workflow handles code validation, container security auditing, and automated deployment to a cloud environment.

## Pipeline Stages
* **Linting**: Static code analysis using `flake8`.
* **Testing**: Unit tests executed via `pytest`.
* **Security**: Container vulnerability scanning with `Trivy`.
* **Packaging**: Docker image build and push to Docker Hub.
* **Deployment**: Continuous Deployment to Render via Webhooks.

## Tech Stack
* **Language**: Python (FastAPI)
* **Automation**: GitHub Actions
* **Containers**: Docker
* **Security**: Trivy
* **Hosting**: Render

## Access & Usage
* **Live API**: [https://moje-api-latest.onrender.com/](https://moje-api-latest.onrender.com/)
* **Local Run**:
```bash
docker run -p 8000:8000 joemachiato97/moje-api:latest
```
## Preview
![Moja Grafika](image.png)