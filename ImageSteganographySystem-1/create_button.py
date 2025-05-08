from PIL import Image, ImageDraw, ImageFont
import os

def create_button_image():
    # Create a new image with a transparent background
    width = 191
    height = 69
    image = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    draw = ImageDraw.Draw(image)
    
    # Draw button background (matching the style of other buttons)
    draw.rounded_rectangle([(0, 0), (width-1, height-1)], radius=10, fill='#20DF7F')
    
    # Add text
    text = "Detect"
    font_size = 24
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
    
    # Create assets/frame3 directory if it doesn't exist
    os.makedirs('assets/frame3', exist_ok=True)
    
    # Save the image
    image.save('assets/frame3/button_4.png')

if __name__ == '__main__':
    create_button_image() 