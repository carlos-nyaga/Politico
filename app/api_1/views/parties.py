from flask import jsonify, request, make_response
from app.api_1 import bp
import json
from app.api_1.models.parties_models import Parties



@bp.route('/parties', methods=['POST'])
def  create_party():
    data = request.get_json()
    party_name = data["name"]
    hq_address = data["hqAddress"]
    logo_url = data["logoUrl"]

    instance = Parties()
    created_party = instance.party_create(party_name, hq_address, logo_url)
    
    return make_response(jsonify({
        "status" : 201,
        "data" : [{
            "id" : created_party["party_id"],
            "name" : created_party["party_name"]
        }]    }))    


@bp.route('/parties' , methods =['GET'])
def get_parties():
    pass

    

@bp.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    pass


@bp.route('/parties/<int:id>', methods = ['PATCH'])
def edit_party(id):
    pass

@bp.route('parties/<int:id>', methods = ['DELETE'])
def delete_party(id):
    pass

