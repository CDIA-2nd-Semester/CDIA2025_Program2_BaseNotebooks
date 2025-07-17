import joblib
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_iris

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

model_path = os.path.join(BASE_DIR, 'ml_model', 'model.pkl')

model= joblib.load(model_path)

target_names = load_iris().target_names


def predict_iris_species(features):
    pred= model.predict(np.array([features]).reshape(1, -1))[0]
    return target_names[pred]