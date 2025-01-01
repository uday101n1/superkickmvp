# # from flask import Flask, request, jsonify,render_template  # Ensure request and jsonify are imported
# # from flask_sqlalchemy import SQLAlchemy
# # from datetime import datetime, timezone


# # db = SQLAlchemy()
# # # Initialize the Flask app and configure it
# # app = Flask(__name__)
# # app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:data/data.db'
# # print(app.config['SQLALCHEMY_DATABASE_URI'])
# # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# # # Initialize SQLAlchemy
# # db = SQLAlchemy(app)

# # @app.route('/')
# # def home():
# #     return render_template('index.html')  # Render the index.html file from the templates folder

# # # Define your models
# # class Submission(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     name = db.Column(db.String(100), nullable=False)
# #     iam_input = db.Column(db.String(200), nullable=False)
# #     looking_for = db.Column(db.String(200), nullable=False)
# #     email = db.Column(db.String(100), nullable=False)
# #     #timestamp = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc))  # Use timezone-aware datetime
    

# # class JoinRequest(db.Model):
# #     id = db.Column(db.Integer, primary_key=True)
# #     submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
# #     name = db.Column(db.String(100), nullable=False)
# #     social_media = db.Column(db.String(200), nullable=True)
# #     email = db.Column(db.String(100), nullable=False)

# # # Create the database tables within the app context
# # with app.app_context():
# #     db.create_all()  # Ensures tables are created before running the app



# # # Define other routes
# # @app.route('/submit', methods=['POST'])
# # def submit():
# #     data = request.json
# #     new_submission = Submission(
# #         name=data['name'],
# #         iam_input=data['iam_input'],
# #         looking_for=data['looking_for'],
# #         email=data['email']
# #     )
# #     db.session.add(new_submission)
# #     db.session.commit()
# #     return jsonify({'message': 'Submission added successfully'})

# # @app.route('/get_submissions', methods=['GET'])
# # def get_submissions():
# #     submissions = Submission.query.all()
# #     return jsonify([
# #         {'id': sub.id, 'name': sub.name, 'iam_input': sub.iam_input, 'looking_for': sub.looking_for}
# #         for sub in submissions
# #     ])

# # @app.route('/join', methods=['POST'])
# # def join():
# #     data = request.json
# #     new_join = JoinRequest(
# #         submission_id=data['submission_id'],
# #         name=data['name'],
# #         social_media=data.get('social_media'),
# #         email=data['email']
# #     )
# #     db.session.add(new_join)
# #     db.session.commit()
# #     return jsonify({'message': 'Join request successful'})

# # with app.app_context():
# #     db.create_all()

# # # Run the app
# # import os
# # print("Database file location:", os.path.abspath('data.db'))

# # if __name__ == '__main__':
# #     app.run(debug=True)
# import os
# from flask import Flask, request, jsonify, render_template
# from flask_sqlalchemy import SQLAlchemy
# from datetime import datetime

# # Initialize the Flask app and configure it
# app = Flask(__name__)
# # Ensure the 'instance' directory exists
# db_path = os.path.join(os.path.dirname(__file__), '/data')
# if not os.path.exists(db_path):
#     os.makedirs(db_path)

# # Corrected database URI using absolute path
# app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_path, "data.db")}'

# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# # Initialize SQLAlchemy
# db = SQLAlchemy(app)

# app = Flask(__name__, template_folder='FrontEnd')  # Specify the folder containing templates

# @app.route('/')
# def home():
#     return render_template('index.html')  # Ensure templates/index.html exists

# # Define your models
# class Submission(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(100), nullable=False)
#     iam_input = db.Column(db.String(200), nullable=False)
#     looking_for = db.Column(db.String(200), nullable=False)
#     email = db.Column(db.String(100), nullable=False)
#     timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Use UTC timestamp

# class JoinRequest(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
#     name = db.Column(db.String(100), nullable=False)
#     social_media = db.Column(db.String(200), nullable=True)
#     email = db.Column(db.String(100), nullable=False)

