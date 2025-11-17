from PIL import Image, ImageOps, ImageFilter, ImageEnhance, ImageChops
import numpy as np

def dodge(front, back):
    result = front * 255 / (255 - back)
    result[result > 255] = 255
    result[back == 255] = 255
    return result.astype('uint8')

def enhance_edges(image):
    edges = image.filter(ImageFilter.FIND_EDGES)
    edges = ImageOps.invert(edges)
    return edges

def pencil_sketch(image_path, output_path):
    try:
        # Open the original image
        image = Image.open(image_path)

        # Convert the image to grayscale
        gray_image = ImageOps.grayscale(image)

        # Invert the grayscale image
        inverted_image = ImageOps.invert(gray_image)

        # Blur the inverted image
        blurred_image = inverted_image.filter(ImageFilter.GaussianBlur(10))

        # Convert images to numpy arrays for manipulation
        gray_array = np.asarray(gray_image).astype('float64')
        blurred_array = np.asarray(blurred_image).astype('float64')

        # Apply the custom dodge function
        result_array = dodge(gray_array, blurred_array)

        # Convert the result array back to an image
        pencil_sketch_image = Image.fromarray(result_array)

        # Enhance the edges
        edges = enhance_edges(gray_image)

        # Blend the pencil sketch image with the edges
        pencil_sketch_image = ImageChops.multiply(pencil_sketch_image, edges)

        # Save the result
        pencil_sketch_image.save(output_path)

        print(f"The image was successfully converted to a pencil sketch and saved as {output_path}.")

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage with user input
image_path = input("Enter the image file name or path: ")
output_path = input("Enter the output file name or path: ")
pencil_sketch(image_path, output_path)

