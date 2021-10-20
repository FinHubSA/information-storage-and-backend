import paramiko
import ftplib
import pymysql
from werkzeug.datastructures import FileStorage
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin
from boto3 import session as s
from werkzeug.utils import secure_filename
import json
from botocore.client import Config
import urllib.request as requests

ACCESS_ID = 'ZOO2NN5ZCZKZCDTVMTSY'
SECRET_KEY = 'qfFQWuvjutxD6Gu1PIrpwxZCq8nv2m2L5x0w8+3jHGo'
# remoteURL = "https://api-aaronskit.org/api/"
remoteURL = "http://localhost:5000/api/"
newJournalID = None
uploadedFile = FileStorage

#upload json files with the following command:
#curl -X POST -F file=@"sdfstrvadfdsfdsfdl442l.pdf" https://api-aaronskit.org/api/upload-paper-droplet
#curl -X POST -F file=@"sdfstrvadfdsfdsfdl442l.json" https://api-aaronskit.org/api/upload-metadata
#NB: use the following naming convention: doi.json, doi.pdf

#sample endpoint:
#http://localhost:5000/api/upload-pdf?paperDOI=sdfstrvadfdsfdsfdl442r

def checkAuthorExists(paperDOI):
    newArticle = json
    with open("Metadata/"+paperDOI+".json", "r") as read_file:
        newArticle = json.load(read_file)
     #check if author exists
    authorURL= remoteURL+"author/check?surname="+newArticle["AuthorSurname"]+"&initial="+newArticle["AuthorInitial"]
    authorRAW = requests.urlopen(authorURL).read()
    authorCheck = json.loads(authorRAW)
    return authorCheck

def checkJournalExists(paperDOI):
    newArticle = json
    with open("Metadata/"+paperDOI+".json", "r") as read_file:
        newArticle = json.load(read_file)
    replcaceSpacesJournal = replaceSpaces(newArticle["JournalName"])
    journalURL= remoteURL+"journals/check?checkjournal="+replcaceSpacesJournal
    journalRAW = requests.urlopen(journalURL).read()
    print(journalRAW)
    journalCheck = json.loads(journalRAW)
    return journalCheck

def checkArticleExists(paperDOI):
    newArticle = json
    with open("Metadata/"+paperDOI+".json", "r") as read_file:
        newArticle = json.load(read_file)
    doi = newArticle["DOI"]
    articlelURL= remoteURL+"articles/doi?checkdoi="+paperDOI
    print(articlelURL)
    articleRAW = requests.urlopen(articlelURL).read()    
    articleCheck = json.loads(articleRAW)
    return articleCheck
    

def replaceSpaces(replaceString):
    replcaceSpacesString = replaceString.replace(" ", "%20")
    return replcaceSpacesString


@app.route("/api/upload-metadata", methods=['POST','PUT'])
@cross_origin()
def uploadMetadata():
    ##### Upload Metadata #####    
    uploadedFile = request.files['file']
    filename=secure_filename(uploadedFile.filename)  
    uploadedFile.save("Metadata/"+filename) 
    return filename

@app.route("/api/upload-paper-droplet", methods=['POST','PUT'])
@cross_origin()
def uploadPaperToServer():
    ##### Upload Metadata #####    
    uploadedFile = request.files['file']
    filename=secure_filename(uploadedFile.filename)  
    uploadedFile.save("Papers/"+filename) 
    return filename

@app.route("/api/upload-pdf")
@cross_origin()
def uploadPdf():
    ##### Upload PDF #####    
    query_parameters = request.args
    paperDOI = query_parameters.get('paperDOI')
    # Initiate session
    session = s.Session()
    client = session.client('s3', region_name='fra1', endpoint_url='https://fra1.digitaloceanspaces.com', aws_access_key_id=ACCESS_ID, aws_secret_access_key=SECRET_KEY)
    # Upload a file to your Space
    client.upload_file('Papers/'+paperDOI+'.pdf', 'aaronskit-cloudstorage', paperDOI+'.pdf',ExtraArgs={'ACL':'public-read', 'StorageClass':'REDUCED_REDUNDANCY'})

    #build article URL for insertion into articles table
    newArticleUrl = "https://aaronskit-cloudstorage.fra1.digitaloceanspaces.com/"+paperDOI+".pdf"
    ##### Create new article #####
    
    #Speak to remote aaronskit server to create a new entry to the articles table using the URL above and metadata
    newArticle = json
    with open("Metadata/"+paperDOI+".json", "r") as read_file:
        newArticle = json.load(read_file)
    authorCheck = checkAuthorExists(paperDOI)
    newAuthorID = None
    if (len(authorCheck)==0):
    #create new author
        authorQuery = """
        INSERT INTO Authors (AuthorInitial, AuthorSurname)
        VALUES
            ('"""+newArticle["AuthorInitial"]+"""','"""+newArticle["AuthorSurname"]+"""');
        """
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(authorQuery)
        conn.commit()
    else:
        authors = authorCheck[0]
        newAuthorID = authors["AuthorID"]    
    #check if journal exists. If yes, grab ID, if not, create new journal
    journalCheck = checkJournalExists(paperDOI)
    if (len(journalCheck)==0):
    #create new journal
        journalQuery = """
        INSERT INTO Journals (JournalName)
        VALUES
            ('"""+newArticle["JournalName"]+"""');
        """
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(journalQuery)
        conn.commit()
    else:
        journals = journalCheck[0]
        newJournalID = journals["JournalID"]

    #provide newJournalID with new value
    journalReCheck = checkJournalExists(paperDOI)
    print("journal recheck again")
    journals = journalReCheck[0]
    newJournalID = journals["JournalID"]

    #after creating a new journal and author, now create a new article
    articlesQuery = """
    INSERT INTO Articles (URL, Title, YearPublished, DOI, CategoryID, JournalID)
    VALUES
	    ('"""+newArticleUrl+"""','"""+newArticle["Title"]+"""',"""+newArticle["YearPublished"]+""",'"""+newArticle["DOI"]+"""',"""+newArticle["CategoryID"]+""","""+str(newJournalID)+""");
    """
    print(articlesQuery)      
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(articlesQuery)
    conn.commit()
    
    #check if article exists. If yes, grab ID
    replcaceSpacesTitle = replaceSpaces(newArticle["Title"])
    articleURL= remoteURL+"articles/check?titlecheck="+replcaceSpacesTitle
    newArticleID = None

    articleCheck = checkArticleExists(paperDOI)
    print(articleCheck)

    article = articleCheck[0]
    newArticleID = article["ArticleID"]


    #insert into Writes table
    writesQuery = """
    INSERT INTO Writes
    VALUES
	    ('"""+str(newArticleID)+"""','"""+str(newAuthorID)+"""')
    """
    print(writesQuery)         
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(writesQuery)
    conn.commit()
    results = cursor.fetchall()

    resp = jsonify(results)
    resp.status_code = 200

    return resp