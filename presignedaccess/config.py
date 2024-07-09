# config.py
import boto3

def get_s3_resource(profile_name):
    session = boto3.Session(profile_name=profile_name)
    return session.resource('s3')

def get_s3_client(profile_name):
    session = boto3.Session(profile_name=profile_name)
    return session.client('s3')

PROFILE_NAME = 'iamadmin-2024-general'
