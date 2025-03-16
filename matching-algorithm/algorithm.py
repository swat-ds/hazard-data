from datetime import date
from typing import List, Optional
import argparse, csv

# Notes:
#
# Create an Event class.
# Change the status from alive vs. dead into something more complex (TBD).
# Consider adding methods or attributes for comparing parents.
# James recommends using DictReader class from csv module to read in data.
# Focus on creating personas from events for now.

class Persona:
    def __init__(
        self, eventId, firstName, lastName, meeting, activeDate=None, 
        middleNames='', birthdate=None, deathdate=None
    ):
        self.eventId = eventId
        self.firstName = firstName
        self.middleNames = middleNames
        self.lastName = lastName
        self.meeting = meeting
        self.activeDate = activeDate
        self.additionalNames = []
        self.name = ' '.join([self.firstName, self.middleNames, self.lastName])
        self.name = self.name.replace('  ', ' ')
        self.birthdate = birthdate
        self.deathdate = deathdate
        self.siblings = []
        self.parents = []
        self.children = []
        self.spouses = []

    def add_middle_names(self, additionalNames: 'Persona'):
        if additionalNames not in self.additionalNames:
            self.additionalNames.append(additionalNames)

    def add_sibling(self, sibling: 'Persona'):
        if sibling not in self.siblings:
            self.siblings.append(sibling)
            # ensure the sibling also has the current person as a sibling
            sibling.add_sibling(self)  

    def add_parent(self, parent: 'Persona'):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.add_child(self)

    def add_child(self, child: 'Persona'):
        if child not in self.children:
            self.children.append(child)
            child.add_parent(self)

    def add_spouse(self, spouse: 'Persona'):
        if spouse not in self.spouses:
            self.spouses.append(spouse)
            spouse.add_spouse(self)

    def get_status(self) -> str:
        if self.birthdate:
            print(f"Born on {self.birthdate}")
        else:
            print(f"Date of birth unreported")
        print(f'Active around {self.activeDate}')
        if self.deathdate:
            print(f"Deceased on {self.deathdate}")
        else:
            print(f"Date of death unreported")

    def __str__(self):
        msg=f"{self.name}, born {self.birthdate}, Status: {self.get_status()}"
        return msg

    def get_family_info(self):
        siblings_names = [sibling.name for sibling in self.siblings]
        parents_names = [parent.name for parent in self.parents]
        children_names = [child.name for child in self.children]
        spouses_names = [spouses.name for spouses in self.spouses]
        return {
            "siblings": siblings_names,
            "parents": parents_names,
            "children": children_names,
            "spouse(s)": spouses_names
        }

def loadCSV(filepath):
    data = []
    with open(filepath) as f:
        reader = csv.DictReader(f, delimiter="\t")
        for row in reader:
            data.append(row)

    return data

def makePersonasFromEvent(event, eventTypeList):
    """Given a dict representing an event, return a list of persona objects
    """
    # Initialize list of personas that we'll eventually return
    personas = []
   
    # Get the type of event we're handling
    eventType = event['event']

    # Handle main persona first
    # (build up a dict, and then feed it into the obj constructor)
        # Basic categories:
    mainPers = {} 
    mainPers['eventId'] = event['ID']
    mainPers['firstName'] = event['First Name']
    mainPers['lastName'] = event['Last Name']
    mainPers['meeting'] = event['Meeting']
    
        # Dates
    if eventType in eventTypeList['birthEvents']:
        mainPers('birthdate') = event['Date']
    elif eventType in eventTypeList['deathEvents']:
        mainPers('deathdate') = event['Date']
    else:
        mainPers(activeDate) = event['Date']

    return [1,2] #placeholder return value

    # Check the following fields for potential personas:
            # Children
            # Mother
            # Father
            # Spouse(s)
            # Spouse
            # S1 name
            # S1 Father
            # S1 Mother
            # S1 former spouse
            # S2 father
            # S2 mother
            # S2 former spouse
            # Siblings

        # Make a persona for the base person (first name, last name)
        # Make personas from all the people in the corresponding fields
        # Make sure the personas are interlinked


# Usage
if __name__ == "__main__":

    # Define which types of events belong to which categories
    eventTypeList = {
        'birthEvents': ['b', 'b ?', 'bapt', 'B', 'bapt'],
        'deathEvents': ['d', 'dec', 'dec ?', 'bur'],
        'disciplEvents': ['dis', 'ack', 'relrq', 'com', 'jas', 'con', 'mcd',
            'rpd', 'mou', 'mos'], 
            #^TODO^: Consider splitting more finely; handle mcd/mou/mos
        'familyEvents': ['fam', 'h', 'w', 'ch'],
        'joiningEvents': ['recrq', 'rst', 'rqcuc'],
        'marriageEvents': ['m', 'rmt', 'ami', 'amist', 'rm'],
        'memberEvents': ['mbr', 'mbrp', 'mbr minor', 'mbr ?'],
        'movemtEvents': ['cert', 'rm', 'rocf', 'prcf'] # TODO: Add rest
    }

    person1 = Persona(1, "A", 'Moon', 'Goshen', date(1980, 5, 10))
    person2 = Persona(2, "B", 'Sun', 'Goshen', date(1983, 8, 15))

    person1.add_sibling(person2)
    person2.add_parent(person1)

    print(person1)
    print(f"Family Info: {person1.get_family_info()}")
    print(person2)
    print(f"Family Info: {person2.get_family_info()}")


    # Get CSV file path from command line arguments with argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('csvfile')
    args = parser.parse_args()
    filepath = args.csvfile

    # Load event records from CSV
    events = loadCSV(filepath)

    personas = []
    for i, event in enumerate(events):
        personaList = makePersonasFromEvent(event, eventTypeList)
        personas += personaList
        

    # Convert event list into dict with IDs as keys for easy reference
    events = {event['ID']: event for event in events}

    # Do shallow blocking of personas
    # TODO: Sort personas by how much information they contain
    personaBlocks = []
    # TODO: blocking

    # Create individuals from persona groups
    individuals = []
    # TODO: matching within blocks
