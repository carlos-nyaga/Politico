offices = [{
            "office_id": 1,
            "office_type": "federal",
            "office_name": "President"
            
        },
        {
            "office_id": 2,
            "office_type": "legislative",
            "office_name": "Member of Parliament"
            
        },
        {
            "office_id": 3,
            "office_type": "state",
            "office_name": "Governor"
            
        },
        {
            "office_id": 3,
            "office_type": "local government",
            "office_name": "MCA"
            
        }]


class Offices:
    def __init__(self):
        self.offices = offices


    def office_create(self, type, name):
        office = {
            "office_id": len(self.offices)+1,
            "office_type": type,
            "office_name": name
        }
        self.offices.append(office)
        return office

    def office_get(self, id = None):
        if id:
            data = {
                "id": offices[id-1]['office_id'],
                "name" : offices[id-1]['office_name'],
                "type": offices[id-1]['office_type']
                }
            return data

        else:
            data = []
            for i in range(len(offices)):
                office = {
                    "id": offices[i]['office_id'],
                    "name": offices[i]['office_name'],
                    "type": offices[i]['office_type']
                }

                data.append(office)
            return data