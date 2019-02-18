from flask import jsonify, request, make_response
from app.api_2 import bp2
import json
from app.api_2.models.party_models import Parties
from app.api_2.views.errors import bad_request, error_response


@bp2.route('/parties', methods=['POST'])
def  create_party():
    data = request.get_json() or {}
    db = Parties()

    if "party_name" not in data or "hqAddress" not in data or "logoUrl" not in data:
        return bad_request('must include party_name, hqAddress and logoUrl fields')
    
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["party_name"], data["hqAddress"], data["logoUrl"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["party_name"], data["hqAddress"], data["logoUrl"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["party_name"], data["hqAddress"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(db.party_name_exists(data["party_name"])):
        return bad_request(' already in use....please use a different name')

    
    party_name = " ".join(str(data["party_name"]).split())
    hq_address = " ".join(str(data["hqAddress"]).split())
    logo_url = " ".join(str(data["logoUrl"]).split())

    created_party = db.party_create(party_name, hq_address, logo_url)
    
    return make_response(jsonify({
        "status" : 201,
        "party" : [{
            "party_id" : created_party[0],
            "party_name" : created_party[1]
        }]    }),201)    



@bp2.route('/parties' , methods =['GET'])
def get_parties():
    parties_get = Parties()
    

    return make_response(jsonify({
        "status": 200,
        "parties": parties_get.party_get()
    }))
  

    

@bp2.route('/parties/<int:id>', methods=['GET'])
def get_party(id):
    party_get = Parties()
    if not any(party_get.party_exists(id)):
        return error_response(404,'Sorry...Party not found!')

   
    return make_response(jsonify({
        "status" : 200,
        "party": party_get.party_get(id)

    }))


@bp2.route('/parties/<int:id>', methods = ['PATCH'])
def edit_party(id):
    data = request.get_json() or {}
    db = Parties()

    if not any(db.party_exists(id)):
        return error_response(404,'Sorry...Party not found!')
    if "party_name" not in data:
            return bad_request('must include party_name field')
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["party_name"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["party_name"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["party_name"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(db.party_name_exists(data["party_name"])):
        return bad_request('already in use....please use a different name')
    name = data["party_name"]
    party_edit = db.party_edit(id, name)
    
    return make_response(jsonify({
        "status": 200,
        "party": party_edit
    }))

@bp2.route('parties/<int:id>', methods = ['DELETE'])
def delete_party(id):
    db = Parties()
    if not any(db.party_exists(id)):
        return bad_request('Sorry...Party not found!')
    db.party_delete(id)
    return make_response(jsonify({
        "status": 200,
        "msg" : "Party deleted successfully"
    }))

