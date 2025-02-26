from datetime import date
from typing import List, Optional

# Notes:
#
# Create an Event class.
# Change the status from alive vs. dead into something more complex (TBD).
# Consider adding methods or attributes for comparing parents.
# James recommends using DictReader module to read in csv data.
# Focus on creating personas from events for now.

class Person:
    def __init__(self, firstName: str, lastName: str, birthday: Optional[date] = None, deathday: Optional[date] = None):
        self.firstName = firstName
        self.lastName = lastName
        self.additionalNames = []
        self.birthday = birthday
        self.deathday = deathday
        self.siblings = []
        self.parents = []
        self.children = []
        self.spouses = []

    def add_middle_names(self, additionalNames: 'Person'):
        if additionalNames not in self.additionalNames:
            self.additionalNames.append(additionalNames)

    def add_sibling(self, sibling: 'Person'):
        if sibling not in self.siblings:
            self.siblings.append(sibling)
            sibling.add_sibling(self)  # ensure the sibling also has the current person as a sibling

    def add_parent(self, parent: 'Person'):
        if parent not in self.parents:
            self.parents.append(parent)
            parent.add_child(self)

    def add_child(self, child: 'Person'):
        if child not in self.children:
            self.children.append(child)
            child.add_parent(self)

    def add_spouse(self, spouse: 'Person'):
        if spouse not in self.spouses:
            self.spouses.append(spouse)
            spouse.add_spouse(self)

    def get_status(self) -> str:
        if self.birthday:
            print(f"Born on {self.birthday}")
        else:
            print(f"Date of birth unreported")
        if self.deathday:
            print(f"Deceased on {self.deathday}")
        else:
            print(f"Date of death unreported")

    def __str__(self):
        return f"{self.name}, born {self.birthday}, Status: {self.get_status()}"

    def get_family_info(self):
        siblings_names = [sibling.name for sibling in self.siblings]
        parents_names = [parent.name for parent in self.parents]
        children_names = [child.name for child in self.children]
        spouses_names = [spouses.name for spouses in self.spouses]
        return {
            "siblings": siblings_names,
            "parents": parents_names,
            "children": children_names
            "spouse(s)": spouses_names
        }

# Usage
if __name__ == "__main__":
    person1 = Person("A", date(1980, 5, 10))
    person2 = Person("B", date(1983, 8, 15))
    person3 = Person("C", date(2010, 1, 20))
    person4 = Person("D", date(1995, 3, 25), deathday=date(2025, 2, 17))

    person1.add_sibling(person2)
    person2.add_parent(person1)
    person1.add_child(person3)

    print(person1)
    print(f"Family Info: {person1.get_family_info()}")
    print(person2)
    print(f"Family Info: {person2.get_family_info()}")
    print(person3)
    print(f"Family Info: {person3.get_family_info()}")
    print(person4)
    print(f"Family Info: {person4.get_family_info()}")
