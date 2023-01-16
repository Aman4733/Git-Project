from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://root:1234@localhost:5432/postgres"

db = SQLAlchemy()

class MESSAGES(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80),  nullable=False)
    Message = db.Column(db.String(80),  nullable=False)
    Date = db.Column(db.String(120), nullable=False)

class Likes(db.Model):
    Sno = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(80),  nullable=False)
    Date = db.Column(db.String(120), nullable=False)

@app.route('/', methods = ['GET', 'POST'])
def message():
    if(request.method=='POST'):
        '''Add entry to the database'''
        name = request.form.get('name')
        message = request.form.get('message')
        entry = post(Name=name, Message = message, Date= datetime.now())
        db.session.add(entry)
        db.session.commit()
    return render_template('post.html')
    
if __name__ == '__main__':
   app.run(debug=True)