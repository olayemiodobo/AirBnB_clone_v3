#!/usr/bin/python3
""" the blueprint"""
from api.v1.views import app_views
from flask import jsonify
from models import storage


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """ return the status"""
    return jsonify({"status": "ok"})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """an endpoint that retrieves the number of each objects by type:"""
    return jsonify(amenities=storage.count('Amenity')
                   cities=storage.count("City")
                   places=storage.count("Place")
                   reviews=storage.count("Review")
                   states=storge.count("State")
                   users=storage.count("User"))
