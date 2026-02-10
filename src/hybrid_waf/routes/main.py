# Main route handlers

from flask import Flask, render_template, request, jsonify
from src.hybrid_waf.routes.proxy import process_request

app = Flask(__name__, template_folder='../../templates', static_folder='../../static')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/api/check', methods=['POST', 'GET'])
def api_check():
    """
    API endpoint to check if a request is malicious.
    """
    result = process_request(request)
    return jsonify(result)