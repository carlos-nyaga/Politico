from flask import jsonify, request, make_response
from app.api_2 import bp2
import json
from app.api_2.models.candidate_models import Candidates
from app.api_2.views.errors import bad_request

@bp2.route('/office/<int:id>/register', methods=['POST'])
def register_candidate(id):
    data = request.get_json() or {}
    if "user_id" not in data or "party_id" not in data:
        return bad_request('must include user_id and party_id fields')

    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["user_id"], data["party_id"]])):
        return bad_request('Nice try...but no....we do not accept blanks')


    if any(map(lambda x: "".join(str(x).split()).isnumeric() == False, [data["user_id"], data["party_id"]])):
        return bad_request('Only numeric characters allowed')
    
    if any(Candidates().candidate_exists(data["user_id"])):
        return bad_request(' Candidate already exists....')

    userid = data["user_id"]
    partyid = data["party_id"]

    
    candidate = Candidates().candidate_create(id,partyid,userid)

    return make_response(jsonify({
        "status": 201,
        "msg" : "Candidate registered successfully!",
        "candidate":{
            "office_id":candidate[0],
            "candidate_id": candidate[1]
        }
    }))

