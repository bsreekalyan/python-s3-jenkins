# Importing boto3 library
import boto3
import bucket_check
import os

projects_list=[]
projects=os.environ["env"]
projects_list=projects.split(",")

for project in projects_list:
    print(bucket_check.bucket_exists(project))