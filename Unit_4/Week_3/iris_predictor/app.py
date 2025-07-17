from flask import Flask, request, jsonify

from models import db, IrisPredictor

from predictor import predict_iris_species

import config

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = config.SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = config.SQLALCHEMY_TRACK_MODIFICATIONS


db.init_app(app)


# @app.before_first_request
# def create_tables():
#     db.create_all()


@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    features = [
        data["sepal_length"],
        data["sepal_width"],
        data["petal_length"],
        data["petal_width"],
    ]
    prediction = predict_iris_species(features)
    new_record = IrisPredictor(
        sepal_length=features[0],
        sepal_width=features[1],
        petal_length=features[2],
        petal_width=features[3],
        predicted_class=prediction,
    )

    db.session.add(new_record)
    db.session.commit()

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)
