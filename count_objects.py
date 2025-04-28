import boto3

# AWS S3 client
s3 = boto3.client('s3')

bucket_name = 'mybucket-manya123'

# List objects
response = s3.list_objects_v2(Bucket=bucket_name)

# Count objects
if 'Contents' in response:
    print(f"Total objects in bucket '{bucket_name}': {len(response['Contents'])}")
else:
    print(f"No objects found in bucket '{bucket_name}'.")
