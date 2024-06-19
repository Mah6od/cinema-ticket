from reservation_manager import load_reservations
from PIL import Image, ImageDraw, ImageFont
import os

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

    # Image parameters
    width, height = 1000, 1000
    square_size = 90  # Adjust the size of each square
    spacing = 10      # Space between squares

    cols = 10
    rows = 10

    img = Image.new("RGB", (width, height), "gray")
    draw = ImageDraw.Draw(img)

    # Load a larger font
    try:
        font = ImageFont.truetype("arial.ttf", 18)  
    except IOError:
        font = ImageFont.load_default()

    # Draw the squares
    for row in range(rows):
        for col in range(cols):
            chair_number = row * cols + col + 1
            x1 = col * (square_size + spacing)
            y1 = row * (square_size + spacing)
            x2 = x1 + square_size
            y2 = y1 + square_size
            if chair_number in reserved_chairs:
                draw.rectangle([x1, y1, x2, y2], fill="green")
            else:
                draw.rectangle([x1, y1, x2, y2], fill="gray")
            # Adjust the text position to be more visible
            text_position = (x1 + (square_size - font.getsize(str(chair_number))[0]) // 2, y1 + (square_size - font.getsize(str(chair_number))[1]) // 2)
            draw.text(text_position, str(chair_number), font=font, fill="black")

    # Save the image
    if not os.path.exists("chairs"):
        os.makedirs("chairs")
    image_path = "chairs/seat_chart.png"
    img.save(image_path)
    print(f"Chair chart saved as {image_path}")

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
