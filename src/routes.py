from flask import Flask, request, jsonify, url_for, Blueprint, current_user, login_required
from models import Planets, People, User, Favorite, db
from utils import APIException


api = Blueprint('api', __name__)

@api.route('/test', methods=['GET']) 
def testAPI():
    return jsonify('YOUR API WORKS, CONGRATS'), 200



########################################## USERS ####################################

@api.route('/users', methods=['GET'])
def get_all_users():
    users = User.query.all()
    users_list = list(map(lambda user: user.serialize(), users))
    return jsonify(users_list), 200

@api.route('/users/favorites', methods=['GET'])
def get_user_favorites():
    
    current_user_id = current_user.id

    favorites = Favorite.query.filter_by(user_id=current_user_id).all()
    favorites_list = list(map(lambda favorite: favorite.serialize(), favorites))

    return jsonify(favorites_list), 200

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


@api.route('/favorite/people/<int:people_id>', methods=['POST'])
@login_required

def add_favorite_people(people_id):
    user_id = current_user.id

    people = People.query.get_or_404(people_id)
   
    if current_user.has_favorite_people(people_id):
        return jsonify({"error": "People already in favorites"}), 400

    new_favorite = Favorite(user_id=user_id, people_id=people_id)
    db.session.add(new_favorite)
    db.session.commit()

    response_body = {
        "msg": "People added to favorites successfully",
        "favorite": new_favorite.serialize()
    }

    return jsonify(response_body), 200


@api.route('/favorite/people/<int:people_id>', methods=['DELETE'])
@login_required
def delete_favorite_people(people_id):
    user_id = current_user.id

    people = People.query.get_or_404(people_id)
    favorite = Favorite.query.filter_by(user_id=user_id, people_id=people_id).first()
    if favorite is None:
        return jsonify({"error": "People not found in favorites"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify(f"Favorite people with ID {people_id} deleted successfully"), 200

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

@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
@login_required
def add_favorite_planet(planet_id):
    user_id = current_user.id

    
    planet = Planets.query.get_or_404(planet_id)

    if current_user.has_favorite_planet(planet_id):
        return jsonify({"error": "Planet already in favorites"}), 400

    new_favorite = Favorite(user_id=user_id, planet_id=planet_id)
    db.session.add(new_favorite)
    db.session.commit()

    response_body = {
        "msg": "Planet added to favorites successfully",
        "favorite": new_favorite.serialize()
    }

    return jsonify(response_body), 200


@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
@login_required
def delete_favorite_planet(planet_id):
    user_id = current_user.id

    planet = Planets.query.get_or_404(planet_id)

    favorite = Favorite.query.filter_by(user_id=user_id, planet_id=planet_id).first()
    if favorite is None:
        return jsonify({"error": "Planet not found in favorites"}), 404

    db.session.delete(favorite)
    db.session.commit()

    return jsonify(f"Favorite planet with ID {planet_id} deleted successfully"), 200






