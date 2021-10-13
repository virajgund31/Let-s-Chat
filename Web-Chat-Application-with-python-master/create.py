from flask import Flask
from models import *

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='postgres://legpmbyqsmtivd:d4f187b956288c8b4df6d2bffa7ed08abce493109374fe07ac5478e920984574@ec2-34-233-0-64.compute-1.amazonaws.com:5432/d2njbjpkgngs3q'
    #os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db.init_app(app)

def main():
    db.create_all()

if __name__ == "__main__":
    with app.app_context():
        main()
