# AWS IAM Setup

This document describes the initial AWS Identity and Access Management (IAM) configuration for this project.

## Steps Performed

- Created a dedicated IAM user for DevOps activities instead of using the root account
- Attached AdministratorAccess policy for full AWS access (for learning purpose)
- Enabled Multi-Factor Authentication (MFA) to improve account security

## Purpose

- To follow AWS best practices by avoiding root account usage
- To securely manage access to AWS services
- To prepare the account for EC2, RDS, S3, and other AWS services used in this project
