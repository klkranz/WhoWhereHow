# Create a list of locations

class Location:
    def __init__(self, room_name, description, secret_passage, connects_to):
        self.name = room_name
        self.desc = description
        self.secret = secret_passage
        self.connect = connects_to
