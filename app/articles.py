import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/articles")
@cross_origin()
def getAvailableArticles():
    query = """
    SELECT URL, 
    Title, 
    YearPublished, 
    DOI, 
    JournalName, 
    AuthorInitial, 
    AuthorSurname FROM 
		(SELECT ArticleID, URL, 
		Title, YearPublished, DOI,
		JournalName FROM Articles 
		INNER JOIN 
		Journals ON 
        Articles.JournalID = Journals.JournalID) 
	AS New1 INNER JOIN 
		(SELECT ArticleID, AuthorInitial, 
        AuthorSurname FROM Writes AS W 
        INNER JOIN Authors AS A ON  
        W.AuthorID = A.AuthorID) 
	AS New2 ON New1.ArticleID = New2.ArticleID;
    """

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp

@app.route("/api/articles/title")
@cross_origin()
def getArticleByTitle():
    query_parameters = request.args
    search = query_parameters.get('title')
    
    query = """
    SELECT Title,
    YearPublished, 
    DOI, 
    URL, 
    JournalName, AuthorInitial, AuthorSurname FROM 
	    (SELECT Title,
        YearPublished,
        DOI,
        URL, JournalName, ArticleID 
        FROM Articles INNER JOIN 
        Journals ON Articles.JournalID = Journals.JournalID
        WHERE Title LIKE '%{}%')
    AS New1 INNER JOIN  
	    (SELECT ArticleID, AuthorInitial, AuthorSurname 
        FROM Writes AS W INNER JOIN Authors AS A 
        ON  W.AuthorID = A.AuthorID) 
    AS New2 ON New1.ArticleID = New2.ArticleID;
    """.format(
        search
    )
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp

@app.route("/api/articles/year")
@cross_origin()
def getArticlesbyYearRange():
    query_parameters = request.args
    startDate = query_parameters.get('startyearPublished')
    endDate = query_parameters.get('endyearPublished')

    query = """
    SELECT URL, 
    Title, 
    YearPublished, 
    DOI, AuthorInitial,
    AuthorSurname, JournalName FROM 
        (SELECT
        URL, 
        Title, 
        YearPublished, 
        DOI, AuthorInitial,
        AuthorSurname, JournalID
        FROM Articles INNER JOIN 
        Authors ON 
        Articles.ArticleID = Authors.AuthorID
        WHERE 
        YearPublished BETWEEN '{0}' AND '{1}'
        ORDER BY YearPublished DESC) 
    AS New1 INNER JOIN Journals 
    ON New1.JournalID = Journals.JournalID;
    """.format(
        startDate, endDate
    )

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)
    resp.status_code = 200

    return resp

@app.route("/api/articles/check")
@cross_origin()
def checkArticleByTitle():
    query_parameters = request.args
    search = query_parameters.get('titlecheck')
    
    query = """
    SELECT New1.ArticleID, Title,
    YearPublished,
    DOI,
    URL,
    JournalName, AuthorInitial, AuthorSurname FROM 
        (SELECT Title,
        YearPublished,
        DOI,
        URL, JournalName, ArticleID
        FROM Articles INNER JOIN Journals ON 
        Articles.JournalID = Journals.JournalID 
        WHERE Title = "{}") AS New1
    INNER JOIN 
        (SELECT ArticleID, 
        AuthorInitial, 
        AuthorSurname FROM Writes 
        AS W INNER JOIN Authors AS 
        A ON  W.AuthorID = A.AuthorID) 
    AS New2 ON New1.ArticleID = New2.ArticleID;
    """.format(
        search
    )

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)
    resp.status_code = 200

    return resp
