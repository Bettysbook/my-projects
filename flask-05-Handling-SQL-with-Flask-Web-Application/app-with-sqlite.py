from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# - configure required environmental variables for SQLite
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./email.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


# Define the User model
class User(db.Model):
    username = db.Column(db.String, primary_key=True)
    email = db.Column(db.String)


# - Create the users table and insert sample data
def initialize_database():
    with app.app_context():
        db.create_all()

        # Insert sample data
        users = [
            User(username="Tuba", email="tuba@amazon.com"),
            User(username="Ethan", email="ethan@micrasoft.com"),
            User(username="Mostafa", email="mostafa@facebook.com"),
            User(username="Sait", email="sait@tesla.com"),
            User(username="Busra", email="busra@google")
        ]

        db.session.bulk_save_objects(users)
        db.session.commit()



initialize_database()


# - Write a function named `find_emails` which find emails using keyword from the user table in the db,
# - and returns result as tuples `(name, email)`.
def find_emails(keyword):
    query = """
    SELECT * FROM users WHERE username like :keyword;
    """
    result = db.session.execute(query, {"keyword": f"%{keyword}%"})
    user_emails = [(row[0], row[1]) for row in result]
    if not any(user_emails):
        user_emails = [("Not Found", "Not Found")]
    return user_emails

# - Write a function named `insert_email` which adds new email to users table the db.
def insert_email(name, email):
    query = """
    SELECT * FROM users WHERE username like :name
    """
    result
