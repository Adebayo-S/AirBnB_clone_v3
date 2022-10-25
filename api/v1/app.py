#!/usr/bin/python3
"""
    app.py to connect to API. app entry point
"""

import os
from models import storage
from api.v1.views import app_views
from flask import Flask


app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown(code):
    """
    teardown_appcontext method that closes the storage
    """
    storage.close()

@app.errorhandler(404)
def page_404_not_found(e):
    """method for 404 errors.
    """
    return ({'error': 'Not found'}), 404

if __name__ == "__main__":
    app.run(host=os.getenv('HBNB_API_HOST', '0.0.0.0'),
            port=int(os.getenv('HBNB_API_PORT', '5000')),
            threaded=True)
