# Create list of weapons of the murder.

class Weapons:
    def __init__(self, item_name, description, start_loc):
        self.weapon = item_name
        self.desc = description
        self.start = start_loc


weapon1 = Weapons('candlestick', 'The candlestick is a large silver-plated single candlestick.', 'Lounge')
weapon2 = Weapons('knife', 'The knife is a sharp knife from the dining room silverware set.', 'Dining Room')
weapon3 = Weapons('lead pipe', 'The lead pipe appears to have been removed from some part of the mansion plumbing.',
                  'Conservatory')
weapon4 = Weapons('revolver', 'The revolver is a fully functional hand gun with ammunition loaded.', 'Study')
weapon5 = Weapons('rope', 'The rope is a length of sturdy hemp rope.', 'Hall')
weapon6 = Weapons('wrench', 'The wrench is a slightly rusted adjustable wrench.', 'Kitchen')
