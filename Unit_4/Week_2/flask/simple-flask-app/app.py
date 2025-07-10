from flask import Flask, request, jsonify,render_template,Request
import joblib
import numpy as np

app = Flask(__name__)


@app . route ('/')
def home ():
    return render_template ('index.html ')

#model = joblib.load("iris_model.pkl")  # Trained scikit-learn model

#@app.route('/predict', methods=['POST'])
# def predict():
#     data = request.get_json()
#     features = [
#         data['sepal_length'],
#         data['sepal_width'],
#         data['petal_length'],
#         data['petal_width']
#     ]
#    #pred = model.predict([features])[0]
#     #return jsonify({"prediction": str(pred)})

if __name__ == "__main__":
    app.run(debug=True)
