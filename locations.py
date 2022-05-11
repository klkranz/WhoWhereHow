# Create a list of locations

class Location:
    def __init__(self, room_name, description, secret_passage, connects_to=None):
        self.name = room_name
        self.desc = description
        self.secret = secret_passage
        self.connect = connects_to


location1 = Location('Cellar', 'fill in description.', False)
location2 = Location('Attic', 'fill in description.', False)
location3 = Location('Conservatory', 'fill in description.', True, 'Laboratory')
location4 = Location('Dining Room', 'fill in description', False)
location5 = Location('Master Bedroom', 'fill in description', False)
location6 = Location('Kitchen', 'fill in description', True, 'Study')
location7 = Location('Library', 'fill in description', False)
location8 = Location('Laboratory', 'fill in description', True, 'Conservatory')
location9 = Location('Study', 'fill in description', True, 'Kitchen')
