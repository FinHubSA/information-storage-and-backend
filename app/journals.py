import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin


@app.route("/journals")
@cross_origin()
def getAvailableJournals():
    query = """
    SELECT *
    FROM `Journals`
    """

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp