from flask import Flask, render_template, redirect, url_for, request
from flask import g
from flask import session, flash 
from flask_bootstrap import Bootstrap
from flask.views import View
from functools import wraps
import sqlite3
import os
from os import listdir	



app = Flask(__name__)
app.secret_key="darisi"

@app.before_request
def before_request():
    g.db = sqlite3.connect("database_users.db")
	
@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
		g.db.close()


#login required decorator
def login_required(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			return f(*args,**kwargs)
		else:
			flash('You need to login first')
			return redirect(url_for('login'))
	return wrap

@app.route("/login", methods=['GET','POST'])
def login(): 
		error = None
		if request.method =='POST':
			if request.form['username'] != 'admin' or request.form['password'] != 'admin':
					error = 'invalid Credentials, please try again.'
			else:
				session['logged_in']= True
				flash("You were just logged in!   ")
				return redirect(url_for('main_account'))
		return render_template('Py-login.html', error= error)

		
@app.route("/logout")
def logout(): 
	session.pop('logged_in', None)
	flash('You were just logged out!   ')
	return redirect(url_for('login'))

	
@app.route("/signup")
def signup(): 
		return render_template('Py-signUP.html')
		
		
@app.route("/files")
@login_required
def files(): 
	path="C:/Users/Sumuu/Downloads"
	os.listdir(path)

@app.route("/account")
@login_required
def main_account(): 
	return render_template('acc.html')

@app.route("/banks")
@login_required
def myBanks(): 
	return render_template('banks.html')

@app.route("/identities")
@login_required
def myIdentities(): 
	return render_template('identities.html')
	
@app.route("/coupons")
@login_required
def myCoupons(): 
	return render_template('coupons.html')
	
	

@app.route("/docs")
@login_required
def myDocs(): 
	return render_template('docs.html')
			
@app.route("/home")
@login_required
def home(): 
	return render_template('home.html')

@app.route("/testing")
def testing(): 
	return render_template('testing.html')

@app.route("/pdf")
def testinggg(): 
	return render_template('pdf.php')

	
@app.route("/user/<name>/")
@login_required
def page(name): 
	return "<h2>hi %s!</h2>" %name

@app.route("/contact/")	
def contact(): 
	return render_template('forms.html')


@app.route("/test/")
def index1():
	user_agent = request.headers.get('User-Agent')
	return '<p>Your browser is %s</p>' % user_agent	

@app.route('/user/<int:post_id>')
def show_post(post_id):
	# show the post with the given id, the id is an integer
	return 'Post %d' % post_id	



if __name__ == "__main__":
    app.run(debug=True,port=8210)