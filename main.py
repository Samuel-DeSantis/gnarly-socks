from PIL import Image, ImageGrab
import pytesseract
from pdf2image import convert_from_path

# images = convert_from_path('test_drawing.pdf')

# Save each image as a separate file
# for i, image in enumerate(images):
    # image.save(f'output_{i}.png', 'PNG')

custom_config = r'--oem 3 --psm 3'

print(pytesseract.image_to_string(Image.open("output_0.png"), lang='eng', config=custom_config))