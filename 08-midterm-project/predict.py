import pickle

from flask import Flask
from flask import request
from flask import jsonify


model_file = 'models/model.pkl'
dv_file = 'models/dv.pkl'

with open(model_file, 'rb') as f_in:
    model = pickle.load(f_in)

with open(dv_file, 'rb') as f_in:
    dv = pickle.load(f_in)

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    music = request.get_json()

    X = dv.transform([music])
    y_pred = model.predict_proba(X)[0, 1]
    like = y_pred >= 0.5

    result = {
        'like_probability': float(y_pred),
        'like': bool(like)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True)