from PIL import Image, ImageDraw, ImageFont
import os

def create_button(width, height, color, text, filename):
    """Create a button image with specified parameters"""
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw button background
    draw.rounded_rectangle([(0, 0), (width-1, height-1)], radius=10, fill=color)
    
    # Add text
    font_size = 16 if text != "Home" else 14
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except:
        font = ImageFont.load_default()
    
    # Calculate text position to center it
    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    x = (width - text_width) // 2
    y = (height - text_height) // 2
    
    # Draw text
    draw.text((x, y), text, fill='white', font=font)
    
    # Save the image
    image.save(f'assets/frame7/{filename}')

def create_background():
    """Create a background image"""
    width, height = 862, 519
    image = Image.new('RGBA', (width, height), (9, 53, 69, 255))  # #093545
    
    # Add a subtle gradient
    draw = ImageDraw.Draw(image)
    for y in range(height):
        alpha = int(255 * (1 - y/height))
        draw.line([(0, y), (width, y)], fill=(32, 223, 127, alpha//8))  # #20DF7F with varying alpha
    
    image.save('assets/frame7/image_1.png')

def main():
    # Create assets directory if it doesn't exist
    os.makedirs('assets/frame7', exist_ok=True)
    
    # Create buttons
    create_button(191, 34, '#20DF7F', 'Select File', 'button_1.png')
    create_button(191, 34, '#20DF7F', 'Detect', 'button_2.png')
    create_button(91, 34, '#FF0000', 'Home', 'button_3.png')
    
    # Create background
    create_background()

if __name__ == '__main__':
    main() 