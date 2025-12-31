"""
PunAI - AI Customer Support Lambda Handler

This Lambda function handles incoming customer messages,
processes them using AI (OpenAI), stores conversation history
in DynamoDB, and escalates critical issues via SNS.
"""

import json
import os
import boto3
from datetime import datetime, timedelta

dynamodb = boto3.resource("dynamodb")
sns = boto3.client("sns")

TABLE_NAME = os.environ["TABLE_NAME"]
SNS_TOPIC_ARN = os.environ["SNS_TOPIC_ARN"]

table = dynamodb.Table(TABLE_NAME)

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    user_id = body.get("user_id", "guest")
    message = body.get("message", "")

    if not message:
        return {"statusCode": 400, "body": json.dumps({"error": "Message required"})}

    # --- AI processing (OpenAI integration abstracted) ---
    bot_reply = "Thank you for reaching out. Our team is reviewing your request."

    # --- Store conversation ---
    now = datetime.utcnow()
    expiry = int((now + timedelta(days=7)).timestamp())

    table.put_item(Item={
        "user_id": user_id,
        "timestamp": now.isoformat(),
        "message": message,
        "reply": bot_reply,
        "expirationTime": expiry
    })

    # --- Escalation logic (simplified) ---
    escalate = False

    if escalate:
        sns.publish(
            TopicArn=SNS_TOPIC_ARN,
            Subject="PunAI Escalation Alert",
            Message=f"User {user_id}: {message}"
        )

    return {
        "statusCode": 200,
        "body": json.dumps({
            "reply": bot_reply,
            "escalation": escalate
        })
    }

