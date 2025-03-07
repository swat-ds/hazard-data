import csv
from datetime import datetime
from collections import defaultdict

# Define the Persona class
class Persona:
    def __init__(self, id, first_name, last_name, note, event, year, month, day, meeting, call_number, volume, page, hazard_index):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.note = note
        self.event = event
        self.year = year
        self.month = month
        self.day = day
        self.meeting = meeting
        self.call_number = call_number
        self.volume = volume
        self.page = page
        self.hazard_index = hazard_index

    def __str__(self):
        # Check if year, month, and day are valid
        try:
            event_date = datetime(self.year, self.month, self.day).strftime('%B %d, %Y')
        except ValueError:
            event_date = "Invalid Date"
        
        # Return a string representation of the Persona
        return f"Name: {self.first_name} {self.last_name}, Event: {self.event}, Date: {event_date}"

# Define the Individual class
class Individual:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.events = []

    def add_event(self, event):
        if event not in self.events:
            self.events.append(event)

    def __str__(self):
        return f"Name: {self.first_name} {self.last_name}, Events: {', '.join(self.events)}"

# Function to read the CSV file and create Persona objects
def read_csv_and_create_personas(csv_file_path):
    personas = []
    
    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        print("Column names in CSV:", reader.fieldnames)  # Print column names
        
        for row in reader:
            try:
                # Ensure valid year, month, day data before creating Persona
                year = int(row['Year']) if row['Year'].isdigit() else None
                month = int(row['Month']) if row['Month'].isdigit() else None
                day = int(row['Day']) if row['Day'].isdigit() else None
                
                persona = Persona(
                    id=row['ID'],
                    first_name=row['First name'],
                    last_name=row['Last name'],
                    note=row['Note'],
                    event=row['Event'],
                    year=year,
                    month=month,
                    day=day,
                    meeting=row['Meeting'],
                    call_number=row['Call #'],
                    volume=row['Volume'],
                    page=row['Page'],
                    hazard_index=row['Index assigned by Hazard']
                )
                personas.append(persona)
            except ValueError as e:
                print(f"Error processing row: {e} - Row: {row}")
            except KeyError as e:
                print(f"Missing key: {e}")
    
    return personas

# Function to combine personas into individuals based on name matching
def combine_personas_to_individuals(personas):
    individuals = defaultdict(Individual)  # Use a dictionary to group personas by (first_name, last_name)
    
    for persona in personas:
        key = (persona.first_name, persona.last_name)
        if key not in individuals:
            individuals[key] = Individual(persona.first_name, persona.last_name)
        individuals[key].add_event(persona.event)
    
    return list(individuals.values())

# Function to display each individual
def display_individuals(individuals):
    for individual in individuals:
        print(individual)

def main():
    csv_file_path = '/Users/fionamoon/Downloads/allHazard_thru1937.csv'
    personas = read_csv_and_create_personas(csv_file_path)
    individuals = combine_personas_to_individuals(personas)
    display_individuals(individuals)

if __name__ == "__main__":
    main()
