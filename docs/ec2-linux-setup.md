# EC2 & Linux Setup

This document explains how an Amazon EC2 instance was launched and configured with basic Linux operations.

## EC2 Instance Details

- Cloud Provider: AWS
- Service: Amazon EC2
- AMI: Ubuntu 22.04 LTS
- Instance Type: t3.micro (Free Tier)
- Key Pair: Vasan_Key.pem
- Security Group Rules:
  - SSH (22) – My IP
  - HTTP (80) – Anywhere
  - HTTPS (443) - Anywhere

## Connecting to EC2

The instance was accessed securely using SSH and a private key.

```bash
chmod 400 "Vasan_Key.pem"
ssh -i "Vasan_Key.pem" ubuntu@ec2-52-202-237-234.compute-1.amazonaws.com
