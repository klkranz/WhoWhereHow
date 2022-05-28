# Murder Mystery Game - A Murder at Hearth Manor

# Create class for Suspects detailing information that will be needed to solve the problem.
class Suspect:
    """Each suspect has a name, title(profession), associated color, relationship to the victim
    and a motive for wanting the victim dead."""
    def __init__(self, name, title, color, relation, motive):
        self.name = name
        self.title = title
        self.color = color
        self.relation = relation
        self.motive = motive

    def __str__(self):
        return f"{self.title} {self.name}, the victim's {self.relation}"


# Create a class for Locations detailing information about the locations.
class Location:
    """Each location has a name, description, either does or doesn't have a secret passage.
    If secret passage is True, then it shows the location to which it connects."""

    def __init__(self, room_name, description, secret_passage, connects_to=None):
        self.name = room_name
        self.description = description
        self.secret_passage = secret_passage
        self.connects_to = connects_to

    def __str__(self):
        return f"{self.name} - {self.description} - connects to {self.connects_to}"


# Create a class for the Weapons that could be used by the suspects.
class Weapons:
    """Each potential weapon has a name, description and the location where it is normally found."""
    def __init__(self, item_name, description, start_loc):
        self.name = item_name
        self.description = description
        self.start = start_loc

    def __str__(self):
        return f"{self.name} - {self.description} - normally found in {self.start}"


# Defining the specific suspects, locations and potential weapons.
suspect1 = Suspect('Kelly Hearth', 'Mr.', 'green', 'son', 'financial gain as only living male heir')
suspect2 = Suspect('Cerise Hearth', 'Miss', 'red', 'daughter', "rebelling against victim's control over her life")
suspect3 = Suspect('Azure Hearth', 'Mrs.', 'blue', 'widowed daughter-in-law', "blames victim for her husband's death")
suspect4 = Suspect('Lavender', 'Capt.', 'purple', 'friend from military days', 'victim knew his dark secret')
suspect5 = Suspect('Golden', 'Dr.', 'yellow', 'employee, a personal physician', 'verbally abused by the victim')
suspect6 = Suspect('Snow', 'Chef', 'white', 'employee, the cook for the household', 'victim spurned her affection')
location1 = Location('Attic', 'fill in description.', False)
location2 = Location('Master Bedroom', 'fill in description', True, 'Study')
location3 = Location('Study', 'fill in description', True, 'Master Bedroom')
location4 = Location('Conservatory', 'fill in description.', True, 'Laboratory')
location5 = Location('Dining Room', 'fill in description', False)
location6 = Location('Library', 'fill in description', False)
location7 = Location('Kitchen', 'fill in description', False,)
location8 = Location('Laboratory', 'fill in description', True, 'Conservatory')
location9 = Location('Cellar', 'fill in description.', False)
weapon1 = Weapons('candlestick', 'a heavy silver-plated candlestick with no candle.', 'Dining Room')
weapon2 = Weapons('knife', "a sharp chef's knife", 'Kitchen')
weapon3 = Weapons('poison', 'a vial of liquid with the poison warning on an otherwise unreadable label', 'Laboratory')
weapon4 = Weapons('revolver', 'a military service revolver with ammunition', 'Study')
weapon5 = Weapons('twisted wire', 'a length of several electrical wires twisted together.', 'Attic')
weapon6 = Weapons('hammer', 'slightly rusted household hammer with a wooden handle.', 'Cellar')

# Opening introduction to the game, asking the player to name themselves and presenting the initial facts.
detective = input("Welcome to the Mystery at Hearth Manor.\nPlease enter the name you would like to be called: \n")
print(f"Welcome, Detective {detective}. We have an unusual situation for you to investigate today. \n"
      f"Mr. Hearth was found dead with signs that multiple attempts on his life were made with various methods.\n"
      f"All of the suspects are still in the manor. Present in the manor are:")
suspect_list = [suspect1, suspect2, suspect3, suspect4, suspect5, suspect6]
for i in range(0, len(suspect_list)):
    print(suspect_list[i])

location_list = [location1, location2, location3, location4, location5, location6, location7, location8, location9]
# for i in range(0, len(location_list)): print(location_list[i])
# weapon_list = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6]
# for i in range(0, len(weapon_list)): print(weapon_list[i])
# Randomly pick one suspect, one location and one weapon as the 'correct answer'.
# murder_list = [random.choice(suspect_list), random.choice(location_list), random.choice(weapon_list)]
# for i in range(0, len(murder_list)): print(murder_list[i])
