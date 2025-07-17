
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os



BASE_DIR = os.path.dirname(os.path.abspath(__file__))


iris= load_iris()
X = iris.data
y = iris.target


model= RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X, y)


save_dir = os.path.join(BASE_DIR, 'ml_model_2')
os.makedirs(save_dir, exist_ok=True)


joblib.dump(model, save_dir + '/model.pkl')