from app import db

class ToDo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task = db.Column(db.String(120), index=True, unique=True)

    def __repr__(self):
        return '<Task {}>'.format(self.task)