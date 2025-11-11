bash
pip install flask sqlalchemy flask-sqlalchemy
from flask import Flask, request, redirect, url_for
from werkzeug.utils import secure_filename
import os
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Flask setup
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'pdf'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/database_name'
db = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
Session = sessionmaker(bind=db)
Base = declarative_base()

# SQLAlchemy model for storing file paths
class UploadedFile(Base):
    __tablename__ = 'uploadedfiles'
    id = Column(Integer, primary_key=True)
    filename = Column(String(100))
    filepath = Column(String(255))

# Initialize the database and create tables
Base.metadata.create_all(db)
session = Session()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload-pdf', methods=['POST'])
def upload_pdf():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '' or not allowed_file(file.filename):
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Save the file path in the database
        uploaded_file = UploadedFile(filename=filename, filepath=filepath)
        session.add(uploaded_file)
        session.commit()

        return "File successfully uploaded and saved to the database."

@app.route('/download-pdf/<int:id>')
def download_pdf(id):
    file = session.query(UploadedFile).filter_by(id=id).first()
    if not file:
        return "File not found.", 404
    return redirect(url_for('static', filename=file.filepath))

if __name__ == '__main__':
    app.run(debug=True)