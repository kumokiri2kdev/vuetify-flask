from flask import Flask, request, jsonify, make_response
from flask_cors import CORS
import json

app = Flask(__name__, static_folder='.')
app.config["JSON_AS_ASCII"] = False
CORS(app)

data = {
    'data_a': [
        100, 200, 300
    ],
    'data_b': [
        {
            'key': '001',
            'title': 'データ001'
        },
        {
            'key': '002',
            'title': 'データ002'
        },
        {
            'key': '003',
            'title': 'データ003'
        }
    ]
}

data_base = {
    '001': 'アフリカ支援に官民4兆円　首相「人への投資」表明',
    '002': '24時間テレビ　今年のチャリTシャツはなぜ売れていないのか',
    '003': '二階俊博「自民党はビクともしない」統一教会問題で国民感情逆撫で'
}

memo = {}

@app.route('/geta', methods=['GET', 'OPTIONS'])
def get_a():
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""


    response_message = data['data_a']
    response = make_response(jsonify(response_message))

    return response

@app.route('/getb', methods=['GET', 'OPTIONS'])
def get_b():
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""


    response_message = data['data_b']
    response = make_response(jsonify(response_message))

    return response

@app.route('/getbd/<key>', methods=['GET', 'OPTIONS'])
def get_b_detail(key):
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""


    response_message = data_base[key]
    response = make_response(jsonify(response_message))

    return response

@app.route('/memo', methods = ['POST', 'OPTIONS'])
def put_memo():
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""

    body = request.get_data().decode('utf-8')
    print(body)
    json_data = json.loads(body)
    print(json_data)
    memo[json_data['key']] = json_data['memo']

    return ""

@app.route('/getmemo/<key>', methods=['GET', 'OPTIONS'])
def get_memo(key):
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""

    res = ''
    if key in memo:
        res = memo[key]

    return res

@app.route('/form', methods = ['POST', 'OPTIONS'])
def post_form():
    if request.method == "OPTIONS":
        print('OPTIONS')
        return ""

    body = request.get_data().decode('utf-8')
    print(body)
    json_data = json.loads(body)
    print(json_data)

    return ""

if __name__ == '__main__':
    app.run(host='0.0.0.0')
