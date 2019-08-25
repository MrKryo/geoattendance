from application import db
import models

rec = models.AttendanceRecord(email="Artensdfdfdffdfon@gmail.com")
db.session.add(rec)
db.session.commit()
