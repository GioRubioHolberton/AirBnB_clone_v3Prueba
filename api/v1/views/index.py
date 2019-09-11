#!/usr/bin/python3
"""Module"""
from models import storage
from api.v1.views import app_views
from flask import jsonify


all_objects = {"amenities": Amenity,
               "cities": City,
               "places": Place,
               "reviews": Review,
               "states": State,
               "users": User}


@app_views.route('/status')
def status():
    """status"""
    return jsonify({"status": "OK"})


@app_views.route('/stats')
def stats():
    """states to return"""
    dic = {}
    for key, value in all_objects.items():
        dic[key] = storage.count(value)
    return jsonify(dic)
