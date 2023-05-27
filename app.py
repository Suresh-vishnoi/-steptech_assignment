from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/db_name'
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))


@app.route('/hello')
def hello():
    return 'Hello, World!'


@app.route('/users')
def users():
    user_list = User.query.all()
    return render_template('users.html', users=user_list)


@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user = User(name=name, email=email)
        db.session.add(user)
        db.session.commit()
        return 'User added successfully!'
    return render_template('new_user.html')


@app.route('/users/<int:id>')
def user_details(id):
    user = User.query.get(id)
    if user is None:
        return 'User not found'
    return render_template('user_details.html', user=user)


@app.errorhandler(404)
def not_found(error):
    return 'Resource not found', 404


if __name__ == '__main__':
    app.run()

