from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import models
application = Flask(__name__)
application.config.from_object('config')
application.debug = True
db = SQLAlchemy(application)


# admin credentials
admin_email = "dhruv@gmail.com"
admin_pass = "123"

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


@application.route("/clear", methods=['GET','POST'])
def clear_db():
    # application.logger.info()
    # redirect('/getrecords')
    number =db.session.query(models.AttendanceRecord).delete()
    db.session.commit()
    return redirect('/getrecords')


@application.route("/admin", methods=['GET','POST'])
def show_admin():
    return render_template('admin.html')


@application.route("/validate", methods=['POST'])
def validate():
    email = request.form['email']
    password = request.form['pass']

    if email == admin_email and admin_pass == password:
        return redirect('/getrecords')
    else:
        return render_template('error.html')


if __name__ == "__main__":
    application.run()

