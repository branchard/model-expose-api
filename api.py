from flask import Flask
import numpy as np

app = Flash('Taxi trip duration prediction')


@app.route('/endpoint', method=['POST'])
def root():
    payload = request.joson
    with open('./model.pkl', 'rb') as fp:
        model = pickle.load(fp)

    datapoint = np.array(payload['datapoint'])
    result = model.predict(datapoint.reshape(1, -1))
    return jsonify(result.tolist())
