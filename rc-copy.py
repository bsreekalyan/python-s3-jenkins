# Importing boto3 library
import boto3
import bucketcheck

s3 = boto3.resource('s3')
 
#check if the bucket exists or not

print(bucketcheck.bucket_exists('bucket_1'))
print(bucketcheck.bucket_exists('sreekalyan-enterprise-1'))

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)