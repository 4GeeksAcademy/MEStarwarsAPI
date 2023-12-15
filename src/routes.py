from flask import Flask, request, jsonify, url_for, Blueprint
from models import Planets, People, db
from utils import APIException

api = Blueprint('api', __name__)

@api.route('/test', methods=['GET']) 
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200

##########################################PEOPLE####################################

@api.route('/people', methods=['POST']) 
def add_people():
    rb = request.get_json()  #request_body
    people = People (name=rb["name"], height=rb["height"], weight=rb["weight"])
    db.session.add(people)
    db.session.commit()
    return f"People {rb['name']} was added to our database"


@api.route('/people', methods=['GET'])
def get_all_people():
    people = People.query.all()
    people_list = list(map(lambda People: People.serialize(), people ))
    return jsonify(people_list), 200
    
@api.route('/people/<int:people_id>', methods=['GET'])
def get_one_person(people_id):
    people = People.query.get_or_404(people_id)
    return jsonify(people.serialize())

@api.route('/people/<int:people_id>', methods=['PUT'])
def update_one_person(id):
    people = People.query.get_or_404(id)
    rb = request.get_json()
    if "name" in rb:
        people.name=rb["name"]
    if "height" in rb:
        people.height=rb["height"]
    if "weight" in rb:
        people.weight=rb["weight"]
    db.session.commit()
    return jsonify(people.serialize())


@api.route('/people/<int:people_id>', methods=['DELETE'])
def delete_one_person(people_id):
    people = People.query.get_or_404(people_id)
    db.session.delete(people)
    db.session.commit()
    return f"Person {people.name} was deleted", 200


##########################################PLANETS####################################

@api.route('/planets', methods=['POST']) 
def add_planets():
    rb = request.get_json()  #request_body
    planet = Planets (name=rb["name"], rotaion_period=rb["Rotaion period"], diameter=rb["Diameter"])
    db.session.add(planet)
    db.session.commit()
    return f"Planet {rb['name']} was added to our database"

@api.route('/planets', methods=['GET'])
def get_all_planets():
    planets = Planets.query.all()
    planets_list = list(map(lambda Planets: Planets.serialize(), planets ))
    return jsonify(planets_list), 200


@api.route('/planets/<int:planets_id>', methods=['GET'])
def get_one_planet(planets_id):
    planets = Planets.query.get_or_404(planets_id)
    return jsonify(planets.serialize())


@api.route('/planets/<int:planets_id>', methods=['PUT'])
def update_one_planet(id):
    planets = Planets.query.get_or_404(id)
    rb = request.get_json()
    if "name" in rb:
        planets.name=rb["name"]
    if "rotaion_period" in rb:
        planets.rotaion_period=rb["rotaion_period"]
    if "diameter" in rb:
        planets.diameter=rb["diameter"]
    db.session.commit()
    return jsonify(planets.serialize())


@api.route('/planets/<int:planets_id>', methods=['DELETE'])
def delete_one_planet(planets_id):
    planet = Planets.query.get_or_404(planets_id)
    db.session.delete(planet)
    db.session.commit()
    return f"Planet {planet.name} was deleted", 200






