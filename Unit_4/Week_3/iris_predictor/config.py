import os 

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

#print(f"Base directory for configuration: {BASE_DIR}")

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'iris.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False
