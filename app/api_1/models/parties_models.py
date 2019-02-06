parties = []


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


    