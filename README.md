# -steptech_assignment
First, make sure you have Flask and the necessary dependencies installed. You can install Flask using pip:
pip install flask
Then, open Python file,  app.py
In this example, we're using Flask along with SQLAlchemy to connect to a MySQL database. Make sure to replace 'mysql://username:password@localhost/db_name' with your actual MySQL connection details.
You can run the Flask application by executing python app.py in your terminal. The application will start, and you can access the routes you defined:

/hello will display "Hello, World!".
/users will retrieve the list of users from the MySQL database and display them in an HTML table.
/new_user will render an HTML page with a form to accept user input and store the information in the database.
/users/<id> will retrieve the details of a specific user from the database and display them.
Error handling is implemented with a 404 error handler, which will return "Resource not found" when a route or resource is not found.
