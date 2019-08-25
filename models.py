from application import db
import datetime as dt


class AttendanceRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, unique=False, nullable=False)
    time = db.Column(db.Time, unique=False, nullable=False)
    email = db.Column(db.String(200), unique=False, nullable=False)
    date_time = db.Column(db.DateTime, unique=False, nullable=False)

    def __init__(self, email):
        self.email = email
        self.date = dt.datetime.now().date()
        self.time = dt.datetime.now().time()
        self.date_time = dt.datetime.now()
