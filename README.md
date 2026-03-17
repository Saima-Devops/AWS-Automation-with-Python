# How to automate AWS common tasks using Boto3 and Lambda Functions.


## What is Boto3? 

- Boto3 is the name of the Python SDK/Library/Module/API for AWS.

- Boto3 provides an object-oriented API as well as low-level access to AWS services, making it easy to interact with AWS resources programmatically.

- Boto3 allows us to directly create, update, and delete AWS services from our Python scripts.

- Boto3 is built on the top of the botocore module.

- We have to Install boto3 to work with AWS Services using Python Scripts.



## How Boto3 Works with AWS?

Boto3 works by making API calls to AWS services on your behalf. When you use Boto3 to create an S3 bucket, for example, Boto3 constructs an HTTP request that it sends to AWS S3 service endpoints. AWS processes this request and returns a response, which Boto3 then parses and returns to your application in a Python-friendly format.



**###Pre-requisites:**

- **AWS Account** - It is great if you have a free tier account.

- Basic Knowledge on AWS Services and Python (Not mandatory)

- Basic Knowledge of Any **Python IDE**

---

## How to install boto3?

```bash
Python-2.x:  pip install boto3

Python-3.x:  pip3 install boto3
```

### Install Python and Boto3 on Windows Machine.

Python-3.7.4

Go to www.python.org

Set Paths for python and pip3

Install boto3 using  `pip3 install boto3`


### Install Python and Boto3 on Linux Machine.

```bash
yum install gcc openssl-devel bzip2-devel libffi-devel

cd /usr/src

wget https://www.python.org/ftp/python/3.7.4/Python-3.7.4.tgz

tar xzf Python-3.7.4.tgz

cd Python-3.7.4

./configure --enable-optimizations

make altinstall

cd /usr/local/bin/

./python3.7 --version

./pip3.7 --version

pwd

ln -s /usr/local/bin/python3.7 /bin/python3

python3 --version

ln -s /usr/local/bin/pip3.7 /bin/pip3

pip3 --version

pip3 install boto3
```

---

## Create an Automation Server on AWS EC2 Instance 

If you want an **EC2 instance specifically to run automation scripts using** **Boto3** and manage **AWS Lambda**, you should create the instance with the right **OS, IAM role, and security settings** in **Amazon EC2**. Let's create it now!


### 1️⃣ Create an IAM Role (Important for Automation)

Before launching EC2, create a role so your scripts can access Lambda without storing credentials.

1.  Open **AWS Console**

2.  Go to **IAM → Roles**

3.  Click **Create Role**

4.  Select **AWS service**

5.  Choose **EC2**

6.  Attach policies such as:


**Recommended policies:**

-   **AWSLambdaFullAccess**

-   **AmazonS3FullAccess** (if scripts use S3)

-   **CloudWatchLogsFullAccess**

7.  Name the role

```bash
EC2-Boto3-Automation-Role
```

8.  Create role.

Now EC2 will automatically get credentials via the instance metadata service.

---

### 2️⃣ Launch EC2 Instance

Go to **EC2 → Launch Instance**.

### Basic settings

**Name**

`boto3-automation-server`

**AMI (Operating System)**
Choose:

-   **Amazon Linux 2023** ✅ (recommended)

Why:

-   Lightweight

-   AWS optimized

-   Python friendly

---

### 3️⃣ Choose Instance Type

For automation scripts you don’t need large instances.

Recommended:

`t2.micro` or `t3.micro`

---

### 4️⃣ Key Pair (SSH Access)

Create or select a key pair.

Example:

```bash
boto3-key.pem
```

You will use it to SSH into the server.

---

### 5️⃣ Network Settings


Security Group rules:

**Inbound Rules**

Type: SSH
Port: 22
Source: My IP

> You don't need HTTP/HTTPS unless hosting something.

---

### 6️⃣ Attach IAM Role

In **Advanced Details → IAM Instance Profile**

Select the role you created:

```bash
EC2-Boto3-Automation-Role
```

> This allows Boto3 to call Lambda without credentials.

---

### 7️⃣ Storage

Default `8 GB gp3` volume is enough.

---

### 8️⃣ Launch the Instance

Click **Launch Instance**.

Wait until: **Instance State → Running**

---

### 9️⃣ Connect to EC2

From terminal:

```bash
ssh\-i boto3-key.pem ec2-user@EC2-PUBLIC-IP
```
---

### 🔟 Install Python and Boto3

```bash

# Become a Root User first
sudo bash   # or sudo su

#Update the package list
sudo dnf update -y
```


If you're using **Amazon Linux 2023** the Best Version for AWS Automation is `Python 3.9 or 3.10`

### Install Python 3.9+ For scripts controlling Lambda and Boto3


**Reasons:**

-   Stable

-   Compatible with most AWS SDK libraries

-   Matches many **AWS Lambda** runtimes


### **Command Setup (for Python 3.9 or 3.10 EC2 Instance Servers)**

```bash
# If you're using **Amazon Linux 2023**

sudo dnf update -y
sudo dnf install python3 python3-pip -y
pip3 install boto3


```


**Check:**

```bash
python3 -c "import boto3; print('boto3 installed')"
```

**Pyhton & Boto3 Installation Done**


---


### Boto3 Environment Setup

-   Configure credentials of your AWS account on using aws cli commands.

**What is AWS CLI?**

The AWS Command Line Interface (AWS CLI) is **a unified tool to manage your AWS services**. With just one tool to download and configure, you can control multiple AWS services from the command line and automate them through scripts.

-   **Downloading AWS CLI:** https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html/

-   Login to AWS Management Console and create a new user with programmatic access and provide **AdministratorAccess.**

-   Configure IAM user access-keys/credentials using:

- aws configure 

-----

## Boto3 EC2 Automation


- **Task#01- First Automation Script to list all the IAM Users in your Account**

- **Task#02- Lists all the IAM users throuh Boto3 automation**

- **Task#03- List all the running EC2 instances with their IDs & Names**

- **Task#04- Launch EC2 Instance by using Boto3 script**

- **Task#05- How to Start, Stop & Terminate the Instance**

> Access all Labs here: (https://github.com/Saima-Devops/AWS-Automation-with-Python/tree/616d48bdc0577b83cecc08ea165f118ce4de1a37/Boto3-EC2-Oerations)

----------

**Use Boto3 Documentation to get more information (https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)**

---------

## S3 Buket Operartrions through Boto3 automation

- How to Create an S3 Bucket
- How to List the existing S3 Buckets
- How to Delete an S3 Bucket
- How to Upload a File to the S3 Bucket
- How to Download a File from the S3 Bucket
- How to Delete a File from the S3

> Access all Labs here: 