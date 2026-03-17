# TASK-01:

**First Automation Script to list all the IAM Users in your Account**

First let us do it manually and see in the AWS Management Console

**Manual Steps:**

**Step1:** Get AWS Management Console (https://aws.amazon.com/console/)

**Step2:** Get IAM Console

In IAM Console we have many options to select like:

- Users

- Groups

- Roles

- Policies etc...

**Step3:** Create an IAM User

- Assign Role as Full Administrator Access 

- Create User

- Download the Access Key and Save it. This access key is essential to connect with AWS CLI

- got to any CLI and type 'aws configure' 

- Give the credentials and then run the Task-01-script.py file

- you will get the list of all created users in your account
