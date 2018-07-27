import json
from flask import Flask, render_template, make_response, url_for, request

app = Flask(__name__)


@app.route('/')
def drawNodes():
    with open('saved_data.json', 'r') as f:
        data = json.load(f)

    return render_template('index.html', data = json.dumps(data))

@app.route('/receiveJSON', methods = ['POST'])
def receiveJSON():
    data = request.get_json()

    if data != None:
        with open('saved_data.json', 'w') as f:
            f.write(json.dumps(data, indent = 2))

    return json.dumps(data)

@app.route('/getJSON', methods = ['GET'])
def getJSON():
    with open('saved_data.json', 'r') as f:
        data = json.load(f)

    return json.dumps(data)

if __name__ == '__main__':
    app.run(debug = True, host = '127.0.0.1', port = 5000)
