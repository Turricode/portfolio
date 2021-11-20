from flask import Flask, render_template, jsonify, url_for
from gen_connections import gen_connections, load_node_info
import json

app = Flask(__name__)


@app.get('/')
def brain():
    return render_template('brain.html')

@app.get('/projects')
def  projects():
    return render_template('projects.html')

@app.get('/api/graph_data')
def graph_data():
    return jsonify(gen_connections())

@app.get('/api/node_data/<node_name>')
def node_data(node_name):
    return load_node_info(node_name)

if __name__ == '__main__':
    app.run(debug=True)