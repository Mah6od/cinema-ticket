from reservation_manager import load_reservations

def check_user_reservation(name, last_name):
    reservations = load_reservations()
    for reservation in reservations:
        if reservation["name"].lower() == name.lower() and reservation["last_name"].lower() == last_name.lower():
            num_chairs = len(reservation["chair_numbers"])
            print(f"{name} {last_name} has reserved {num_chairs} chair(s).")
            return
    print(f"No reservation found for {name} {last_name}.")

if __name__ == "__main__":
    name = input("Enter the first name: ")
    last_name = input("Enter the last name: ")
    check_user_reservation(name, last_name)
