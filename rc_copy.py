# Importing boto3 library
import boto3
import bucket_check

print(env)

s3 = boto3.resource('s3')
 
#check if the bucket exists or not

print(bucket_check.bucket_exists('bucket123123_1'))
print(bucket_check.bucket_exists('sreekalyan-enterprise-1'))

# Print out bucket names
for bucket in s3.buckets.all():
    print(bucket.name)