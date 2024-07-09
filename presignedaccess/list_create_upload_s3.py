import os
import json
import logging
from botocore.exceptions import ClientError
import config

# API documentation for list_bucket
# https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.list_buckets
# Example: List all buckets

# First way to list all buckets
# for bucket in s3.buckets.all():
#     print(bucket.name)

# # Second way to list all buckets
# response = s3.meta.client.list_buckets()
# # Print bucket names
# for bucket in response['Buckets']:
#     print(f'Bucket Name: {bucket["Name"]}, Creation Date: {bucket["CreationDate"]}')

#********************************************************
#Create a bucket
#https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3.html#S3.Client.create_bucket

# try:
#     response = s3_client.create_bucket(Bucket='my-pk-image-bucket')
#     print(response)
# except ClientError as e:
#     if e.response['Error']['Code'] == 'BucketAlreadyExists':
#         print(f"The specified bucket already exists: {e}")
#     else:
#         print(f"An S3-related error occurred: {e}")
#********************************************************


#********************************************************
#Upload an Image
#s3.meta.client.upload_file('image.jpg', 'my-pk-image-bucket', 'image.jpg')

#putobject
#s3.meta.client.put_object(Bucket='my-pk-image-bucket', Key='image.jpg', Body=open('image.jpg', 'rb'))
#********************************************************

def upload_using_client(s3_client, file_name, bucket_name, object_name,prefix=None):
    """
    Upload an image to an S3 bucket with an optional prefix
    :param s3_client: Boto3 S3 client
    :param file_name: File to upload
    :param bucket_name: Bucket to upload to
    :param prefix: Prefix for the object key
    """
    # Create the object key
    object_name = object_name if prefix is None else f"{prefix}/{object_name}"
    
    try:
        s3_client.upload_file(file_name, bucket_name, object_name)
        print(f"File {file_name} uploaded to {bucket_name}/{object_name}")
    except Exception as e:
        print(f"Error uploading file: {e}")
    
    # Upload an image using put_object
    # with open('image.jpg', 'rb') as image_file:
    #     s3_client.put_object(Bucket='my-pk-image-bucket', Key='image.jpg', Body=image_file)
    # print("Uploaded using client")

# Example usage
if __name__ == "__main__":

    logging.basicConfig(level=logging.ERROR)
    LOGGER = logging.getLogger(__name__)
    LOGGER.addHandler(logging.NullHandler())

    # Initialize S3 client using the configuration #High level API
    s3_client = config.get_s3_client(config.PROFILE_NAME)

    # Initialize S3 client using the configuration #Low level API
    # s3_resource = config.get_s3_resource(config.PROFILE_NAME)


    # File and bucket details
    file_name = 'C:\\Users\\6115747\\Downloads\\code_20210907\\code\\s3\\beach.jpg'  # Local file to upload
    bucket_name = 'my-pk-image-bucket'  # S3 bucket name
    prefix = 'imagefile'  # Optional prefix
    object_name = 'beach.jpg'
    
    # Upload the file
    upload_using_client(s3_client, file_name, bucket_name, object_name, prefix)