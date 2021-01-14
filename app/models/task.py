from app.extensions import db
from app.services.github import GitHub

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    done = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, done):
        self.name = name
        self.done = done

    def __repr__(self):
        return "<Task: {}>".format(self.username)
