import random
from PIL import Image, ImageDraw, ImageFont

# List of people in the secret santa, and their exclusions
list = {
    "people": ["Charlie", "Richard", "Laura", "Chelsea", "Miranda"],
    "exclusions": [
        {"Charlie": "Laura"},
        {"Laura": "Charlie"},
        {"Richard": "Chelsea"},
        {"Chelsea": "Richard"}
    ]
}

# Check if a gifter is excluded from a recipient


def is_excluded(person, recipient, exclusions):
    for exclusion in exclusions:
        if person in exclusion:
            if recipient == exclusion[person]:
                return True
    return False

# Generate the secret santa unidirectional pairs


def generate_pairs(list):
    pairs = {}
    match = True
    while match:
        recipients = list["people"].copy()
        gifters = list["people"].copy()
        exclusions = list["exclusions"].copy()
        random.shuffle(recipients)
        random.shuffle(gifters)
        for gifter in gifters:
            for recipient in recipients:
                if recipient != gifter and not is_excluded(gifter, recipient, exclusions):
                    pairs[gifter] = recipient
                    recipients.remove(pairs[gifter])
                    break
        if len(pairs) == len(gifters):
            match = False
    return pairs

# Create an image of the secret santa pair text


def create_image_from_text(text, output_file):
    font = ImageFont.truetype("arial.ttf", 20)
    img = Image.new("RGB", (500, 500), color="white")
    draw = ImageDraw.Draw(img)
    draw.text((10, 10), text, font=font, fill=(0, 0, 0))
    img.save(output_file + ".png")


def main():
    for key, value in generate_pairs(list).items():
        create_image_from_text(key + " is buying for " + value, key)


if __name__ == "__main__":
    main()
