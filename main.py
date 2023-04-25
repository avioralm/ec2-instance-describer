import boto3

client = boto3.client('ec2', region_name='us-east-1')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-code',
            'Values': [
                '16',
            ]
        },
        {
            'Name': 'tag:tag:k8s.io/role/master',
            'Values': [
                '1',
            ]
        },
    ]
)

for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f" Instance ID: {instance['InstanceId']} Instance Name: {instance['KeyName']}")