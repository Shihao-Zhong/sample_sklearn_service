from flask import Flask, request
import pickle
from flask_cors import CORS


app = Flask(__name__)
CORS(app)
model = pickle.load(open('model.pkl', 'rb'))


@app.route('/predictions', methods=['POST'])
def predictions():
    body = request.json

    prediction = [[float(body["sepalLength"]),
          float(body["sepalWidth"]),
          float(body["petalLength"]),
          float(body["petalWidth"])]]

    res = model.predict(prediction)
    iris_type = ["Setosa", "Versicolour", "Vrginica"]

    return {"result": iris_type[res[0]]}


if __name__ == "__main__":
    app.run(debug=True)