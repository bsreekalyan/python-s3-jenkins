import boto3
from botocore.exceptions import ClientError

bucket_name='sreekalyan-enterprise-1'
path=bucket_name+'/'+'release'+project

print(path)