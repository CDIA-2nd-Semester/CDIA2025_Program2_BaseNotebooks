from flask_sqlalchemy import SQLAlchemy

db= SQLAlchemy()


class IrisPredictor(db.Model):
    
    id= db.Column(db.Integer, primary_key=True)
    sepal_length = db.Column(db.Float)
    sepal_width = db.Column(db.Float)
    petal_length = db.Column(db.Float)
    petal_width = db.Column(db.Float)
    predicted_class  = db.Column(db.String(50))
