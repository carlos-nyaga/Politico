parties = [{
            "party_code": 23,
            "party_id": 1,
            "party_name": "Annd",
            "party_hq": "karen",
            "party_logo": "Learning is a top"
        },
        {
            "party_code": 24,
            "party_id": 2,
            "party_name": "Ian",
            "party_hq": "karen",
            "party_logo": "Dope king"
        },
        {
            "party_code": 25,
            "party_id": 3,
            "party_name": "Jayson",
            "party_hq": "karen",
            "party_logo": " Shadow warrior"
        }]


class Parties:
    def __init__(self):
        self.parties = parties

    
    def party_create(self, id, name, hq_address, logo_url):
        party = {
            "party_code": id,
            "party_id": len(self.parties)+1,
            "party_name": name,
            "party_hq": hq_address,
            "party_logo": logo_url
        }
        self.parties.append(party)
        return party



    def party_get(self,id):
        self.parties = parties
        data = {
            "id": parties[id-1]['party_id'],
             "name" : parties[id-1]['party_name'],
             "logoUrl": parties[id-1]['party_logo']
            }
        return data

    def party_edit(self, id ,name):
        self.parties = parties
        parties[id-1] ['party_name'] = name
        data = {
            "id" : parties[id-1]['party_id'],
            "name" : parties[id-1]['party_name']
        }
        return data


    