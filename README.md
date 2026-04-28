# Serverless AI Document Summarizer

## What This Project Does
Automatically summarizes documents using AWS Lambda and Claude AI.
Upload a document to S3 and get an AI-generated summary back in seconds.
Zero servers to manage. Fully automated pipeline.

## Architecture
Document uploaded to S3
        |
Lambda triggered automatically
        |
Claude AI reads and summarizes
        |
Summary saved back to S3

## What Was Built
- AWS Lambda function - serverless compute
- Amazon S3 - document storage and event trigger
- Claude AI API - intelligent document summarization
- IAM Role with least privilege permissions
- Automated tests with pytest - 2 tests passing
- Error handling - graceful failure management

## Tech Stack
AWS Lambda | Amazon S3 | Claude AI | Python | boto3 | pytest | IAM

## Security
- API keys stored as Lambda environment variables
- Never hardcoded in source code
- IAM role follows least privilege principle
- .gitignore prevents sensitive files from being pushed

## How to Test
pip3 install pytest
python3 -m pytest tests/test_lambda.py -v

## Real World Use Cases
- Canadian banks summarizing loan applications
- Government agencies processing citizen documents
- Healthcare companies summarizing medical reports
- Law firms processing contracts automatically

## Cost
AWS Lambda free tier - 1 million requests per month free
S3 storage - less than 1 CAD per month
Claude AI - less than 0.01 per document

## Screenshots
(screenshots folder coming soon)
