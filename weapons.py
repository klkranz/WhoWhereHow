# Create list of weapons of the murder.

class Weapons:
    def __init__(self, item_name, description, start_loc):
        self.weapon = item_name
        self.desc = description
        self.start = start_loc


weapon1 = Weapons('candlestick', 'a heavy silver-plated candlestick with no candle.', 'Dining Room')
weapon2 = Weapons('knife', 'a sharp chef\'s knife', 'Kitchen')
weapon3 = Weapons('poison', 'a vial of liquid with the poison warning on an otherwise unreadable label', 'Laboratory')
weapon4 = Weapons('revolver', 'a military service revolver with ammunition', 'Study')
weapon5 = Weapons('twisted wire', 'a length of electrical wires twisted together in a bundle.', 'Attic')
weapon6 = Weapons('hammer', 'slightly rusted household hammer.', 'Cellar')