# # Create the database tables within the app context
# with app.app_context():
#     db.create_all()

# # Define other routes
# @app.route('/submit', methods=['POST'])
# def submit():
#     try:
#         data = request.json
#         new_submission = Submission(
#             name=data['name'],
#             iam_input=data['iam_input'],
#             looking_for=data['looking_for'],
#             email=data['email']
#         )
#         db.session.add(new_submission)
#         db.session.commit()
#         return jsonify({'message': 'Submission added successfully'}), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# @app.route('/get_submissions', methods=['GET'])
# def get_submissions():
#     submissions = Submission.query.all()
#     return jsonify([
#         {
#             'id': sub.id,
#             'name': sub.name,
#             'iam_input': sub.iam_input,
#             'looking_for': sub.looking_for,
#             'email': sub.email,
#             'timestamp': sub.timestamp.strftime('%Y-%m-%d %H:%M:%S')
#         }
#         for sub in submissions
#     ])

# @app.route('/join', methods=['POST'])
# def join():
#     try:
#         data = request.json
#         new_join = JoinRequest(
#             submission_id=data['submission_id'],
#             name=data['name'],
#             social_media=data.get('social_media'),
#             email=data['email']
#         )
#         db.session.add(new_join)
#         db.session.commit()
#         return jsonify({'message': 'Join request successful'}), 201
#     except Exception as e:
#         return jsonify({'error': str(e)}), 400

# # Run the app
# if __name__ == '__main__':
#     import os
#     # Debug SQLite file location
#     print("Database file location:", os.path.abspath('data\data.db'))
#     app.run(debug=True)
import os
from flask import Flask, request, jsonify, render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the Flask app and configure it
app = Flask(__name__)  # Specify the folder containing templates

# Ensure the 'instance' directory exists
db_path = os.path.join(os.path.dirname(__file__), 'data')
if not os.path.exists(db_path):
    os.makedirs(db_path)

# Corrected database URI using absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(db_path, "data.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

@app.route('/')
def home():
    return render_template('index.html')  # Ensure templates/index.html exists

# Define your models
class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    iam_input = db.Column(db.String(200), nullable=False)
    looking_for = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)  # Use UTC timestamp

class JoinRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    submission_id = db.Column(db.Integer, db.ForeignKey('submission.id'), nullable=False)
    name = db.Column(db.String(100), nullable=False)
    social_media = db.Column(db.String(200), nullable=True)
    email = db.Column(db.String(100), nullable=False)

# Create the database tables within the app context
with app.app_context():
    db.create_all()

# Define other routes
@app.route('/submit', methods=['POST'])
def submit():
    try:
        data = request.json
        new_submission = Submission(
            name=data['name'],
            iam_input=data['iam_input'],
            looking_for=data['looking_for'],
            email=data['email']
        )
        db.session.add(new_submission)
        db.session.commit()
        return jsonify({'message': 'Submission added successfully'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/get_submissions', methods=['GET'])
def get_submissions():
    submissions = Submission.query.all()
    return jsonify([
        {
            'id': sub.id,
            'name': sub.name,
            'iam_input': sub.iam_input,
            'looking_for': sub.looking_for,
            'email': sub.email,
            'timestamp': sub.timestamp.strftime('%Y-%m-%d %H:%M:%S')
        }
        for sub in submissions
    ])

@app.route('/join', methods=['POST'])
def join():
    try:
        data = request.json
        new_join = JoinRequest(
            submission_id=data['submission_id'],
            name=data['name'],
            social_media=data.get('social_media'),
            email=data['email']
        )
        db.session.add(new_join)
        db.session.commit()
        return jsonify({'message': 'Join request successful'}), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 400

print("Database file location:", os.path.abspath('data.db'))
# Run the app
if __name__ == '__main__':
    import os
    # Debug SQLite file location
    print("Database file location:", os.path.abspath('data/data.db'))
    app.run(debug=True)
