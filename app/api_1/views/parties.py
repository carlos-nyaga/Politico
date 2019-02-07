from flask import jsonify, request, make_response
from app.api_1 import bp
import json
from app.api_1.models.parties_models import Parties



@bp.route('/parties', methods=['POST'])
def  create_party():
    data = request.get_json()
    party_code = data["id"]
    party_name = data["name"]
    hq_address = data["hqAddress"]
    logo_url = data["logoUrl"]

    instance = Parties()
    created_party = instance.party_create(party_code, party_name, hq_address, logo_url)
    
    return make_response(jsonify({
        "status" : 201,
        "data" : [{
            "id" : created_party["party_id"],
            "name" : createdarty["party_name"]
        }]    }))    



@bp.route('/parties' , methods =['GET'])
def get_parties():
    parties_get = Parties()
    

    return make_response(jsonify({
        "status": 200,
        "data": parties_get.parties
    }))
  

    

@bp.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    party_get = Parties()
   
    return make_response(jsonify({
        "status" : 200,
        "data": party_get.party_get(id)

    }))


@bp.route('/parties/<int:id>', methods = ['PATCH'])
def edit_party(id):
    data = request.get_json() or {}
    name = data["name"]
    party_edit =Parties().party_edit(id,name)
    
    return make_response(jsonify({
        "status": 200,
        "data": party_edit
    }))

@bp.route('parties/<int:id>', methods = ['DELETE'])
def delete_party(id):
    party_delete = Parties().party_delete(id)
    return make_response(jsonify({
        "status": 200,
        "msg" : "Party deleted successfully"
    }))

