from reservation_manager import load_reservations

def check_user_reservation(name, last_name):
    reservations = load_reservations()
    for reservation in reservations:
        if reservation["name"].lower() == name.lower() and reservation["last_name"].lower() == last_name.lower():
            num_chairs = len(reservation["chair_numbers"])
            print(f"{name} {last_name} has reserved {num_chairs} chair(s).")
            return
    print(f"No reservation found for {name} {last_name}.")

def check_empty_chairs():
    all_chairs = set(range(1, 101))
    reservations = load_reservations()
    reserved_chairs = {chair for reservation in reservations for chair in reservation["chair_numbers"]}
    empty_chairs = all_chairs - reserved_chairs
    print(f"Empty chairs: {sorted(empty_chairs)}")

if __name__ == "__main__":
    print("Choose an option:")
    print("1. Check a reservation")
    print("2. Check empty chairs")
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        name = input("Enter the first name: ")
        last_name = input("Enter the last name: ")
        check_user_reservation(name, last_name)
    elif choice == "2":
        check_empty_chairs()
    else:
        print("Invalid choice. Please enter 1 or 2.")
