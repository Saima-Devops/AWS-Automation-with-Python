# This script lists all the running EC2 instances with their IDs & Names

import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

result = ec2_console.describe_instances()['Reservations']

for each_instance in result:
    for value in each_instance['Instances']:

        instance_id = value['InstanceId']
        instance_name = "No Name"

        if 'Tags' in value:
            for tag in value['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
        
        print("--------------")
        print("Instance ID:", instance_id)
        print("Instance Name:", instance_name)
        print("--------------")