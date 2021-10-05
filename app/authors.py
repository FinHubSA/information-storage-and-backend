import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/articles/author")
@cross_origin()
def getArticlebyAuthorSearch():
    query_parameters = request.args
    AuthorSearch = query_parameters.get('authorSurname')
    
    query = """
    SELECT 
    A.URL,
    A.Title, 
    A.YearPublished, 
    A.DOI, 
    P.AuthorSurname 
    FROM
    Articles AS A,
    (SELECT W.ArticleID, 
    AuthS.AuthorSurname 
    FROM Writes AS W, 
	    (SELECT AuthorID, 
        AuthorSurname FROM Authors 
        WHERE AuthorSurname LIKE '%{}%')
    AS AuthS WHERE W.AuthorID = AuthS.AuthorID
    )
    AS P WHERE P.ArticleID = A.ArticleID
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