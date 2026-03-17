import boto3

# Create IAM client
iam_console = boto3.client('iam')

result = iam_console.list_users()

for each_user in result['Users']:
    print(each_user['UserName'])