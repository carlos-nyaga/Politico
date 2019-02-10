from flask import jsonify, request, make_response
from app.api_1 import bp
import json
from app.api_1.models.offices_models import Offices
from app.api_1.views.errors import bad_request, error_response

@bp.route('/offices', methods= ['POST'])
def create_office():
    data = request.get_json()
    db = Offices()
    if "name" not in data or "type" not in data:
        return bad_request('must include name and type fields')
    
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["name"], data["type"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["name"], data["type"]])):
        return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalnum() == False, [data["name"], data["type"]])):
        return bad_request('Only alphanumeric characters allowed')

    if any(map(lambda x: x["office_name"] == data["name"], db.offices)):
        return bad_request('already in use....please use a different name')

    office_name = " ".join(str(data["name"]).split())
    office_type = " ".join(str(data["type"]).split())

    
    created_office = db.office_create(office_type, office_name)
    
    
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
        "data" : Offices().office_get()
    }))

@bp.route('/offices/<int:id>', methods =['GET'])
def get_office(id):
    office = Offices()
    if not any(map(lambda x: x["office_id"] == id,office.offices)):
            return error_response(404,'Sorry...Office not found!')
    return make_response(jsonify({
        "status" : 200,
        "data" : office.office_get(id)
    }))