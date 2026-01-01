# PunAI-AI Customer Service Bot
PunAI is a **serverless, AI-powered customer support system** designed for small and medium businesses.
It automatically handles customer queries, maintains conversation context, detects dissatisfaction, and escalates critical issues to human support using AWS services.

This project demonstrates **Applied AI, cloud-native architecture,** and **production-grade backend design.**

# Project Overview:
Customer support teams often struggle with:
  -High volume of repetitive queries
  -Delayed responses
  -Poor escalation handling
  -No conversation memory

# PunAI solves this by:
  -Providing instant AI-generated responses
  -Maintaining user conversation history
  -Detecting unhappy or critical customer intent
  -Automatically escalating issues via email alerts
  -Running fully serverless on AWS (cost-efficient & scalable)

# Key Features:
  -AI-powered response generation (OpenAI)
  -Context-aware conversations using DynamoDB
  -Intelligent escalation to human support
  -Serverless architecture (no EC2 required)
  -Secure API endpoint using API Gateway
  -CloudWatch logging & monitoring
  -Production-ready alerting via SNS

# Architecture Diagram:
![PunAI - Architecture (1)](https://github.com/user-attachments/assets/65265fdc-c12f-4f25-98d5-574b06fa9735)

# Diagram Flow chart:
Customer / Client (Postman / App)
        |
        v
Amazon API Gateway (POST /chat)
        |
        v
AWS Lambda (PunAI Core Logic)
  ├─ OpenAI API (AI response + intent)
  ├─ DynamoDB (conversation history)
  ├─ Amazon SNS (escalation alerts)
  └─ CloudWatch (logs & monitoring)
        |
        v
Admin Email (Support Team)

# AWS Services Used:
| Service                | Purpose                              |
| ---------------------- | ------------------------------------ |
| Amazon API Gateway     | Exposes REST endpoint (`POST /chat`) |
| AWS Lambda             | Core backend + AI orchestration      |
| Amazon DynamoDB        | Stores conversation history          |
| Amazon SNS             | Sends escalation emails              |
| Amazon CloudWatch      | Logging and monitoring               |
| IAM                    | Secure permissions & access control  |


# How It Works (Step-by-Step Flow)
1. Customer sends a message via API (/chat)
2. API Gateway forwards request to Lambda
3. Lambda:
    -Reads conversation history from DynamoDB
    -Builds AI prompt with context
    -Calls OpenAI for response
4. AI response is returned to the user
5. Message + reply stored in DynamoDB
6. If message indicates dissatisfaction:
     -SNS sends escalation email to admin
7. Logs captured in CloudWatch
✅ Fully automated
✅ Context-aware
✅ Human escalation supported

# API Usage (Example)

# Endpoint:
POST https://<api-id>.execute-api.ap-south-1.amazonaws.com/_prod/chat

# Request Body:
{
  "user_id": "customer_123",
  "message": "My order has not arrived yet"
}

# Response:
{
  "reply": "I’m sorry to hear that. I’ll escalate this to our support team.",
  "escalation": true
}

# Security & Best Practices:
  -API keys stored in Lambda environment variables
  -IAM roles with least privilege
  -No credentials committed to GitHub
  -Serverless reduces attack surface

# Scalability & Performance:
  -Automatically scales with traffic
  -DynamoDB on-demand capacity
  -No infrastructure limits
  -Suitable for thousands of users

# Future Improvements:
  -AI-based intent classification (no keywords)
  -Web frontend (React / Next.js)
  -Voice-based assistant
  -WhatsApp / Telegram integration
  -Admin dashboard
  -Multi-tenant SaaS support
  -Sentiment analysis & analytics
  -Authentication using Amazon Cognito
