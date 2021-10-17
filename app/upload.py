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
    query_parameters = request.args
    paperDOI = query_parameters.get('paperDOI')
    # Initiate session
    session = s.Session()
    client = session.client('s3', region_name='fra1', endpoint_url='https://fra1.digitaloceanspaces.com', aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY)
    # Upload a file to your Space
    client.upload_file('DOI/'+paperDOI+'.png', 'aaronskit-cloudstorage', paperDOI+'.png')
    #Speak to remote aaronskit server to create a new entry to the articles table using the URL above and other data