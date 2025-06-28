from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate')
def generate():
    number = random.randint(1, 10000)
    return jsonify({'number': number})

import os
app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5000)))
