import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/articles/authorsearch")
@cross_origin()
def getArticlebyAuthorSearch():
    query_parameters = request.args
    AuthorSearch = query_parameters.get('authorSurname')
    
    query = """
    SELECT 
    URL,
    Title,
    YearPublished,
    DOI, 
    AuthorInitial,
    AuthorSurname
    FROM Articles INNER JOIN Authors ON
    Articles.ArticleID = Authors.AuthorID
    WHERE Authors.AuthorSurname LIKE '%{}%'
    ORDER BY YearPublished DESC;
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