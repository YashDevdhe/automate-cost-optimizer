# Automated AWS Cost Optimizer

A serverless cloud automation solution that automatically identifies and stops idle Amazon EC2 instances to reduce unnecessary AWS costs.

---

## Overview

Cloud resources often remain running even when they are no longer actively used, resulting in avoidable AWS charges.

This project automates the process of detecting underutilized EC2 instances and stopping them using AWS-native services. The entire workflow is event-driven and requires no manual intervention.

The solution leverages Amazon CloudWatch for monitoring, AWS Lambda for automation, and Amazon EC2 for compute resource management.

---

## Problem Statement

Organizations frequently leave EC2 instances running after testing, development, or temporary workloads. Over time, these unused resources contribute to increased cloud spending.

This project addresses that challenge by automatically stopping tagged EC2 instances when their CPU utilization remains below a defined threshold.

---

## Architecture

```text
┌────────────────────┐
│    Amazon EC2      │
│ Running Instances  │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Amazon CloudWatch  │
│ CPU Monitoring     │
└─────────┬──────────┘
          │
     Alarm Trigger
          ▼
┌────────────────────┐
│    AWS Lambda      │
│ Cost Optimizer     │
└─────────┬──────────┘
          │
          ▼
┌────────────────────┐
│ Stop EC2 Instance  │
└────────────────────┘
```

---

## AWS Services Used

* Amazon EC2
* Amazon CloudWatch
* AWS Lambda
* IAM

---

## Features

* Automatic detection of idle EC2 instances
* Event-driven serverless architecture
* Automated EC2 shutdown process
* CloudWatch-based monitoring
* IAM-secured execution
* Reduced operational effort
* Cost optimization through automation

---

## Workflow

1. Launch an EC2 instance.
2. Add the tag:

```text
Key   : AutoStop
Value : True
```

3. CloudWatch continuously monitors CPU utilization.
4. If CPU usage remains below 5% for the configured duration, a CloudWatch alarm is triggered.
5. The alarm invokes the Lambda function.
6. Lambda identifies running instances with the `AutoStop=True` tag.
7. Matching instances are automatically stopped.

---

## Prerequisites

* AWS Account
* Python 3.x
* IAM permissions
* Basic understanding of AWS services

---

## Lambda Function

```python
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

    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instances.append(instance['InstanceId'])

    if instances:
        ec2.stop_instances(InstanceIds=instances)
        print("Stopped:", instances)

    return "Done"
```

---

## Business Impact

* Reduces unnecessary AWS infrastructure costs
* Eliminates manual monitoring efforts
* Improves cloud resource utilization
* Demonstrates real-world cloud automation practices

---

## Skills Demonstrated

* AWS Lambda
* Amazon EC2
* Amazon CloudWatch
* Infrastructure Automation
* Event-Driven Architecture
* Serverless Computing
* Cost Optimization
* Python Automation

---

## Future Enhancements

* Automatic EC2 startup scheduling
* SNS email notifications
* CloudWatch dashboard integration
* Multi-region support
* Cost reporting and analytics
* AI-driven usage prediction

---

## Author

**Yash Devdhe**

AWS Cloud & DevOps Enthusiast

Passionate about cloud automation, serverless architectures, and building efficient infrastructure solutions on AWS.
