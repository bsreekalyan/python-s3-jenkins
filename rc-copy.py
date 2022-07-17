# Importing boto3 library
import boto3
import bucket-check

s3 = boto3.resource('s3')
 
#check if the bucket exists or not

print(bucket_exists('bucket_1'))
print(bucket_exists('sreekalyan-enterprise-'))

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)