🚀 Automated AWS Cost Optimizer

A serverless cloud automation system that automatically detects idle EC2 instances and stops them to reduce AWS costs.

Automated AWS Cost Optimizer: Built a serverless solution using AWS Lambda, CloudWatch, and EC2 to monitor CPU utilization and automatically stop idle instances, reducing cloud costs and improving resource efficiency through event-driven automation.

🧠 Overview

The Automated AWS Cost Optimizer is a fully serverless solution designed to minimize unnecessary AWS billing by automatically identifying and stopping underutilized EC2 instances.

It uses event-driven architecture with AWS-native services to ensure scalability, automation, and zero manual intervention.

🎯 Objective
Detect idle EC2 instances automatically
Reduce AWS cost by stopping unused resources
Build a fully automated DevOps-style cloud system
Eliminate manual monitoring of EC2 usage
🏗️ Architecture
                ┌────────────────────┐
                │   Amazon EC2       │
                │ (Running Instances)│
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Amazon CloudWatch  │
                │ (CPU Monitoring)   │
                └─────────┬──────────┘
                          │ Alarm Trigger
                          ▼
                ┌────────────────────┐
                │ AWS Lambda        │
                │ (Cost Optimizer)  │
                └─────────┬──────────┘
                          │
                          ▼
                ┌────────────────────┐
                │ Stop EC2 Instance  │
                └────────────────────┘
⚙️ AWS Services Used
Amazon EC2 → Compute instances
Amazon CloudWatch → Monitors CPU usage & triggers alarms
AWS Lambda → Executes automation logic
Amazon Web Services → Cloud infrastructure
🔄 Workflow
User launches EC2 instance
Instance runs with tag AutoStop=True
CloudWatch monitors CPU utilization
If CPU < 5% for 10–15 minutes → alarm triggers
AWS Lambda is invoked automatically
Lambda checks running EC2 instances
Matching instances are stopped
AWS cost is reduced automatically
🧰 Prerequisites
AWS Account
IAM permissions for EC2, Lambda, CloudWatch
Basic understanding of AWS services
🪜 Setup Instructions
1. Launch EC2 Instance
Go to EC2 → Launch Instance
Add tag:
Key: AutoStop
Value: True
2. Create IAM Role

Attach permissions:

AmazonEC2FullAccess
CloudWatchLogsFullAccess
AWSLambdaBasicExecutionRole
3. Create Lambda Function
Runtime: Python 3.12
Attach IAM Role
4. Add Lambda Code
import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')

    response = ec2.describe_instances(
        Filters=[
            {'Name': 'instance-state-name', 'Values': ['running']},
            {'Name': 'tag:AutoStop', 'Values': ['True']}
        ]
    )

    instances = []

    for r in response['Reservations']:
        for i in r['Instances']:
            instances.append(i['InstanceId'])

    if instances:
        ec2.stop_instances(InstanceIds=instances)
        print("Stopped:", instances)

    return "Done"
5. Configure CloudWatch Alarm
Metric: CPUUtilization
Condition: CPU < 5%
Duration: 10–15 minutes
Action: Trigger Lambda
📊 Features
⚡ Fully automated EC2 shutdown
💰 Reduces AWS billing cost
☁️ Serverless architecture
📡 Event-driven execution
🔐 Secure IAM-based access
🚀 Future Enhancements
🔄 Auto start EC2 when required
📊 Cost dashboard using CloudWatch metrics
🔔 Email alerts using SNS
🧠 AI-based usage prediction
📦 Multi-region support