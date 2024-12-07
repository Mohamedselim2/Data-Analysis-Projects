import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

def apply_negative(canvas, file_path):

    # Check if a file was selected
    if not file_path:
        messagebox.showerror("File Error", "No file selected.")  # Show a pop-up error
        return

    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("File Error", "Image not loaded correctly.")  # Show a pop-up error
        return

    # Get the dimensions of the image
    height, width, _ = image.shape

    # Apply the negative transformation pixel by pixel
    for i in range(height):
        for j in range(width):
            image[i, j] = 255 - image[i, j]

    # Convert OpenCV image to RGB for Tkinter compatibility
    original_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    original_image_pil = Image.fromarray(original_image_rgb)

    # Resize image to fit canvas rectangles
    resized_image = original_image_pil.resize((int(1675 - 1093), int(745 - 291)))  # Example rectangle size

    # Convert to ImageTk format
    image_tk = ImageTk.PhotoImage(resized_image)

    # Display the negative transformed image on the canvas
    canvas.create_image(1384, 518, image=image_tk, anchor="center")  # Adjust the coordinates as needed

    # Save references to avoid garbage collection
    canvas.image_negative = image_tk
