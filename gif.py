import imageio.v2 as imageio
import os
from PIL import Image

def create_gif(images, output_file, duration=0.5):
    images = [imageio.imread(image) for image in images]
    imageio.mimsave(output_file, images, 'GIF', duration=duration)

def main():
    # Set the input and output file paths
    input_folder = 'input_images'
    output_file = 'output.gif'

    # Check if the input folder exists
    if not os.path.exists(input_folder):
        print(f"Error: The input folder '{input_folder}' does not exist.")
        return

    # Get the list of image files in the input folder
    images = [os.path.join(input_folder, file) for file in os.listdir(input_folder) if file.endswith('.png') or file.endswith('.jpg')]

    # Resize images
    image_size = (700, 500)
    for image in images:
        img = Image.open(image)
        img = img.resize(image_size)
        img.save(image)

    # Convert images to RGB format
    for image in images:
        img = Image.open(image)
        img = img.convert('RGB')
        img.save(image)

    # Create the GIF
    create_gif(images, output_file)

if __name__ == '__main__':
    main()