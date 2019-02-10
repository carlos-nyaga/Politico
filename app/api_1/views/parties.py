from flask import jsonify, request, make_response
from app.api_1 import bp
import json
from app.api_1.models.parties_models import Parties
from app.api_1.views.errors import bad_request, error_response
import re



@bp.route('/parties', methods=['POST'])
def  create_party():
    data = request.get_json() or {}
    db = Parties().parties
   

    if "name" not in data or "hqAddress" not in data or "logoUrl" not in data:
        return bad_request('must include name, hqAddress and logoUrl fields')
    
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["name"], data["hqAddress"], data["logoUrl"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["name"], data["hqAddress"], data["logoUrl"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["name"], data["hqAddress"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(map(lambda x: x["party_name"] == data["name"], db)):
        return bad_request('already in use....please use a different name')
    
    party_name = " ".join(str(data["name"]).split())
    hq_address = " ".join(str(data["name"]).split())
    logo_url = " ".join(str(data["name"]).split())

    instance = Parties()
    created_party = instance.party_create(party_name, hq_address, logo_url)
    
    return make_response(jsonify({
        "status" : 201,
        "data" : [{
            "id" : created_party["party_id"],
            "name" : created_party["party_name"]
        }]    }),201)    



@bp.route('/parties' , methods =['GET'])
def get_parties():
    parties_get = Parties()
    

    return make_response(jsonify({
        "status": 200,
        "data": parties_get.party_get()
    }))
  

    

@bp.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    party_get = Parties()
    if type(id) != int:
        return bad_request('Party ID needs to be of type int')
    elif id > len(party_get.parties):
        return error_response(404,'Sorry...Party not found!')

   
    return make_response(jsonify({
        "status" : 200,
        "data": party_get.party_get(id)

    }))


@bp.route('/parties/<int:id>', methods = ['PATCH'])
def edit_party(id):
    data = request.get_json() or {}

    if id > len(Parties().parties):
        return error_response(404,'Sorry...Party not found!')
    if "name" not in data:
            return bad_request('must include name field')
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["name"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["name"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["name"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(map(lambda x: x["party_name"] == data["name"], Parties().parties)):
        return bad_request('already in use....please use a different name')
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

