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