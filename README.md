
# 🚗 Vehicle Insurance Prediction using MLOps

This project demonstrates a **complete end-to-end MLOps pipeline** — from **data ingestion to deployment** — using modern DevOps and ML lifecycle practices.
It showcases how to build a **production-ready ML system** integrating **MongoDB, AWS (S3, ECR, EC2), Docker, and CI/CD with GitHub Actions**.

---

## 📋 Table of Contents

* [🎯 Project Overview](#-project-overview)
* [🧩 Tech Stack](#-tech-stack)
* [🏗️ Project Architecture](#️-project-architecture)
* [⚙️ Step-by-Step Implementation](#️-step-by-step-implementation)

  * [1️⃣ Project Setup](#1️⃣-project-setup)
  * [2️⃣ MongoDB Setup](#2️⃣-mongodb-setup)
  * [3️⃣ Logging, Exception & EDA](#3️⃣-logging-exception--eda)
  * [4️⃣ Data Ingestion](#4️⃣-data-ingestion)
  * [5️⃣ Data Validation, Transformation & Model Training](#5️⃣-data-validation-transformation--model-training)
  * [6️⃣ AWS & Model Deployment Setup](#6️⃣-aws--model-deployment-setup)
  * [7️⃣ CI/CD Pipeline Setup](#7️⃣-cicd-pipeline-setup)
* [🧠 Features](#-features)
* [🚀 Deployment](#-deployment)
* [🖥️ App Access](#️-app-access)
* [📦 Folder Structure](#-folder-structure)
* [📚 References](#-references)

---

## 🎯 Project Overview

This MLOps project demonstrates:

* Building a **machine learning pipeline** for vehicle data prediction.
* Automating each stage of the ML lifecycle — data ingestion, validation, transformation, model training, evaluation, and deployment.
* Integrating **CI/CD pipelines** to automate builds, testing, and deployment on **AWS EC2**.
* Deploying the trained ML model inside a **Docker container** for scalable serving.

---

## 🧩 Tech Stack

| Category            | Tools / Technologies        |
| ------------------- | --------------------------- |
| Language            | Python 3.10                 |
| Database            | MongoDB Atlas               |
| Cloud Services      | AWS S3, EC2, ECR, IAM       |
| Containerization    | Docker                      |
| CI/CD               | GitHub Actions              |
| Version Control     | Git & GitHub                |
| ML Framework        | Scikit-learn, Pandas, NumPy |
| Web Framework       | Fast API                    |
| Virtual Environment | Conda                       |

---

## 🏗️ Project Architecture

```
                ┌──────────────────────────────┐
                │        Data Source (CSV)     │
                └──────────────┬───────────────┘
                               │
                               ▼
                    MongoDB Atlas (Cloud DB)
                               │
                               ▼
                      Data Ingestion Layer
                               │
                               ▼
                    Data Validation & Transformation
                               │
                               ▼
                         Model Training
                               │
                               ▼
                         Model Evaluation
                               │
                               ▼
                        Model Registry (AWS S3)
                               │
                               ▼
                      Model Deployment (EC2)
                               │
                               ▼
                      Web App (Fast + HTML)
```

---

## ⚙️ Step-by-Step Implementation

### 1️⃣ Project Setup

* Create a project template by executing `template.py`.
* Configure `setup.py` and `pyproject.toml` for local package imports.
* Create and activate a virtual environment:

  ```bash
  conda create -n vehicle python=3.10 -y
  conda activate vehicle
  pip install -r requirements.txt
  ```
* Verify installation:

  ```bash
  pip list
  ```

---

### 2️⃣ MongoDB Setup

1. Create a **MongoDB Atlas** account and new project.
2. Deploy a **free cluster (M0)** and create a database user.
3. Add IP access (`0.0.0.0/0`) for global access.
4. Get your **connection string**:

   ```
   mongodb+srv://<username>:<password>@cluster.mongodb.net/
   ```
5. Load your dataset via Jupyter Notebook (`mongoDB_demo.ipynb`).
6. Verify uploaded data in MongoDB Collections.

---

### 3️⃣ Logging, Exception & EDA

* Implement `logger.py` and `exception.py` for debugging and monitoring.
* Perform **EDA and feature engineering** on the dataset in a dedicated notebook.

---

### 4️⃣ Data Ingestion

* Create configuration and entity classes for ingestion:

  * `constants.__init__.py`
  * `configuration.mongo_db_connections.py`
  * `data_access/proj1_data.py`
  * `entity/config_entity.py`
  * `entity/artifact_entity.py`
  * `components/data_ingestion.py`
* Set MongoDB connection URL as an environment variable:

  ```bash
  export MONGODB_URL="mongodb+srv://<username>:<password>@..."
  ```
* Run `demo.py` to verify successful data fetching.

---

### 5️⃣ Data Validation, Transformation & Model Training

* Define schema details in `config/schema.yaml`.
* Add validation logic in `components.data_validation.py`.
* Perform feature transformations in `components.data_transformation.py`.
* Train ML model in `components.model_trainer.py`.
* Implement custom estimator logic in `entity/estimator.py`.

---

### 6️⃣ AWS & Model Deployment Setup

* Create an **IAM user** with `AdministratorAccess`.
* Configure AWS credentials:

  ```bash
  export AWS_ACCESS_KEY_ID="YOUR_KEY"
  export AWS_SECRET_ACCESS_KEY="YOUR_SECRET"
  ```
* Create an **S3 Bucket** for model registry:

  ```
  Bucket Name: my-model-mlopsproj
  ```
* Add AWS configuration in:

  * `constants.__init__.py`
  * `src/configuration/aws_connection.py`
  * `src/aws_storage/s3_estimator.py`
* Build Model Evaluation & Model Pusher components.

---

### 7️⃣ CI/CD Pipeline Setup

* Add **App** via `app.py` with routes `/` and `/train`.
* Create `static` and `templates` folders for UI.
* Setup **Docker**:

  ```
  Dockerfile
  .dockerignore
  ```
* Create **GitHub Actions Workflow** under `.github/workflows/aws.yaml`.
* Setup **ECR Repository**:

  ```
  Name: vehicleproj
  Region: us-east-1
  ```
* Create **EC2 Instance** and install Docker:

  ```bash
  curl -fsSL https://get.docker.com -o get-docker.sh
  sudo sh get-docker.sh
  sudo usermod -aG docker ubuntu
  newgrp docker
  ```
* Configure **Self-hosted GitHub Runner** on EC2.
* Add **GitHub Secrets**:

  * `AWS_ACCESS_KEY_ID`
  * `AWS_SECRET_ACCESS_KEY`
  * `AWS_DEFAULT_REGION`
  * `ECR_REPO`
* Commit & Push — pipeline triggers automatic deployment.

---

## 🧠 Features

✅ End-to-End ML Pipeline
✅ Automated Data Ingestion & Validation
✅ Model Training, Evaluation & Pushing to AWS S3
✅ Dockerized  Application
✅ Continuous Integration & Deployment with GitHub Actions
✅ Real-time Deployment on AWS EC2

---

## 🚀 Deployment

Once CI/CD is successful:

1. Open your **EC2 Security Group**.
2. Add inbound rule:

   ```
   Type: Custom TCP
   Port: 5000
   Source: 0.0.0.0/0
   ```
3. Launch the app using:

   ```
   http://<EC2_PUBLIC_IP>:5000
   ```

---

## 🖥️ App Access

* Visit: `http://<EC2_PUBLIC_IP>:5000`
* Train Model: `http://<EC2_PUBLIC_IP>:5000/train`

---

## 📦 Folder Structure

```
📂 Vehicle-MLops-Project
│
├── 📁 src
│   ├── components
│   ├── configuration
│   ├── data_access
│   ├── entity
│   ├── aws_storage
│   └── utils
│
├── 📁 notebook
│   └── mongoDB_demo.ipynb
│
├── app.py
├── setup.py
├── pyproject.toml
├── requirements.txt
├── Dockerfile
├── .dockerignore
├── .github/workflows/aws.yaml
└── README.md
```

---




