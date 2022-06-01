# Murder Mystery Game - A Murder at Hearth Manor

# Create class for Suspects detailing information that will be needed to solve the problem.
class Suspect:
    """Each suspect has a name, title(profession), a signature item in their favorite color, relationship to the victim
    and a motive for wanting the victim dead."""
    def __init__(self, name, title, signature_item, relation, motive):
        self.name = name
        self.title = title
        self.signature_item = signature_item
        self.relation = relation
        self.motive = motive

    def __str__(self):
        return f"{self.title} {self.name}, the victim's {self.relation}"


# Create a class for Locations detailing information about the locations.
class Location:
    """Each location has a name, description, description of what doors in the room connect to and
    if there is a secret passage, to what room it connects."""

    def __init__(self, room_name, description, connects_to, secret_passage=None):
        self.name = room_name
        self.description = description
        self.connects_to = connects_to
        self.secret_passage = secret_passage

    def __str__(self):
        return f"The {self.name} is {self.description}. It has {self.connects_to}"


# Create a class for the Weapons that could be used by the suspects.
class Weapons:
    """Each potential weapon has a name, description and the location where it is normally found."""
    def __init__(self, item_name, description, start_loc):
        self.name = item_name
        self.description = description
        self.start = start_loc

    def __str__(self):
        return f"{self.name} - {self.description} - normally found in {self.start}"


# Class providing witness reports from each of the suspects.
class Witness:
    """When a witness is questioned, they provide their name, their timeline of events, a clue about witnessing
    someone else up to something suspicious, a lie about their own activities, and a half-truth about their motive."""
    def __init__(self, name, timeline, clue, lie, half_truth):
        self.name = name
        self.timeline = timeline
        self.clue = clue
        self.lie = lie
        self.half_truth = half_truth


# Defining the specific suspects, locations and potential weapons.
suspect1 = Suspect("Kelly", "Mr.", "green jacket", "son", "financial gain as only living male heir")
suspect2 = Suspect("Cerise", "Miss", "red scarf", "daughter",
                   "rebelling against victim's control over her life")
suspect3 = Suspect("Azure", "Mrs.", "blue dress", "widowed daughter-in-law",
                   "blames victim and victim blames her for her husband's death")
suspect4 = Suspect("Lavender", "Capt.", "purple tie", "friend from military days",
                   "victim threatened to reveal a dark secret from his past")
suspect5 = Suspect("Golden", "Dr.", "yellow vest", "employee, a personal physician", "verbally abused by the victim")
suspect6 = Suspect("Snow", "Housekeeper", "white apron", "employee, the housekeeper and cook",
                   "mistress with hopes to become his new wife")
location1 = Location("Attic",
                     "a dusty storage space, piled with boxes, trunks and random items from generations of the Hearth "
                     "family. Some odd things stand out such as a box of very rusted nails, a hollowed out grenade, a "
                     "coil of electrical wire and a box of broken or cracked beakers and vials.",
                     "There is a stairway down to the first floor hallway and a small window which lets in some light.")
location2 = Location("Master Bedroom",
                     "lavishly appointed with a four-posted bed and an overstuffed chair next to the fireplace. A "
                     "nightstand containing a water pitcher, glass, and a tray with an assortment of ointments, "
                     "tinctures and bottles of pills. The wardrobe has all the clothes pushed to one side.",
                     "This room has a door to the first floor hallway and a door to a private bathroom.",
                     "The wardrobe conceals a secret stairway down to the Study.")
location3 = Location("Laboratory",
                     "a cluttered and dirty room. The counters display signs of wear and stains from past "
                     "\"experiments\". Old beakers, tubes and other paraphernalia are scattered on all available "
                     "counters as if left in the middle of whatever project for which they were used. The shelves "
                     "above are covered with stoppered bottles, vials and boxes mostly covered in dust. There are two "
                     "wooden cabinets built into one wall.",
                     "There is a door to the first floor hallway",
                     "A wooden cabinet conceals a secret stairway down to the Conservatory.")
