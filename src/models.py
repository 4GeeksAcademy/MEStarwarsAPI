from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email, 
            # do not serialize the password, its a security breach
        }
    
class People(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    height = db.Column(db.String(10), unique=False, nullable=False)
    weight = db.Column(db.String(10), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "height": self.height, 
            "weight": self.weight, 
        }




class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    rotaion_period = db.Column(db.String(10), unique=False, nullable=False)
    diameter = db.Column(db.String(10), unique=False, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name, 
            "rotaion_period": self.rotaion_period, 
            "diameter": self.diameter, 
        }
    

class Favorite(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    planet_id = db.Column(db.Integer, db.ForeignKey('planets.id'))
    people_id = db.Column(db.Integer, db.ForeignKey('people.id'))

    def serialize(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "planet_id": self.planet_id,
            "people_id": self.people_id
        }