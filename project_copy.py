#!/usr/bin/env python3
import boto3

# s3_session=boto3.client(service_name='s3',region_name='us-west-2')
def project_release(project_name,version,release_version):
    bucket_name = "sreekalyan-enterprise-1"
    project_key = 'release' +'/' + project_name +'/'
    source_version = project_key + version +'-'+ release_version

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)

    for object in bucket.objects.filter(Prefix=source_version):
        key=object.key
        if key.endswith(".tgz"):
            source= { 'Bucket' : bucket_name, 'Key': object.key }
            dest=s3.Bucket(bucket_name)
            destination_path=project_key+version+'/'+key.split(release_version+'/',1)[1]
            dest.copy(source, destination_path)
    print(f"The Release on {project_name} is successful ")
