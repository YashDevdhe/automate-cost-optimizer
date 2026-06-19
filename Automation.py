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

    for r in response.get('Reservations', []):
        for i in r.get('Instances', []):
            instances.append(i['InstanceId'])

    print("Instances found:", instances)

    if instances:
        ec2.stop_instances(InstanceIds=instances)
        print("Stopped:", instances)
        return "Stopped instances"
    else:
        return "No instances found"