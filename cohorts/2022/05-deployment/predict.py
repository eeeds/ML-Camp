import pickle

from flask import Flask
from flask import request
from flask import jsonify


with open('models/model1.bin', 'rb') as f_in:
    model = pickle.load(f_in)
with open('models/dv.bin', 'rb') as f_in:
    dv = pickle.load(f_in)
app = Flask('churn')

@app.route('/predict', methods=['POST'])
def predict():
    customer = request.get_json()

    X = dv.transform([customer])
    y_pred = model.predict_proba(X)[0, 1]
    score = y_pred >= 0.5

    result = {
        'credit_card_probability': float(y_pred),
        'credit_card': bool(score)
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)