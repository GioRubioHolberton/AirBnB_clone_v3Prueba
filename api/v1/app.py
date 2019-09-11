#!/usr/bin/python3
"""Module for Flask"""
from models import storage
from flask import Flask
from api.v1.views import app_views
from os import getenv


"""create a variable app""" 
app = Flask(__name__)
app.register_blueprint(app_views)


@app.errorhandler(404)
def page_not_found(e):
    """404 error returns a JSON file"""
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """ run Flask server"""
    host = getenv("HBNB_API_HOST", "0.0.0.0")
    port = getenv("HBNB_API_PORT", 5000)
    app.run(host, port, threaded=True)
