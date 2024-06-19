import json
import os

# Function to load reservations from file
def load_reservations(file_name="reservations.json"):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

# Function to save reservations to file
def save_reservations(reservations, file_name="reservations.json"):
    with open(file_name, "w") as file:
        json.dump(reservations, file, indent=4)

# Function to check if a chair is available
def is_chair_available(reservations, chair_number):
    for reservation in reservations:
        if chair_number in reservation["chair_numbers"]:
            return False
    return True

# Main function to handle reservations
def make_reservation():
    reservations = load_reservations()

    print("Welcome to the cinema reservation system!")

    name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    num_people = int(input("Enter the number of people: "))

    chair_numbers = []
    for i in range(num_people):
        chair_number = int(input(f"Enter chair number {i+1} (1-100): "))
        while chair_number < 1 or chair_number > 100 or not is_chair_available(reservations, chair_number):
            print("It's full, please select another one.")
            chair_number = int(input(f"Enter chair number {i+1} (1-100): "))
        chair_numbers.append(chair_number)

    reservation = {
        "name": name,
        "last_name": last_name,
        "age": age,
        "chair_numbers": chair_numbers
    }

    reservations.append(reservation)
    save_reservations(reservations)

    print("Reservation successful!")

# Run the reservation function
make_reservation()
