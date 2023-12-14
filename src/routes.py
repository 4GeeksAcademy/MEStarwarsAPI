from flask import Flask, request, jsonify, url_for, Blueprint
from models import Planets, People, db
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET']) 
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200


@api.route('/people', methods=['POST']) 
def add_people():
    rb = request.get_json()  #request_body
    people = People (name=rb["name"], height=rb["height"], weight=rb["weight"])
    db.session.add(people)
    db.session.commit()
    return f"People {rb['name']} was added to our database"
