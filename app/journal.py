import pymysql
from flask import jsonify, request
from flask_cors import cross_origin

from app import app
from db import mysql


@app.route("/api/journals/titles")
@cross_origin()
def getAvailableJournals():
    query = """
    SELECT * FROM Journals
    """

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp


@app.route("/api/articles/journal")
@cross_origin()
def getSpecificArticlesfromJournals():
    query_parameters = request.args
    journal = query_parameters.get("journalName")

    query = """
    SELECT Title,
        URL,
        DOI,
        YearPublished,
        JournalName,
        CategoryName,
        AuthorInitial,
        AuthorSurname
    FROM
        (SELECT * FROM
            (SELECT A.ArticleID,
                    A.Title,
                    A.URL,
                    A.DOI,
                    A.YearPublished,
                    J.JournalName,
                    C.CategoryName
            FROM
                Articles AS A,
                Journals AS J,
                Category AS C
            WHERE A.JournalID = J.JournalID
            AND A.CategoryID = C.CategoryID
            ORDER BY A.YearPublished DESC)
        AS New_View)
    AS J_C_A
    INNER JOIN Authors
    ON J_C_A.ArticleID = Authors.AuthorID
    WHERE JournalName LIKE '%{}%'
    ORDER BY YearPublished DESC
    """.format(
        journal
    )

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp

@app.route("/api/journals/check")
@cross_origin()
def checkArticlebyJournalName():
    query_parameters = request.args
    search = query_parameters.get('checkjournal')

    query = """
    SELECT JournalID, JournalName
    FROM Journals
    WHERE JournalName ="{}";
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
