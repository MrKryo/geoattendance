# the following line is used when the app is being deployed because it stores the uri of remote db server (aws)
 #SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://dhruvginni:artenson98@attendancedb.cjrrbjtusfar.us-east-2.rds.amazonaws.com:3306/myattendancedb.db'

# the following line is used for local testing. it contains the uri of local db. comment this line when deploying the app
SQLALCHEMY_DATABASE_URI = 'sqlite:///test.db'

SQLALCHEMY_POOL_RECYCLE = 3600

WTF_CSRF_ENABLED = True

# SECRET_KEY = 'ORS+LZn81XXKifgI1v++srZ82ot+6koOf4uPGTba'
# ACCESS_KEY_ID = 'AKIATZG3KLDHJPQL7DPA'
