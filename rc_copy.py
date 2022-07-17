# Importing boto3 library
import boto3
import bucket_check
import os

projects=[]
projects=os.environ["env"]
print(projects)

for project in projects:
    print(bucket_check.bucket_exists(project))