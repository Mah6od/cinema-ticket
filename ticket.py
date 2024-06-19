from PIL import Image, ImageDraw, ImageFont
import os

TICKET_FOLDER = "tickets"

# Create a folder for ticket images if it doesn't exist
if not os.path.exists(TICKET_FOLDER):
    os.makedirs(TICKET_FOLDER)

def generate_ticket_image(name, last_name, age, chair_numbers):
    width, height = 400, 200 + 30 * len(chair_numbers)
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

    # Save the ticket image in the tickets folder
    ticket_file = os.path.join(TICKET_FOLDER, f"ticket_{name}_{last_name}.png")
    ticket.save(ticket_file)
    print(f"Ticket saved as {ticket_file}")
