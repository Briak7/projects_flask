import os
from flask import Flask, request, render_template, session, sessions
from flask.helpers import make_response
from werkzeug.utils import redirect
from werkzeug.wrappers import  response
app = Flask (__name__)
app.config["DEBUG"]="TRUE"
app.secret_key=os.urandom(2)
#debut
@app.route('/')
def hello():
    
    return render_template("index.html")

@app.route('/page2/')
def page2():
    if 'username' in session:
        return render_template("page2.html",user=session['username'])
    else:
        return render_template("page2.html")

@app.route('/next')
def next():
    username=request.cookies.get('username')
    return render_template("next.html", message=username)
@app.route('/cookies')
def pageCookies():
    response=make_response("<h1> Cette page crée des cookie")
    response.set_cookie('username', 'Bob')
    return response
@app.route('/', methods=['POST'])
def login():
    #form_user=request.form['username']
    session["username"]=request.form['username']
    #form_mdp=request.form['mdp']
    session["password"]=request.form['mdp']
    return redirect('page2') 

@app.route('/page2', methods=['POST'])
def signup():
    form_nom=request.form['nom']
    form_prenom=request.form['prenom']
    form_age=request.form['age']
    return render_template('next.html', nom=form_nom, prenom=form_prenom, age=form_age)     
@app.route('/page2')
def logout():
    session.pop('username',None)
    session.pop('password',None)
    session.clear()
    return render_template("page2.html")
if __name__=="__main__":
    app.run() 
