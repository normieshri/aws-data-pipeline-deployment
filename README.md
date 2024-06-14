# aws-data-pipeline-deployment
This repository contains code for an AWS data pipeline project that reads data from S3 and pushes it to RDS or Glue. It uses Docker for containerization, Jenkins for CI/CD, and Terraform for provisioning AWS resources. The pipeline includes Docker image deployment to ECR and a Lambda function using this image.


---

### AWS Data Pipeline Deployment

This repository contains the code and configurations for a data pipeline project that reads data from Amazon S3, processes it, and pushes it to Amazon RDS or AWS Glue. The project leverages Docker for containerization and Jenkins for CI/CD pipeline automation. Terraform is used to provision the necessary AWS resources.

#### Key Features:
- **S3 Data Ingestion:** Read data from an S3 bucket.
- **Data Storage:** Push data to Amazon RDS. If RDS is unavailable, fallback to AWS Glue.
- **Containerization:** Dockerfile to create an image for the application.
- **Deployment:** Docker image deployment to AWS ECR.
- **Serverless Processing:** AWS Lambda function using the Docker image.
- **Infrastructure as Code:** Terraform scripts for provisioning AWS resources.
- **Continuous Integration/Continuous Deployment:** Jenkins pipeline for automated builds and deployments.

#### Repository Structure:
```
aws-data-pipeline-deployment/
│
├── Dockerfile
├── app.py
├── requirements.txt
├── Jenkinsfile
├── terraform/
│   ├── main.tf
│   ├── variables.tf
│   └── outputs.tf
└── README.md
```

#### Getting Started:
1. **Clone the repository:**
   ```sh
   git clone https://github.com/normieshri/aws-data-pipeline-deployment.git
   ```
2. **Build and push Docker image to ECR:**
   - Follow the instructions in the `Jenkinsfile`.
3. **Deploy AWS resources using Terraform:**
   - Navigate to the `terraform` directory and follow the instructions in the `README.md`.
4. **Run the pipeline:**
   - Set up Jenkins and trigger the pipeline to automate the deployment process.

