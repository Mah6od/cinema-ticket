from PIL import Image, ImageDraw, ImageFont
import os
import random

TICKET_FOLDER = "tickets"
CHARACTER_FOLDER = "characters"

# Create a folder for ticket images if it doesn't exist
if not os.path.exists(TICKET_FOLDER):
    os.makedirs(TICKET_FOLDER)

def get_random_character_image(gender):
    folder = os.path.join(CHARACTER_FOLDER, gender)
    if not os.path.exists(folder):
        raise FileNotFoundError(f"The folder {folder} does not exist.")
    
    images = [os.path.join(folder, img) for img in os.listdir(folder) if img.endswith(('.png', '.jpg', '.jpeg'))]
    if not images:
        raise FileNotFoundError(f"No images found in the folder {folder}.")
    
    return random.choice(images)

def generate_ticket_image(name, last_name, age, chair_numbers, gender):
    width, height = 500, 200 + 30 * len(chair_numbers)  # Increased width to accommodate character image
    ticket = Image.new("RGB", (width, height), "white")
    draw = ImageDraw.Draw(ticket)

    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    draw.text((10, 10), f"Cinema Ticket", font=font, fill="black")
    draw.text((10, 40), f"Name: {name} {last_name}", font=font, fill="black")
    draw.text((10, 70), f"Age: {age}", font=font, fill="black")
    draw.text((10, 100), f"Chairs: {', '.join(map(str, chair_numbers))}", font=font, fill="black")

    # Add character image
    try:
        character_image_path = get_random_character_image(gender)
        character_image = Image.open(character_image_path).resize((100, 100), Image.ANTIALIAS)
        ticket.paste(character_image, (width - 110, 10))  # 10 pixels padding from the right edge
    except FileNotFoundError as e:
        print(e)

    # Save the ticket image in the tickets folder
    ticket_file = os.path.join(TICKET_FOLDER, f"ticket_{name}_{last_name}.png")
    ticket.save(ticket_file)
    print(f"Ticket saved as {ticket_file}")
