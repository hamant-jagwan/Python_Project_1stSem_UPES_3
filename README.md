# Image Resizer

This project involves creating a script that resizes images in a directory using Python's Pillow library along with `os.listdir()` for directory handling.

## Screenshot

![alt text](<Screenshot 2024-12-17 175747.png>)

## Features

- Resize images to a specified width and height
- Maintain the aspect ratio of images (optional)
- Batch processing of all images in a directory
- Save resized images to a specified output directory

## Requirements

- Python 3.x
- Pillow library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/hamant-jagwan/Python_Project_1stSem_UPES_3/blob/main/Resize.py
    ```

2. Navigate to the project directory:
    ```sh
    cd image-resizer
    ```

3. Install the required Python packages:
    ```sh
    pip install Pillow
    ```

## Usage

1. **Set Up Directories:**
    - Create a folder named `Input_Pic` inside your `Project_3` directory and place the images you want to resize into this folder.

2. **Run the Script:**
    - Execute the script to resize images:
    ```sh
    python Resize.py
    ```

3. **Verify Output:**
    - The resized images will be saved in the `Resized_Pic` directory.

## Project Structure

- `Resize.py`: Main script containing the code for resizing images.

## Code Overview

1. **Importing Necessary Libraries:**
   - The script imports the `Pillow` library (specifically `PIL.Image`) for image processing and the `os` library for directory handling.

2. **Setting Input and Output Directories:**
   - The `input_dir` is set to the path of the directory containing the images to be resized.
   - The `output_dir` is set to the path of the directory where resized images will be saved.

3. **Creating Output Directory:**
   - The script checks if the output directory exists and creates it if it doesn't.

4. **Defining New Size:**
   - The images will be resized to 800x600 pixels by default.

5. **Resize Function:**
   - The `resize_image` function opens, resizes, and saves the image using the `Image.LANCZOS` filter for high-quality downsampling.

6. **Processing Images:**
   - The script lists all files in the input directory, filters for image files (e.g., `.jpg`, `.jpeg`, `.png`), and resizes each image.

## Example Code
Here's a high-level overview of the steps involved in the script:

1. **Import Libraries**
2. **Set Directories**
3. **Create Output Directory**
4. **Define Resize Function**
5. **Process Images**



