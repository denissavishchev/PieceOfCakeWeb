from flask import Flask, render_template, url_for, request, redirect, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


cake = Flask(__name__)
cake.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ingredients.db'
cake.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(cake)

class Ingredients(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    qty = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text, nullable=True)
    date = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Ingredients %r>' % self.id


@cake.route('/')
def index():
    return render_template('index.html')


@cake.route('/createIng', methods=['POST', 'GET'])
def createIng():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        qty = request.form['qty']
        comment = request.form['comment']

        ingredients = Ingredients(name=name, price=price, qty=qty, comment=comment)

        try:
            db.session.add(ingredients)
            db.session.commit()
            return redirect('/createIng')
        except:
            return 'Error'
    else:
        return render_template('createIng.html')


@cake.route('/ingList')
def ingList():
    ingredients = Ingredients.query.order_by(Ingredients.name).all()
    return render_template('ingList.html', ingredients=ingredients)


@cake.route('/ingList/<int:id>')
def ingListComment(id):
    ingComment = Ingredients.query.get(id)
    return render_template('ingComment.html', ingComment=ingComment)


@cake.route('/<name>')
def user(name):
    return 'Hello, ' + name

if __name__ == '__main__':
    cake.run(debug=True)