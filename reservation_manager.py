import json
import os

FILE_NAME = "reservations.json"

def load_reservations():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []

def save_reservations(reservations):
    with open(FILE_NAME, "w") as file:
        json.dump(reservations, file, indent=4)
