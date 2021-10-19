import pymysql
from app import app
from db import mysql
from flask import jsonify, request
from flask_cors import cross_origin
import json
import urllib.request as requests


remoteURL = "https://api-aaronskit.org/api/"

@app.route("/api/articles")
@cross_origin()
def getAvailableArticles():
    query = """
    SELECT * FROM Articles
    """

    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    results = cursor.fetchall()

    resp = jsonify(results)

    resp.status_code = 200

    return resp

@app.route("/api/create-article", methods=["POST"])
@cross_origin()
def postArticle():
    newArticle = json
    with open("article.json", "r") as read_file:
        newArticle = json.load(read_file)
    query_parameters = request.args
    # articleID = query_parameters.get('ArticleID')
    # URL = query_parameters.get('URL')
    # Title = query_parameters.get('Title')
    # YearPublished = query_parameters.get('YearPublished')
    # CategoryID = query_parameters.get('CategoryID')
    # DOI = query_parameters.get('DOI')
    # JournalID = query_parameters.get('JournalID')
    # JournalName = query_parameters.get('JournalName')
    # AuthorSurname = query_parameters.get('AuthorSurname')    
    # JournalName = "American%20Economic%20Journal:%20Macroeconomics"
    # AuthorSurname = "Chen"
    # AuthorInitial = 'C'
    
    #check if journal exists, if not, create new journal
    # journalCheck = requests.urlopen(remoteURL+"articles/journal?journalName="+newArticle.JournalName).read()
    # print(journalCheck)
    # if (len(journalCheck)==0):
    # #create new journal
    #     journalQuery = """
    #     INSERT INTO Journals
    #     VALUES
    #         ("""+newArticle.JournalName+""");
    #     """         
    #     conn = mysql.connect()
    #     cursor = conn.cursor(pymysql.cursors.DictCursor)
    #     cursor.execute(journalQuery)
    #     conn.commit()

    #check if author exists, if not, create new author
    authorURL= remoteURL+"articles/author?authorSurname="+newArticle["AuthorSurname"]
    print(authorURL)
    authorCheck = requests.urlopen(authorURL).read()
    if (len(authorCheck)==0):
    #create new author
        journalQuery = """
        INSERT INTO Authors
        VALUES
            ("""+newArticle["AuthorInitial"]+""","""+newArticle["AuthorSurname"]+""");
        """
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute(journalQuery)
        conn.commit()
    
    #after creating a new journal and author, now create a new article
    articlesQuery = """
    INSERT INTO Articles
    VALUES
	    ("""+newArticle["ArticleID"]+""",'"""+newArticle["URL"]+"""','"""+newArticle["Title"]+"""',"""+newArticle["YearPublished"]+""","""+newArticle["CategoryID"]+""",'"""+newArticle["DOI"]+"""',"""+newArticle["JournalID"]+""");
    """
    print(articlesQuery)      
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(articlesQuery)
    conn.commit()
    
    #insert into Writes table
    writesQuery = """
    INSERT INTO Writes
    VALUES
	    (8,"""+newArticle["JournalID"]+""")
    """         
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(writesQuery)
    conn.commit()
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

