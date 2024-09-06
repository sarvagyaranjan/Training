from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///users.db"
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)  # Increased length for hashed passwords

@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')

        # Check if both username and password are provided
        if username and password:
            # Create a new User object
            new_user = User(username=username, password=password)
            
            # Add the user to the session and commit
            db.session.add(new_user)
            db.session.commit()
            # return "User added successfully!"  # Provide feedback or redirect

        else:
            # Handle missing data case
            return username == None, 400

    return render_template('index.html')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True, port=8000)
