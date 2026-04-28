# Why I Built This Project

## Real World Problem This Solves

Canadian companies collect thousands of documents every day:
- TD Bank processes loan applications and financial reports
- Government of Canada handles citizen documents and policy papers
- Healthcare companies process patient records and medical reports
- Law firms process contracts and legal documents

Reading and summarizing all these documents manually takes hours.
This project automates that entire process using AI.

## How It Works In Real Business

A document is uploaded to S3.
Lambda triggers automatically within seconds.
Claude AI reads and summarizes the document.
Summary is saved back to S3 instantly.
Zero human effort needed.

## Canadian Job Market Relevance

This project targets these roles directly:
- AI Engineer at Canadian banks and fintech companies
- Cloud Engineer at Shopify, Telus, Bell, Rogers
- ML Engineer at startups across Calgary and Toronto
- Federal IT-02/IT-03 roles automating government processes

Skills demonstrated:
- AWS Lambda - serverless computing
- Amazon S3 - cloud storage and event triggers
- Claude AI API - real AI integration
- Python - production code with error handling
- IAM roles - least privilege security
- Automated testing with pytest

## Nokia Connection

At Nokia I worked with automated processing pipelines in 5G core.
When a UE connects, the network automatically triggers AMF, SMF, UPF
in sequence - no manual intervention needed.

This Lambda function follows the exact same event-driven architecture.
S3 upload triggers Lambda - same as UE attach triggers network functions.

## What I Learned

- Serverless architecture - no server management needed
- Event-driven design - S3 triggers Lambda automatically
- AI API integration - Claude AI in production code
- AWS IAM security - least privilege role for Lambda
- Environment variables - secure API key management
- Python packaging - deploying dependencies with Lambda

## Interview Answer

I built a serverless AI document summarizer on AWS.
When a document is uploaded to S3, Lambda triggers automatically,
sends the document to Claude AI, and saves the summary back to S3.
The entire pipeline runs without any servers to manage.

This is the same event-driven pattern used in production at Canadian
banks and government agencies to automate document processing.
It maps directly to my Nokia background where network events
automatically triggered core network function chains.

## Cost

AWS Lambda free tier covers 1 million requests per month.
S3 storage costs less than 1 CAD per month for testing.
Claude AI API costs less than 0.01 per document summary.
Effectively free for portfolio and learning purposes.
