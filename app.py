from flask import Flask
from flask_sqlalchemy import SQLAlchemy
  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employment_data.db'

db = SQLAlchemy(app)

class EmploymentData(db.Model):
    id = db.Column(db.Integer, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    company_name = db.Column(db.String(255), nullable=False)
    location = db.Column(db.String(255), nullable=False)
    via = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)
    schedule_type = db.Column(db.String(255), nullable=False)
    job_id = db.Column(db.Text, primary_key=True, nullable=False)


    def __repr__(self):
        return f"<employment_data {self.id} {self.title} {self.company_name}>"