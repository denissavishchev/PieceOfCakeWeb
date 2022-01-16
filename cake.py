from flask import Flask, render_template, url_for,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


cake = Flask(__name__)
# cake.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'
# cake.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(cake)


@cake.route('/')
def index():
    return render_template('index.html')



if __name__ == '__main__':
    cake.run(debug=True)