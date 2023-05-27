from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

@app.route('/users')
def users():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host='localhost',
        user='your_username',
        password='your_password',
        database='your_database'
    )
    cursor = db.cursor()

    # Fetch users from the database
    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    # Close the database connection
    cursor.close()
    db.close()

    # Render the users.html template with the user data
    return render_template('users.html', users=users)

if __name__ == '__main__':
    app.run()
