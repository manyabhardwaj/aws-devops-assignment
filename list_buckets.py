import boto3

s3 = boto3.client('s3')

buckets = s3.list_buckets()

print("Your S3 Buckets:")
for bucket in buckets['Buckets']:
    print(f' - {bucket["Name"]}')
