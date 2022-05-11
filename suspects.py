# Create the list of suspects.

class Suspect:
    def __init__(self, name, title, color, relationship, motivation):
        self.name = name
        self.title = title
        self.color = color
        self.relation = relationship
        self.motive = motivation


suspect1 = Suspect('Kelly', 'Mr.', 'green', 'son', 'financial gain')
suspect2 = Suspect('Golden', 'Dr.', 'yellow', 'employee', 'verbally abused by the victim')
suspect3 = Suspect('Azure', 'Mrs.', 'blue', 'daughter-in-law', 'blames victim for her husband\'s death')
suspect4 = Suspect('Lavender', 'Capt.', 'purple', 'friend', 'victim knew a dark secret')
suspect5 = Suspect('Cerise', 'Miss', 'red', 'daughter', 'rebelling against victim\'s control over her life')
suspect6 = Suspect('Snow', 'Chef', 'white', 'employee', 'victim spurned her')
