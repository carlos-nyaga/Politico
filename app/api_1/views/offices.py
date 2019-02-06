from app.api_1 import bp

@bp.route('/offices', methods= ['POST'])
def create_office():
    pass

@bp.route('/offices', methods =['GET'])
def get_offices():
    pass

@bp.route('/offices/<int:id>', methods =['GET'])
def get_office(id):
    pass