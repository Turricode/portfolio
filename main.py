from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)


@app.get('/')
def index():
    return render_template('index.html')

@app.get('/api/graph_data')
def graph_data():

    with open('test.json', 'r') as fp:
        data = json.load(fp)

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)