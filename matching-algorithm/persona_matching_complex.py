import csv
from datetime import datetime
from fuzzywuzzy import fuzz
from collections import defaultdict

# Define the Persona class
class Persona:
    def __init__(self, id, first_name, last_name, note, event, year, month, day, meeting, call_number, volume, page, hazard_index):
        self.id = id
        self.first_name = first_name.lower().strip()  # Lowercase and strip for optimization
        self.last_name = last_name.lower().strip()    # Lowercase and strip for optimization
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
        try:
            event_date = datetime(self.year, self.month, self.day).strftime('%B %d, %Y')
        except ValueError:
            event_date = "Invalid Date"
        return f"Name: {self.first_name.capitalize()} {self.last_name.capitalize()}, Event: {self.event}, Date: {event_date}"

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
                year = int(row['Year']) if row['Year'].isdigit() else 1900
                month = int(row['Month']) if row['Month'].isdigit() else 1
                day = int(row['Day']) if row['Day'].isdigit() else 1
                
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

# Optimized matching algorithm using fuzzywuzzy
def match_personas(personas, threshold=80):
    matched_individuals = defaultdict(Individual)
    
    # First, group personas by first and last name for more efficient matching
    grouped_personas = defaultdict(list)
    for persona in personas:
        grouped_personas[(persona.first_name, persona.last_name)].append(persona)

    for (first_name, last_name), grouped in grouped_personas.items():
        # If multiple personas have the same name, apply fuzzy matching to detect near matches
        if len(grouped) > 1:
            for persona in grouped:
                found_match = False
                # Check existing individuals for possible matches based on name similarity
                for individual_key, individual in matched_individuals.items():
                    # Fuzzy match names (first_name and last_name)
                    if fuzz.ratio(persona.first_name, individual.first_name) > threshold and \
                       fuzz.ratio(persona.last_name, individual.last_name) > threshold:
                        individual.add_event(persona.event)
                        found_match = True
                        break
                
                # If no match is found, create a new individual
                if not found_match:
                    new_individual = Individual(persona.first_name.capitalize(), persona.last_name.capitalize())
                    new_individual.add_event(persona.event)
                    matched_individuals[(persona.first_name, persona.last_name)] = new_individual
        else:
            # If only one persona exists with this name, simply add it to the matched individuals
            persona = grouped[0]
            matched_individuals[(persona.first_name, persona.last_name)] = Individual(persona.first_name.capitalize(), persona.last_name.capitalize())
            matched_individuals[(persona.first_name, persona.last_name)].add_event(persona.event)
    
    return list(matched_individuals.values())

# Function to display each individual
def display_individuals(individuals):
    for individual in individuals:
        print(individual)

def main():
    csv_file_path = '/Users/fionamoon/Downloads/allHazard_thru1937.csv'
    personas = read_csv_and_create_personas(csv_file_path)
    individuals = match_personas(personas)  # Use the new match function
    display_individuals(individuals)

if __name__ == "__main__":
    main()
