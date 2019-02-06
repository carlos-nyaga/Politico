from flask import jsonify, request, make_response
from app.api_1 import bp
import json
from app.api_1.models.offices_models import Offices

@bp.route('/offices', methods= ['POST'])
def create_office():
    data = request.get_json()
    office_name = data["name"]
    office_type = data["type"]

    instance = Offices()
    created_office = instance.office_create(office_type, office_name)
    
    return make_response(jsonify({
        "status" : 201,
        "data" : [{
            "id" : created_office["office_id"],
            "type": created_office["office_type"],
            "name" : created_office["office_name"]
        }]    })) 


@bp.route('/offices', methods =['GET'])
def get_offices():
    return make_response(jsonify({
        "status" : 200,
        "data" : Offices().offices
    }))

@bp.route('/offices/<int:id>', methods =['GET'])
def get_office(id):
    pass