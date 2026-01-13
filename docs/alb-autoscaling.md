# Application Load Balancer & Auto Scaling

This document describes how high availability and scalability were implemented.

## Components Used
- Application Load Balancer (ALB)
- Target Group
- Auto Scaling Group (ASG)
- Launch Template

## Implementation Details
- Created AMI from configured EC2
- Used launch template for consistent instances
- Configured ALB to distribute traffic
- Enabled auto scaling based on CPU metrics

## Result
- Application is highly available
- Traffic is load balanced
- Infrastructure scales automatically
