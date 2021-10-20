import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin

@app.route("/api/articles/doi")
@cross_origin()
def checkArticlebyDOI():
    query_parameters = request.args
    search = query_parameters.get('checkdoi')

    query = """
    SELECT ArticleID,DOI
    FROM Articles
    WHERE DOI ="{}";
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

