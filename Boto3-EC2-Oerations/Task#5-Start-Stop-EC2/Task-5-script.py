# Import all the modules & Libraries
import boto3

# Open Management Console
aws_management_console = boto3.session.Session(profile_name="default")

# Open EC2 Console
ec2_console = aws_management_console.client(service_name="ec2")

# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

# Stop the previous running EC2 Instance
response = ec2_console.stop_instances(
    InstanceIds=['i-0a8883f67ee0f1c68']
)


# Start EC2 Instance
#response = ec2_console.start_instances(
#    InstanceIds=['i-0a8883f67ee0f1c68'],
#)

# Terminate EC2 Instance
#response = ec2_console.terminate_instances(
#    InstanceIds=['i-0a8883f67ee0f1c68'],
#)
