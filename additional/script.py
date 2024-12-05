from PIL import Image
import os

# Specify the directory containing the images for the dictionary
image_directory = "../resized"

# Dictionary to store image names and their dimensions
image_dimensions = {}

# Populate the dictionary with image names and their dimensions
for filename in os.listdir(image_directory):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.tiff')):  # Supported formats
        image_path = os.path.join(image_directory, filename)
        try:
            with Image.open(image_path) as img:
                width, height = img.size
                # Store the data in the dictionary
                image_dimensions[filename] = (height, width)
        except Exception as e:
            print(f"Error processing {filename}: {e}")

# Print the dimensions for reference
print("Available images and their dimensions:")
for name, dimensions in image_dimensions.items():
    print(f"Image: {name} | Dimensions: {dimensions}")

# Input: Path to the image you want to resize
input_image_path = input("\nEnter the path to the image you want to resize: ")

# Input: Name of the reference image from the dictionary
reference_image_name = input("Enter the name of the reference image: ")

# Check if the reference image exists in the dictionary
if reference_image_name not in image_dimensions:
    print(f"Error: The reference image '{reference_image_name}' is not in the dictionary.")
else:
    try:
        # Get the dimensions of the reference image
        ref_height, ref_width = image_dimensions[reference_image_name]

        # Open and resize the input image
        with Image.open(input_image_path) as img:
            resized_img = img.resize((ref_width, ref_height))

            # Save the resized image
            output_path = os.path.join(os.path.dirname(input_image_path),
                                       f"resized_{os.path.basename(input_image_path)}")
            resized_img.save(output_path)
            print(f"Image resized successfully and saved as: {output_path}")
    except Exception as e:
        print(f"Error resizing the image: {e}")
