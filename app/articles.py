import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/articles")
@cross_origin()
def getAvailableArticles():
    query = """
    SELECT Title, YearPublished, DOI, URL FROM Articles
    """

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp

@app.route("/api/articles/titlesearch")
@cross_origin()
def getArticlebyTitleSearch():
    query_parameters = request.args
    search = query_parameters.get('title')
    
    query = """
    SELECT Title,
    YearPublished,
    DOI,
    URL
    FROM Articles
    WHERE Title LIKE '%{}%'
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

@app.route("/api/articles/yearsearch")
@cross_origin()
def getArticlesbyYearRange():
    query_parameters = request.args
    startDate = query_parameters.get('startyearPublished')
    endDate = query_parameters.get('endyearPublished')

    query = """
    SELECT
    URL, 
    Title, 
    YearPublished, 
    DOI, 
    AuthorSurname
    FROM Articles INNER JOIN 
    Authors ON 
    Articles.ArticleID = Authors.AuthorID
    WHERE 
    YearPublished BETWEEN '{0}' AND '{1}'
    ORDER BY YearPublished DESC

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

