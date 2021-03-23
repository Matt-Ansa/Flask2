from flask import Flask, jsonify, request
from flask_cors import CORS

import PAYE

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/getNetIncome/', method=['POST'])
def netIncome():
    gross_income = request.get_json
    print(gross_income)
    gross = float(gross_income["gross_income"])
    return jsonify(gross - PAYE.totalTax(gross))

if __name__ == ' main ':
    app.run(host='0.0.0.0')

