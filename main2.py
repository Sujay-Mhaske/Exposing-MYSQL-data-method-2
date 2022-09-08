from flask import *
import mysql.connector

app = Flask(__name__)
mydb = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Sujya999$',
    port='3306',
    autocommit=True,
)
mycursor = mydb.cursor()


@app.route('/', methods=['GET', 'POST'])
def home():
    mycursor.execute("SHOW DATABASES")
    data = [i[0] for i in mycursor.fetchall()]
    return render_template("index.html", data=data)


@app.route('/<string:database>', methods=['GET', 'POST'])
def database(database):
    mycursor.execute("USE {}".format(database))
    mycursor.execute("SHOW TABLES FROM {}".format(database))
    data = [i[0] for i in mycursor.fetchall()]
    return render_template("index2.html", data=data, database=database)


@app.route('/<string:database>/<string:tables>', methods=['GET', 'POST'])
def tabledata(database, tables):
    mycursor.execute("USE {}".format(database))
    mycursor.execute("SELECT * FROM {}".format(tables))
    data = mycursor.fetchall()
    return render_template("index3.html", data=data)


if __name__ == '__main__':
    app.run(debug=True)