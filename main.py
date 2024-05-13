# This program will help you remove background from your image

# Libs for working with images
from rembg import remove
from PIL import Image

# Just for decoration
from pyfiglet import Figlet

import os

def main():
    # Decorate console
    f = Figlet(font='slant')
    print(f.renderText('BG-Remover'))

    # Locate current directory and scan it
    directory = os.curdir
    files = os.listdir(directory)

    # Using loop get each file
    for file in files:
        # Split file
        filename,extension = os.path.splitext(file)

        # Remove background if file has correct extension for removing
        if extension.lower() in ['.png', '.jpg', '.jpeg']:
            # Create output filename
            output = f'{filename}_removed.png'

            # Locate current directory
            input_file = os.path.join(directory, file)
            output_file = os.path.join(directory, output)

            # Use remove_background() func to remove background
            if remove_background(input_file, output_file):
                # If everything correct, notify user
                print(f'Background removed from {file}. Result saved as {output}')
            else:
                print(f'Something went wrong..')

'''
    This function will use this params:
    - input_path: file path to be modified
    - output_path: modified file to save
'''
def remove_background(input_path, output_path):
    try:
        # Open the file using PIL
        img = Image.open(input_path)

        # Use rembg lib remove background from the image and save it
        output = remove(img)
        output.save(output_path)

        return True
    
    except Exception as e:
        return False

if __name__ == "__main__":
    main()