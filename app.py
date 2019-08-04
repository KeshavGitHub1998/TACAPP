from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
#import bcrypt
from werkzeug.utils import escape
from werkzeug.http import HTTP_STATUS_CODES

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = '77st3uGD1t'
app.config['MYSQL_PASSWORD'] = 'fIAV9GlmFB'
app.config['MYSQL_DB'] = '77st3uGD1t'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

#template should be changed for the home page
@app.route('/')
def main():
	return render_template("abcd.html")

@app.route('/home')
def home():
	return render_template("home.html")



@app.route('/register', methods=["GET", "POST"])
def register():
	if request.method == 'GET':
		return render_template("register.html")
	else:
		name = request.form['name']
		eno = request.form['eno']
		dept = request.form['dept']
		course = request.form['course']
		spec = request.form['spec']
		phno = request.form['phno']
		email = request.form['email']
		school = request.form['school']
		city = request.form['city']
		state = request.form['state']
		semester = request.form['semester']
		blood = request.form['blood']
		os = request.form['os']
		stay = request.form['stay']
		bachelor = request.form['bachelor']
		college = request.form['college']
		#password = request.form['password']
		password = request.form['password'].encode('utf-8')
		#hash_password = hashpw(password, gensalt())
		#hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

		cur = mysql.connection.cursor()
		cur.execute("INSERT INTO users (name, eno, dept, course, spec, phno, school, city, state, semester, blood, os, stay, bachelor, college, email, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(name, eno, dept, course, spec, phno, school, city, state, semester, blood, os, stay, bachelor, college, email, password,))
		mysql.connection.commit()
		session['name'] = request.form['name']
		session['email'] = request.form['email']
		return redirect(url_for('home'))

@app.route('/login',methods=["GET","POST"])
def login():
	if request.method == 'POST':
		email = request.form['email']
		password = request.form['password']

		curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		curl.execute("SELECT * FROM users WHERE email=%s",(email,))
		user = curl.fetchone()
		curl.close()

		if len(user) > 0:
			if password == user["password"]:
			#bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
				session['name'] = user['name']
				session['email'] = user['email']
				return render_template("home.html")
			else:
				return "Error password and email not match"
		else:
			return "Error user not found"
	else:
		return render_template("login.html")

@app.route('/logout')
def logout():
	session.clear()
	return render_template("abcd.html")


@app.route('/ambasdors')
def ambasdors():
	return render_template("ambasdors.html")

@app.route('/teamheads')
def teamheads():
	return render_template("teamheads.html")

if __name__ == '__main__':
	app.secret_key = "7222871686"
	app.run(debug=True)
	#this line is to be changed while deploying
	#app.run(host='0.0.0.0', port=5000)

'''import mysql.connector

mydb = mysql.connector.connect(
  host="remotemysql.com",
  user="77st3uGD1t",
  passwd="fIAV9GlmFB",

)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")


for x in mycursor:
	print(x)'''