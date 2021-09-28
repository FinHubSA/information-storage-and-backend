from app import app
from flaskext.mysql import MySQL
import pymysql

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "root"
app.config["MYSQL_DATABASE_DB"] = "aarons_kit_backend"
app.config["MYSQL_DATABASE_HOST"] = "db"
mysql.init_app(app)
