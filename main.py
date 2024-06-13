
from PIL import Image, ImageDraw, ImageFont

def generate_circle_image(n, size, m1, m2):
    width, height = size
    # Create a transparent canvas
    image = Image.new('RGBA', size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(image)

    # Calculate the circle's bounding box
    bbox = [0, 0, width, height]
    
    # Draw a red circle
    draw.ellipse(bbox, outline='red', fill='red')

    # Load a font
    try:
        font_large = ImageFont.truetype("arial.ttf", int(min(width, height) * 0.3))  # Large font for number
        font_small = ImageFont.truetype("arial.ttf", int(min(width, height) * 0.05))  # Small font for m1 and m2
    except IOError:
        # Fallback if the truetype font isn't found
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()

    # Calculate text size and position for 'n'
    text_n_width, text_n_height = draw.textsize(str(n), font=font_large)
    text_n_x = (width - text_n_width) // 2
    text_n_y = (height - text_n_height) // 2

    # Calculate text size and position for 'm1'
    text_m1_width, text_m1_height = draw.textsize(m1, font=font_small)
    text_m1_x = (width - text_m1_width) // 2
    text_m1_y = (height * 0.15) - (text_m1_height // 2)

    # Calculate text size and position for 'm2'
    text_m2_width, text_m2_height = draw.textsize(m2, font=font_small)
    text_m2_x = (width - text_m2_width) // 2
    text_m2_y = height - (height * 0.15) - (text_m2_height // 2)

    # Draw the texts on the image
    draw.text((text_n_x, text_n_y), str(n), fill="white", font=font_large)
    draw.text((text_m1_x, text_m1_y), m1, fill="white", font=font_small)
    draw.text((text_m2_x, text_m2_y), m2, fill="white", font=font_small)

    return image

# Example usage
image = generate_circle_image(123, (500, 500), 'upper', 'lower')
image.show()