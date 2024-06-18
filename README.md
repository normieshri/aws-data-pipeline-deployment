AWS Data Pipeline Project
Overview

This project aims to create a data pipeline using various AWS services to automate the process of uploading a remote CSV file to an S3 bucket, processing it with a Lambda function, and uploading the modified data to an RDS database.
Tech Stack

    Amazon EC2
    Amazon S3
    Amazon Lambda
    Amazon RDS
    Amazon ECR
    Docker
    Python
    Shell Scripting

Objective

The main objective of this project is to transfer a remote CSV file to an S3 bucket, trigger a Lambda function to modify the data, and store the modified data in a private RDS database.
Setup Steps

    IAM Role: Create a suitable IAM role for the Lambda function with access to S3, RDS, and CloudWatch.
    Amazon VPC and Security Groups: Create a dedicated VPC for all services, with RDS, EC2, and Lambda in a private subnet.
    EC2 Instance: Launch an EC2 instance with the necessary IAM role and security group.
    Amazon S3: Create an S3 bucket for uploading the CSV file.
    Amazon RDS MySQL: Create an RDS MySQL database with the required configuration.
    Lambda Function: Create a Lambda function using a Docker image to process the CSV file and upload the data to RDS.

Deployment

    Docker Image: Build and push the Docker image to AWS ECR.
    Lambda Function: Create the Lambda function using the Docker image.
    Testing: Test the Lambda function to ensure it processes the CSV file correctly.

Conclusion

This project demonstrates the automation of a data pipeline using AWS services, enabling the seamless transfer and processing of data from a remote source to a secure RDS database.
