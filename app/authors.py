import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/articles/author")
@cross_origin()
def getArticlebyAuthor():
    query_parameters = request.args
    AuthorSearch = query_parameters.get('authorSurname')
    
    query = """
    SELECT URL,
    Title,
    YearPublished,
    DOI, 
    AuthorInitial,
    AuthorSurname, 
    JournalName
    FROM (SELECT 
ArticleID,
JournalID,
    URL,
    Title,
    YearPublished,
    DOI, 
    AuthorInitial,
    AuthorSurname
    FROM Articles INNER JOIN Authors ON
    Articles.ArticleID = Authors.AuthorID
    WHERE Authors.AuthorSurname Like '%{}%'
    ORDER BY YearPublished DESC) 
    AS New1 INNER JOIN Journals ON
    New1.JournalID = Journals.JournalID;
    """.format(
        AuthorSearch
    )
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp


@app.route("/api/author/check")
@cross_origin()
def checkArticlebyAuthor():
    query_parameters = request.args
    AuthorSurname = query_parameters.get('surname')
    AuthorInitial = query_parameters.get('initial')
    
    query = """
    SELECT AuthorID, 
    AuthorInitial,
    AuthorSurname FROM Authors 
    WHERE Authors.AuthorSurname = "{0}" 
    AND Authors.AuthorInitial = "{1}";
    """.format(
        AuthorSurname,AuthorInitial
    )
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp