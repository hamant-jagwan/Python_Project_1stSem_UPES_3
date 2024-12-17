import os
from PIL import Image

# Set the input and output directories
input_dir = r'H:\1st_sem_Python_Project\Project_3\Input_Pic'
output_dir = r'H:\1st_sem_Python_Project\Project_3\Resized_Pic'

# Create the output directory if it doesn't exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Define the new size for the images
new_width = 800
new_height = 600

def resize_image(input_path, output_path, size):
    with Image.open(input_path) as img:
        img = img.resize(size, Image.LANCZOS)
        img.save(output_path)

# List all files in the input directory
for filename in os.listdir(input_dir):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        input_path = os.path.join(input_dir, filename)
        output_path = os.path.join(output_dir, filename)
        
        resize_image(input_path, output_path, (new_width, new_height))
        
        print(f"Resized and saved {filename}")

print("All images have been resized and saved to the output directory.")


