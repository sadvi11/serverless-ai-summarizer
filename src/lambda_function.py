import json
import boto3
import urllib.request
import os

s3_client = boto3.client("s3")

def get_claude_summary(text):
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    payload = json.dumps({
        "model": "claude-haiku-4-5-20251001",
        "max_tokens": 1024,
        "messages": [{"role": "user", "content": f"Summarize in 3-5 bullet points:\n\n{text[:3000]}"}]
    }).encode("utf-8")
    req = urllib.request.Request(
        "https://api.anthropic.com/v1/messages",
        data=payload,
        headers={"Content-Type": "application/json", "x-api-key": api_key, "anthropic-version": "2023-06-01"},
        method="POST"
    )
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read().decode("utf-8"))
        return result["content"][0]["text"]

def lambda_handler(event, context):
    try:
        bucket_name = event["Records"][0]["s3"]["bucket"]["name"]
        file_key = event["Records"][0]["s3"]["object"]["key"]
        print(f"Processing file: {file_key} from bucket: {bucket_name}")
        response = s3_client.get_object(Bucket=bucket_name, Key=file_key)
        file_content = response["Body"].read().decode("utf-8")
        summary = get_claude_summary(file_content)
        filename = file_key.split("/")[-1]
        summary_key = f"summaries/{filename}_summary.txt"
        s3_client.put_object(Bucket=bucket_name, Key=summary_key, Body=summary.encode("utf-8"), ContentType="text/plain")
        return {"statusCode": 200, "body": json.dumps({"message": "Document summarized successfully", "summary_location": summary_key, "summary": summary})}
    except Exception as e:
        print(f"Error: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": str(e)})}
