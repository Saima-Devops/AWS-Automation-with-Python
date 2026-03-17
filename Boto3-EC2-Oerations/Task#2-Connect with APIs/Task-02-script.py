# This script lists all the IAM users

import boto3
from pprint import pprint


# Open Management Console 
aws_management_console = boto3.session.Session(profile_name="default")

# Open IAM Console 
iam_console_resource = aws_management_console.resource('iam') # Resource Object
iam_console_client = aws_management_console.client('iam') # Client Object

# IAM users list with resource object:
for each_user in iam_console_resource.users.all():
    print(each_user.name)

# IAM users list with client object:
for each in iam_console_client.list_users()['Users']:
   print(each['UserName'])

dir(aws_management_console)
pprint(aws_management_console.get_available_resources())