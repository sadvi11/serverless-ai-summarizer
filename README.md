# Serverless AI Document Summarizer

> Fully serverless AI document summarization pipeline using AWS Lambda, S3, and Claude AI — zero servers, automatic scaling, pay-per-use.

[![Python](https://img.shields.io/badge/Python-3.11-3776AB?logo=python)](https://python.org)
[![AWS Lambda](https://img.shields.io/badge/AWS-Lambda-FF9900?logo=awslambda)](https://aws.amazon.com/lambda)
[![AWS S3](https://img.shields.io/badge/AWS-S3-FF9900?logo=amazonaws)](https://aws.amazon.com/s3)
[![Claude AI](https://img.shields.io/badge/Claude_AI-Anthropic-D4A27F)](https://anthropic.com)
[![Status](https://img.shields.io/badge/Status-Deployed%20%26%20Verified-2ea44f)]()

---

## What This Project Does

An event-driven serverless pipeline that automatically summarizes documents using
Claude AI. A document uploaded to S3 triggers a Lambda function that reads the
content, calls the Claude API for intelligent summarization, and returns a
structured summary. No servers to manage. Scales automatically from zero to
thousands of concurrent requests. Cost approaches zero for low-volume usage.

---

## Architecture

```
  DOCUMENT UPLOAD              AWS CLOUD                    OUTPUT
  ───────────────             ───────────                  ────────
  Upload PDF/TXT         ┌──────────────────┐
  to S3 bucket   ──────► │   AWS S3 Bucket  │
                         │   (trigger)      │
                         └────────┬─────────┘
                                  │ S3 Event Trigger
                         ┌────────▼─────────┐
                         │   AWS Lambda     │
                         │   Function       │
                         │                  │
                         │  1. Read S3 doc  │
                         │  2. Call Claude  │
                         │  3. Parse output │
                         └────────┬─────────┘
                                  │
                         ┌────────▼─────────┐
                         │   Claude AI API  │    ──────► Summary JSON
                         │   (Anthropic)    │
                         └──────────────────┘
```

---

## Components

| Component | Technology | Purpose |
|---|---|---|
| Trigger | AWS S3 Event | Document upload fires Lambda automatically |
| Compute | AWS Lambda | Serverless function — runs only when triggered |
| Storage | AWS S3 | Document input and summary output storage |
| AI Engine | Claude API | Intelligent document summarization |
| Packaging | Lambda ZIP | Dependencies bundled for Lambda deployment |
| Tests | pytest | Validates Lambda function and Claude integration |

---

## Serverless Advantages

| Traditional Server | This Serverless Approach |
|---|---|
| EC2 running 24/7 | Lambda runs only when triggered |
| Fixed monthly cost | Pay only per invocation (near zero) |
| Manual scaling | Automatic scaling to any volume |
| Server maintenance | Zero infrastructure management |
| Deployment complexity | Single ZIP upload |

---

## Key Design Decisions

**Why Lambda over EC2 for AI inference?**
Document summarization is an event-driven, intermittent task — documents arrive
unpredictably. Lambda is the right tool: it scales from zero when idle to handle
bursts of uploads, with billing only for actual execution time. EC2 would run and
bill 24/7 regardless of whether documents are being processed.

**Why S3 for document storage instead of direct API upload?**
S3 decouples ingestion from processing. Documents can be uploaded by any source —
web app, CLI, another Lambda — without changing the processing pipeline. S3 also
provides durable storage, versioning, and access logging automatically.

**Why Claude AI for summarization?**
Claude handles documents of varying structure — PDFs, reports, technical documents —
without custom parsing logic. Claude's large context window enables summarizing
long documents in a single API call without chunking complexity.

**Why package dependencies in a ZIP instead of a Lambda Layer?**
For a single-function deployment, a self-contained ZIP is simpler and avoids
Layer versioning complexity. The 17MB package includes all dependencies needed
for Lambda execution.

---

## Deployment

```bash
# Clone
git clone https://github.com/sadvi11/serverless-ai-summarizer.git
cd serverless-ai-summarizer

# Install dependencies locally
pip install -r requirements.txt -t package/

# Create deployment package
cd package && zip -r ../lambda.zip . && cd ..
zip lambda.zip lambda_function.py

# Deploy to AWS Lambda
aws lambda create-function \
  --function-name document-summarizer \
  --runtime python3.11 \
  --role arn:aws:iam::ACCOUNT_ID:role/lambda-role \
  --handler lambda_function.lambda_handler \
  --zip-file fileb://lambda.zip

# Set environment variables
aws lambda update-function-configuration \
  --function-name document-summarizer \
  --environment Variables={ANTHROPIC_API_KEY=your_key}
```

---

## Sample Output

```json
{
  "document": "test_document.txt",
  "summary": "This document discusses...",
  "key_points": [
    "Point 1...",
    "Point 2...",
    "Point 3..."
  ],
  "word_count": 1250,
  "summary_word_count": 87
}
```

---

## Repository Structure

```
serverless-ai-summarizer/
├── src/
│   └── lambda_function.py  # Main Lambda handler
├── tests/
│   └── test_lambda.py      # pytest test suite
├── lambda.zip              # Deployment package (built)
├── test_document.txt       # Sample document for testing
├── requirements.txt        # Python dependencies
├── WHY.md                  # Design decision documentation
└── README.md
```

---

## Interview Talking Points

- **Event-driven architecture** — how S3 triggers Lambda automatically
- **Lambda cold starts** — what they are, how to mitigate them
- **Lambda packaging** — ZIP vs Layers, size limits, dependency management
- **IAM roles for Lambda** — execution role, S3 read permission, secrets access
- **Claude API in serverless context** — timeout considerations, error handling
- **Cost model** — Lambda pricing per invocation vs EC2 hourly billing
- **Serverless limitations** — 15-minute timeout, 10GB memory, cold start latency

---

## Author

**Sadhvi Sharma** — Cloud & AI Engineer
Nokia India (5G Packet Core) → Cloud & AI Engineering
Calgary, AB, Canada | Permanent Resident | Open to Relocation

[LinkedIn](https://linkedin.com/in/sadhvi-sharma-5789a6249) | [GitHub](https://github.com/sadvi11)
