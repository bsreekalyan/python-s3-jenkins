#!/usr/bin/env python3
import boto3



def project_exists(project_name,final_version):
    bucket_name = "sreekalyan-enterprise-1"
    project_key = 'release' +'/' + project_name +'/'
    version_key = project_key + final_version + '/'
    s3_session = boto3.client(service_name='s3',region_name='us-west-2')
    
    project = s3_session.list_objects_v2(Bucket=bucket_name, Prefix=project_key)
    if 'Contents' in project:
        print("Project exists")
        # Check Version
        version = s3_session.list_objects_v2(Bucket=bucket_name, Prefix=version_key)
        if 'Contents' in version:
            print(f"The {final_version} Release version exists")    
        else:
            print(f"Wrong Version {final_version} Entered! Please check the Version and Release-Version Input")
            exit()
    else:
        print(f"The Project {project_name} doesn't exist")
        exit()
