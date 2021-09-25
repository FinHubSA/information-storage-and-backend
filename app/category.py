import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/api/category")
@cross_origin()
def getAvailableCategory():
    query_parameters = request.args
    category = query_parameters.get('categoryName')
    
    query = """
    SELECT A.Title, A.URL, A.DOI, A.YearPublished, J.JournalName, C.CategoryName FROM Articles 
    AS A, Journals AS J, Category AS C 
    WHERE  A.JournalID = J.JournalID AND A.CategoryID = C.CategoryID AND 
    C.CategoryName='{0}'
    ORDER BY A.YearPublished DESC;
    """.format(
        category
    )
    
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp