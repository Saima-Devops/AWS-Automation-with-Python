# Boto3 Core Interfaces

Following are the Core Components aka **Boto3 Core Interfaces** used to interact with **Amazon Web Services** services.

In **Boto3**, there are two main ways to interact with **Amazon Web Services** services:

- **Session** (Manages AWS credentials and configuration)
- **Client** (Low-level interface for interacting with AWS services)
- **Resource** (High-level interface for interacting with AWS services)
- **Meta Collections** (Metadata about resource/client/session) 
- **Waiters** (Wait until AWS resource reaches a state)
- **Paginators** (Handle paginated AWS API responses)


In **Boto3**, there are two main ways to interact with **Amazon Web Services** services:

1️⃣ **Client Object**
2️⃣ **Resource Object**

Both let you call AWS APIs, but they work differently.


## 1️⃣ Client Object (Low-Level API)

A **Client Object** provides a **direct mapping to AWS service APIs**.
Each function corresponds almost exactly to the AWS API operation.

Example: Using a client for ***AWS Identity and Access Management (IAM)**

```bash
import boto3

iam_client = boto3.client('iam')

response = iam_client.list_users()

for user in response['Users']:
    print(user['UserName'])
```

**Output:**

{
'Users': [
   {'UserName': 'admin'},
   {'UserName': 'developer'}
 ]
}

### Characteristics

-   Low-level interface

-   Returns **JSON/dictionary responses**

-   Full access to **all AWS API operations**

-   Faster and more explicit

-   Used most often in **automation scripts**

---

## 2️⃣ Resource Object (High-Level API)

A **Resource Object** is a **higher-level, object-oriented interface** that makes AWS services easier to work with.

Example using **Amazon Simple Storage Service (S3)**

```bash
import boto3

s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)
```

OR

```bash
import boto3
bucket = s3.Bucket('my-bucket')
forobjinbucket.objects.all():
print(obj.key)
```

**Output:**

`my-bucket`

### Characteristics

-   Higher-level interface
-   Uses **Python objects**
-   Easier to read and write
-   Automatically handles some API calls


### Key Differences

| Feature | Client Object | Resource Object |
| --- | --- | --- |
| Level | Low-level | High-level |
| Data format | Dictionary/JSON | Python objects |
| API coverage | Full AWS API | Limited |
| Performance | Slightly faster | Slightly slower |
| Usage | Automation, DevOps | Application development |


---

## Important Note

Not all AWS services support **Resource objects**.

For example:

-   **AWS Identity and Access Management** → mostly **Client**

-   **Amazon Simple Storage Service** → Client + Resource

-   **AWS Lambda** → Client only

> For **automation scripts (Lambda, EC2, IAM, etc.)**, engineers usually use:

`boto3.client()`

because it exposes **every AWS API operation**

---

### Resource Object available options in Boto3


Resource objects are only available for these AWS Services only.

```bash
import boto3
aws_management_console.get_available_resources()
```

This shows all AWS services that support **Resource objects**.

**Output:**

['cloudformation', 'cloudwatch', 'dynamodb', 'ec2', 'glacier', 'iam', 's3', 'sns', 'sqs']


**Note:**

All operations in AWS Management Console can be done in Client (beacuse Client is always availabel all the time for all the resources) whereas Resource does not guarantee you that. Some operations may not be supported by Resource Object.

Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

----
