import boto3

client = boto3.client('ec2', region_name='us-east-1')

response = client.describe_instances(
    Filters=[
        {
            'Name': 'instance-state-code',
            'Values': ['16']
        },
        {
            'Name': 'tag:k8s.io/role/master',
            'Values': ['1']
        }
    ]
)

# Describe all filtered instances and print instance name and id
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_name = next((tag['Value']
                              for tag in instance['Tags'] if tag['Key'] == 'Name'), 'Unnamed')
        print(f"Instance ID: {instance['InstanceId']} \nInstance Name: {instance_name}")