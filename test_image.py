from PIL import Image, ImageDraw

def create_image_with_border_and_marks(width, height, border_color, mark_color, background_color):
    # Create a new image with a white background
    img = Image.new('RGB', (width, height), background_color)
    draw = ImageDraw.Draw(img)

    # Draw 1px border around the image
    draw.rectangle([0, 0, width-1, height-1], outline=border_color)

    # Draw corner marks 10px away from the edges
    # Top-left corner
    draw.line([(10, 0), (10, 10)], fill=mark_color)
    draw.line([(0, 10), (10, 10)], fill=mark_color)

    # Top-right corner
    draw.line([(width-11, 0), (width-11, 10)], fill=mark_color)
    draw.line([(width-1, 10), (width-11, 10)], fill=mark_color)

    # Bottom-left corner
    draw.line([(0, height-11), (10, height-11)], fill=mark_color)
    draw.line([(10, height-1), (10, height-11)], fill=mark_color)

    # Bottom-right corner
    draw.line([(width-11, height-1), (width-11, height-11)], fill=mark_color)
    draw.line([(width-1, height-11), (width-11, height-11)], fill=mark_color)

    return img

# Define the image size and colors
width = 1920
height = 1080
border_color = 'black'
mark_color = 'black'
background_color = 'white'

# Create the image
img = create_image_with_border_and_marks(width, height, border_color, mark_color, background_color)

# Save the image to a file
img.save('output_image.png')