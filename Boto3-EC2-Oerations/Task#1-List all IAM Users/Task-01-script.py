import boto3

# Create IAM client
iam_console = boto3.client('iam')

result = iam_console.list_users()

for each_user in result['Users']:
    print(each_user['UserName'])


# Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)