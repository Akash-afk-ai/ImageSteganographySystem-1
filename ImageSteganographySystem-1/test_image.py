from PIL import Image, ImageDraw

# Create a simple test image
img = Image.new('RGB', (100, 100), color='white')
draw = ImageDraw.Draw(img)
draw.rectangle([(20, 20), (80, 80)], fill='blue')
img.save('test_image.png')

print("Test image created successfully!") 