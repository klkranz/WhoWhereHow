# Create a list of locations

class Location:
    def __init__(self, room_name, description, secret_passage, connects_to=None):
        self.name = room_name
        self.desc = description
        self.secret = secret_passage
        self.connect = connects_to


location1 = Location('Ballroom', 'The grand ballroom has parquet floor and a beautiful crystal chandelier.', False)
location2 = Location('Billiard Room', 'The billiard room has wood paneling and a plush billiard table and '
                                      'comfortable chairs.', False)
location3 = Location('Conservatory', 'The conservatory has large glass windows and a lot of potted plants.', True,
                     'Lounge')
location4 = Location('Dining Room', 'The dining room has a large elegant table and chairs with a large side-board '
                                    'and cupboard.', False)
location5 = Location('Hall', "The hall is a grand entrance from the front door with doors leading into the rest of "
                             "the mansion.", False)
location6 = Location('Kitchen', 'The kitchen has a large stove and oven and sink.', True, 'Study')
location7 = Location('Library', 'The library has ceiling to floor bookcases and comfortable chairs and couches.', False)
location8 = Location('Lounge', 'The lounge has large windows and couches in a couple of conversation groups.', True,
                     'Conservatory')
location9 = Location('Study', 'The study has a large ornate desk and a small grouping of chairs.', True, 'Kitchen')
