from datetime import date
from typing import List, Optional

class Event:
    def __init__(self, category: str, startDate: date, endDate: Optional[date] = None):
        self.category = category
        self.startDate = startDate
        self.endDate = endDate
        self.peopleInvolved = []
    
    def add_people_involved(self, person: str):
        if person not in self.peopleInvolved:
            self.peopleInvolved.append(person)

    def __str__(self):
        return f"{self.category}, started {self.startDate}"

    def get_event_info(self):
        return {
            "event": self.category,
            "date": self.startDate,
            "people involved": self.peopleInvolved
        }

if __name__ == "__main__":
    # Create event instances
    event1 = Event("wedding", date(1780, 6, 17))
    event2 = Event("meeting", date(1820, 1, 2), date(1850, 4, 28))
    
    # Add people to the events (example)
    event1.add_people_involved("John Doe")
    event2.add_people_involved("Jane Smith")

    # Print event info
    print(f"{event1.get_event_info()}")
    print(f"{event2.get_event_info()}")
