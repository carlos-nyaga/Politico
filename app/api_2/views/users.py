from flask import jsonify, make_response, request
from app.api_2 import bp2
import json
from app.api_2.models.user_models import Users
from app.api_2.views.errors import bad_request, error_response

@bp2.route('/auth/signup', methods = ['POST'])
def create_user():
    user = Users()
    data = request.get_json() or {}
    fields = ["first_name", "last_name", "other_name","email", "phone_number", "passport_url", "password", "isadmin"]
    for field in fields:
        if field not in data:
            return bad_request('missing or invalid data field(s)')
        
        elif any(map(lambda x: len("".join(str(x).split())) < 1, [data[field]])):
            return bad_request('Nice try...but no....we do not accept blanks')
        
        elif any(map(lambda x: len("".join(str(x).split())) < 3, [data[field]])):
            return bad_request('minimum length should be 3 characters long')

    if any(map(lambda x: "".join(str(x).split()).isalpha() == False, [data["first_name"], data["last_name"],data["other_name"]])):
            return bad_request("Only alphabets allowed in names")


    fname = data['first_name']
    lname = data['last_name']
    oname = data['other_name']
    email = data['email']
    phoneNo = data['phone_number']
    passport = data['passport_url']
    password = data['password']
    isadmin = data['isadmin']

    created_user = user.user_create(fname, lname, oname, email, phoneNo, passport,password, isadmin)


    return make_response(jsonify({
       "status" : 201,
        "user" : [{
            "token": user.auth_token_encode(created_user[0]),
            "user" : user.to_dict(created_user)
        }]
        }),201)


@bp2.route('/auth/login', methods = ['POST'])
def login():
    user = Users()
    data = request.get_json() or {}
    if "password" not in data or "email" not in data:
        return bad_request('must include name and email fields')
    
    if any(map(lambda x: len("".join(str(x).split())) < 1, [data["password"], data["email"]])):
        return bad_request('Nice try...but no....we do not accept blanks')

    elif any(map(lambda x: len("".join(str(x).split())) < 3, [data["password"], data["email"]])):
        return bad_request('minimum length should be 3 characters long')    

    email = data['email']
    password = data['password']

    token = user.login(email,password)
    return make_response(jsonify({
       "status" : 200,
       "user" : [{
           "token": user.auth_token_encode(token[0]),
           "user" : user.to_dict(token)

       }]}),200)