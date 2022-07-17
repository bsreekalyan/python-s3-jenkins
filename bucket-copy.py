import boto3
s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'mybucket',
    'Key': 'mykey'
 }
s3.meta.client.copy(copy_source, 'otherbucket', 'otherkey')