# Importing boto3 library
import boto3
import project_check
import os

projects_list=[]
projects=os.environ["env"]
projects_list=projects.split(",")

for project in projects_list:
    print(project_check.object_exists(project))