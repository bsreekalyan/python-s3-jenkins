# Importing boto3 library
 import boto3

# Creating a client connection with AWS S3
 s3 = boto3.client('s3')
 
# Storing the client connection within rep
 response = s3.list_buckets()
 
# Output the bucket names
 print('Existing buckets:')
 for bucket in response['Buckets']: # For Loop to list all the buckets
     print(f'{bucket["Name"]}')