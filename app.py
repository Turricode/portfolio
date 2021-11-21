from flask import Flask, render_template, jsonify, url_for
from gen_connections import gen_connections
import json

app = Flask(__name__)


@app.get('/')
def brain():
    return render_template('brain.html')

@app.get('/projects')
def  projects():
    return render_template('projects.html')

@app.get('/aboutme')
def about_me():
    return render_template('about.html')

@app.get('/contacts')
def contacts():
    return render_template('contacts.html')

@app.get('/api/graph_data')
def graph_data():
    return jsonify(gen_connections())

if __name__ == '__main__':
    app.run(debug=False)