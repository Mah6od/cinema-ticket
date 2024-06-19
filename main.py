from reservation_manager import load_reservations, save_reservations

# Function to check if a chair is available
def is_chair_available(reservations, chair_number):
    for reservation in reservations:
        if chair_number in reservation["chair_numbers"]:
            return False
    return True

# Function to check if all chairs are full
def are_all_chairs_full(reservations):
    all_chairs = set(range(1, 101))
    reserved_chairs = set(chair for reservation in reservations for chair in reservation["chair_numbers"])
    return all_chairs == reserved_chairs

# Main function to handle reservations
def make_reservation():
    reservations = load_reservations()

    if are_all_chairs_full(reservations):
        print("All chairs are full. No more reservations can be made.")
        return

    print("Welcome to the cinema reservation system!")

    name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")
    age = int(input("Enter your age: "))
    num_people = int(input("Enter the number of people (maximum 5): "))

    while num_people < 1 or num_people > 5:
        print("You can reserve between 1 to 5 chairs.")
        num_people = int(input("Enter the number of people (maximum 5): "))

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
if __name__ == "__main__":
    make_reservation()
