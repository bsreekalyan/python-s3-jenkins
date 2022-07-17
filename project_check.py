from genericpath import exists
import boto3
from botocore.exceptions import ClientError

# To check whether root bucket exists or not
def object_exists(project_name):
   bucket_name='sreekalyan-enterprise-1'
   path='/'+'release'+'/'+project_name
   print(path)
   try:
      session = boto3.session.Session()
      s3_resource = session.resource('s3')
      s3_resource.Object(bucket_name,path).load()
      print("The Project name is valid and accessible")
      exists=True   
   except ClientError as error:
      error_code = int(error.response['Error']['Code'])
      if error_code == 403:
         print("Private Bucket. Forbidden Access! ", bucket_name)
      elif error_code == 404:
         print("Project Does Not Exist!", bucket_name)