#!/usr/bin/python3
"""
Start web aptication
"""
from api.v1.views import app_views
from models import storage
from flask import Flask, jsonify
from os import getenv


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def close(self):
    """
    Close session
    """
    storage.close()


@app.errorhandler(404)
def error_notfound(error):
    """ returns a JSON-formatted 404 status code response """
    return jsonify({"error": "Not found"}), 404


if __name__ == "__main__":
    """
    Start api
    """
    host = getenv('HBNB_API_HOST', '0.0.0.0')
    port = getenv('HBNB_API_PORT', '5000')
    app.run(host=host, port=port, threaded=True)
