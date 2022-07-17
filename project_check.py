from genericpath import exists
import boto3
from botocore.exceptions import ClientError

# To check whether root bucket exists or not
def object_exists(project_name):
   bucket_name='sreekalyan-enterprise-1'+'/'+'release'+'/'+project_name
   try:
      session = boto3.session.Session()
      # User can pass customized access key, secret_key and token as well
      s3_resource = session.resource('s3')
      s3_resource.meta.client.head_bucket(Bucket=bucket_name)
      print("Bucket exists.", bucket_name)
      exists = True
   except ClientError as error:
      error_code = int(error.response['Error']['Code'])
      if error_code == 403:
         print("Private Bucket. Forbidden Access! ", bucket_name)
      elif error_code == 404:
         print("Bucket Does Not Exist!", bucket_name)
      exists = False
      return exists