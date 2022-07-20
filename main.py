#!/usr/bin/env python3
import os
import project_check
import project_copy


projects_list=[]
projects=os.environ["PROJECTS"]
version=os.environ["VERSION"]
release_version=os.environ["RC_VERSION"]
final_version=version+'-'+release_version

# projects=os.environ["env"]
projects_list=projects.split(",")
print(projects_list)
#Validate if the project names and the version&RC_version numbers are valid.
for project in projects_list:
    print(project)
    print(project_check.project_exists(project,final_version))
#Perform the s3 Bucket copy Operation    
for project in projects_list:
    print(f"Performing Release on these {project}")
    print(project_copy.project_release(project,version,release_version))
