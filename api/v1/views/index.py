#!/usr/bin/python3
"""
    index.py file in v1/views
"""
from api.v1.views import app_views
from flask import Flask, jsonify


@app_views.route("/status")
def status_message():
    """
        method to return an OK status
    """
    return jsonify({"status": "OK"})
