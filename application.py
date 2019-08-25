from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
import logging
import models
application = Flask(__name__)
application.config.from_object('config')
application.debug = True
db = SQLAlchemy(application)


@application.route("/")
def main():
    return render_template('index.html')


@application.route("/mark_attendance", methods=['POST'])
def mark_attendance():
    isInArea = request.form.get('isInArea')
    email = request.form.get('email')
    if not isInArea:
        return "Not In Area. Exiting!"

    record = models.AttendanceRecord(email=email)
    db.session.add(record)
    db.session.commit()
    return "Successfully added record in the database"


@application.route("/getrecords", methods=['GET'])
def get_records():
    records = models.AttendanceRecord.query.all()
    application.logger.info(records)
    return render_template("records.html", records=records)


if __name__ == "__main__":
    application.run()

