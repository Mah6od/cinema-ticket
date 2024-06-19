from reservation_manager import load_reservations, save_reservations
from ticket import generate_ticket_image

class CinemaReservation:
    def __init__(self):
        self.reservations = load_reservations()

    def is_chair_available(self, chair_number):
        for reservation in self.reservations:
            if chair_number in reservation["chair_numbers"]:
                return False
        return True

    def are_all_chairs_full(self):
        all_chairs = set(range(1, 101))
        reserved_chairs = set(chair for reservation in self.reservations for chair in reservation["chair_numbers"])
        return all_chairs == reserved_chairs

    def make_reservation(self):
        if self.are_all_chairs_full():
            print("All chairs are full. No more reservations can be made.")
            return

        print("Welcome to the cinema reservation system!")

        name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        age = int(input("Enter your age: "))
        
        gender = input("Enter your gender (male/female): ").lower()
        while gender not in ['male', 'female']:
            print("Invalid input. Please enter 'male' or 'female'.")
            gender = input("Enter your gender (male/female): ").lower()

        num_people = int(input("Enter the number of people (maximum 5): "))
        while num_people < 1 or num_people > 5:
            print("You can reserve between 1 to 5 chairs.")
            num_people = int(input("Enter the number of people (maximum 5): "))

        chair_numbers = []
        for i in range(num_people):
            chair_number = int(input(f"Enter chair number {i+1} (1-100): "))
            while chair_number < 1 or chair_number > 100 or not self.is_chair_available(chair_number):
                print("It's full, please select another one.")
                chair_number = int(input(f"Enter chair number {i+1} (1-100): "))
            chair_numbers.append(chair_number)

        reservation = {
            "name": name,
            "last_name": last_name,
            "age": age,
            "chair_numbers": chair_numbers
        }

        self.reservations.append(reservation)
        save_reservations(self.reservations)

        generate_ticket_image(name, last_name, age, chair_numbers, gender)

        print("Reservation successful!")

if __name__ == "__main__":
    CinemaReservation().make_reservation()
