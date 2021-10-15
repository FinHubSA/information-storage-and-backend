import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin
from boto3 import session as s
from botocore.client import Config

ACCESS_ID = 'ZOO2NN5ZCZKZCDTVMTSY'
SECRET_KEY = 'qfFQWuvjutxD6Gu1PIrpwxZCq8nv2m2L5x0w8+3jHGo'

@app.route("/api/upload")
@cross_origin()
def uploadPdf():
    # Initiate session
    session = s.Session()
    client = session.client('s3', region_name='fra1', endpoint_url='https://fra1.digitaloceanspaces.com', aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY)

    f = request.files['file']
    filename = secure_filename(f.filename)
    # Upload a file to your Space
    client.upload_file('abc.png', 'aaronskit-cloudstorage', 'uploaded-test.png')


    # Upload a file to your Space
    # client.put_object(Bucket='aaronskit-cloudstorage',
    #               Key='abc.png',
    #               Body=b'The contents of the file.',
    #               ACL='private',
    #               Metadata={
    #                   'x-amz-meta-my-key': 'your-value'
    #               }
    #             )
    
    print('hello')

    # client.upload_file('abc.png', 'aaronskit-cloudstorage', 'abc.png')