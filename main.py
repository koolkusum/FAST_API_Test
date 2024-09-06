from fastapi import FastAPI, UploadFile, File, HTTPException

import os
# to load in the credential information from the .env file
from dotenv import load_dotenv
# using boto3 to make the calls to s3
from boto3 import client
from botocore.exceptions import ClientError
import logging


load_dotenv()
app = FastAPI()


# load in the the access key id and the secret key generated from my aws account
aws_access_key_id = os.getenv("aws_secret_access_key_id")
aws_secret_access_key = os.getenv("aws_secret_access_key")
aws_bucket_name = os.getenv("aws_bucket_name")

# to run the code run the following command:
# python -m uvicorn main:app --reload


#intialize the session with the client information
s3 = boto3.client('s3', aws_access_key_id, aws_secret_access_key)

@app.get("/")
async def root():
 return {"greeting":"Hello world"}

# uploaded directly from aws doc
def upload_file(file_name, bucket, object_name=None):
    """Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """

    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    try:
        response = s3.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True