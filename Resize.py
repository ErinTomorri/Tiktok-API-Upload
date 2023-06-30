import os
from PIL import Image

def resize_images(folder_path, target_size):
    print (os.listdir(folder_path))
    for filename in os.listdir(folder_path):
        print(filename)
        if filename.endswith(".JPG") or filename.endswith(".JPEG") or filename.endswith(".PNG") or filename.endswith(".jpg") or filename.endswith(".jpeg") or filename.endswith(".png"):
            image_path = os.path.join(folder_path, filename)
            try:
                image = Image.open(image_path)
                resized_image = image.resize(target_size)
                resized_image.save(image_path)
                print(f"Resized image: {filename}")
            except Exception as e:
                print(f"Error resizing image: {filename}")
                print(str(e))

# Example usage
folder_path = "Image/Random copy"  # Specify the path to your folder containing the images
target_size = (400, 400)  # Specify the target size in pixels (width, height)
resize_images(folder_path, target_size)
