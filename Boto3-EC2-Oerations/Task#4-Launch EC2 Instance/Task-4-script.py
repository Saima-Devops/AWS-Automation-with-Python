# This script creates an ec2 instance on aws automatically
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Create EC2 Instance
response = ec2_console.run_instances(
    ImageId="ami-0f559c3642608c138",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1
)
# Print instance ID
for instance in instances:
    print("Launched instance with ID:", instance.id)