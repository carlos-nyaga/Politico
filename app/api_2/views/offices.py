from flask import jsonify, request, make_response
from app.api_2 import bp2
import json
from app.api_2.models.offices_models import Offices
from app.api_2.views.errors import bad_request, error_response

@bp2.route('/offices', methods= ['POST'])
def create_office():
    data = request.get_json() or {}
    db = Offices()
    if "office_name" not in data or "office_type" not in data:
        return bad_request('must include office_name and office_type fields')
    
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["office_name"], data["office_type"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["office_name"], data["office_type"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["office_name"], data["office_type"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(db.name_exists(data["office_name"])):
        return bad_request(' already in use....please use a different name')

    office_name = " ".join(str(data["office_name"]).split())
    office_type = " ".join(str(data["office_type"]).split())

    
    created_office = db.office_create(office_name, office_type)
    
    
    return make_response(jsonify({
        "status" : 201,
        "office" : [{
            "office_id" : created_office[0],
            "office_type": created_office[1],
            "office_name" : created_office[2]
        }]    })) 


@bp2.route('/offices', methods =['GET'])
def get_offices():
    return make_response(jsonify({
        "status" : 200,
        "offices" : Offices().office_get()
    }))

@bp2.route('/offices/<int:id>', methods =['GET'])
def get_office(id):
    office = Offices()
    if not any(office.office_exists(id)):
        return bad_request('Sorry...Party not found!')
    return make_response(jsonify({
        "status" : 200,
        "office" : office.office_get(id)
    }))