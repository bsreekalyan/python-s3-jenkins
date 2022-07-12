import boto3

#Creating Session With Boto3.
session = boto3.Session(
aws_access_key_id='Your Access Key ID',
aws_secret_access_key='Your Secret access key'
)

#Creating S3 Resource From the Session.
s3 = session.resource('s3')

srcbucket = s3.Bucket('your_source_bucket_name')

destbucket = s3.Bucket('your_target_bucket_name')

# Iterate All Objects in Your S3 Bucket Over the for Loop
for file in srcbucket.objects.all():
    
    #Create a Soucre Dictionary That Specifies Bucket Name and Key Name of the Object to Be Copied
    copy_source = {
    'Bucket': 'your_source_bucket_name',
    'Key': file.key
    }
    
    destbucket.copy(copy_source, file.key)
    
    print(file.key +'- File Copied')