location4 = Location("Study",
                     "a comfortable room with wood paneling on the walls. The most imposing item in the room is a "
                     "large wooden desk with ink stains, piles of papers, and many drawers including one with a lock. "
                     "It looks like the lock has been tampered with at some point. There are two comfortable and "
                     "well-used chairs placed in front of the fireplace with a small table conveniently placed for a "
                     "tray of drinks.",
                     "There is a door to the ground floor hallway.",
                     "A narrow bookshelf behind the desk conceals a secret stairway up to the Master Bedroom.")
location5 = Location("Conservatory",
                     "an indoor greenhouse filled with low planters and small potted plants. There are some cushioned "
                     "benches, chairs and small tables affording a peaceful spot to enjoy the beauty of nature while "
                     "still being comfortable.",
                     "There is a door to the Library, a door to the ground floor hallway and a glass door out into the "
                     "gardens. A door leads to a small closet used as a shed for gardening tools.",
                     "The closet conceals a secret stairway up to the Laboratory.")
location6 = Location("Dining Room",
                     "an elegant dining space with a finely carved dining table and matching chairs. A large sideboard "
                     "displays the fine serving dishes, well-polished silverware, ornate china plates and silver "
                     "candlesticks. The crystal chandelier hangs above the middle of the table.",
                     "There is a door to the kitchen and a door to the ground floor hallway.")
location7 = Location("Library",
                     "lined with bookshelves filled with books. Some of the books are obviously covered in dust and "
                     "others look frequently used. There are cushioned window-seats at the two large bay windows, and "
                     "other comfortable chairs and a couch in two small conversation groups.",
                     "There is a door to the Conservatory, and a door to the ground floor hallway")
location8 = Location("Kitchen",
                     "a large but simple room decorated to be utilitarian not grand like the rest of the manor. "
                     "Everything seems to have its place and there is no sign of any dust, crumb or stain except the "
                     "old stains on the large wooden cutting board next to the block where all the knives are stored.",
                     "There is a door to the Dining room, a door to the ground floor hallway and a door to a stairway "
                     "down to the Cellar.")
location9 = Location("Cellar",
                     "a stone-walled room with a well-compacted dirt floor. There a some baskets with root vegetables "
                     "and a small wine rack with various ages of wine and other unknown bottles. There is a small "
                     "workman's bench in one corner with household tools haphazardly lying on the bench or hung on "
                     "pegs in the wall above it.",
                     "There is a stairway up to the Kitchen.")
weapon1 = Weapons("candlestick", "a heavy silver-plated candlestick with no candle.", "Dining Room")
weapon2 = Weapons("knife", "a sharp chef's knife", "Kitchen")
weapon3 = Weapons("poison", "a vial of liquid with the poison warning on an otherwise unreadable label", "Laboratory")
weapon4 = Weapons("revolver", "a military service revolver with ammunition", "Study")
weapon5 = Weapons("twisted wire", "a length of several electrical wires twisted together.", "Attic")
weapon6 = Weapons("hammer", "slightly rusted household hammer with a wooden handle.", "Cellar")

# Opening introduction to the game, asking the player to name themselves and presenting the initial facts.
detective = input("Welcome to the Mystery at Hearth Manor.\nI've forgotten your name, Detective...? \n")
print(f"Welcome, Detective {detective}. We have an unusual situation for you to investigate today. \n"
      f"Mr. Hearth was found dead with signs that multiple attempts on his life were made with various methods.\n"
      f"All of the suspects are still in the manor. Present in the manor are:")
suspect_list = [suspect1, suspect2, suspect3, suspect4, suspect5, suspect6]
for i in range(0, len(suspect_list)):
    print(suspect_list[i])

location_list = [location1, location2, location3, location4, location5, location6, location7, location8, location9]
for i in range(0, len(location_list)): print(location_list[i])
weapon_list = [weapon1, weapon2, weapon3, weapon4, weapon5, weapon6]
for i in range(0, len(weapon_list)): print(weapon_list[i])
# Notes for later version: randomly pick the suspect and weapon.
# import random  # This should be at the beginning of the code.
# murder_list = [random.choice(suspect_list), random.choice(weapon_list)]
# for i in range(0, len(murder_list)): print(murder_list[i])
