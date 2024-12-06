import cv2 # pip install opencv-python
from PIL import Image, ImageTk  # Make sure Pillow is imported
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def apply_median(canvas, file_path):
    # Check if a file was selected
    if not file_path:
        messagebox.showerror("File Error", "No file selected.")  # Show a pop-up error
        return

    # Read the image in grayscale
    image = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
    if image is None:
        messagebox.showerror("Error: Image not loaded correctly.")
        return

    # Get the negative of the image
    negative_image = 255 - image

    # Convert OpenCV images to PIL format
    original_image_pil = Image.fromarray(image)
    negative_image_pil = Image.fromarray(negative_image)

    # Resize images to fit the rectangles
    original_image_resized = original_image_pil.resize((int(827 - 245), int(745 - 291)))  # Rectangle 1 size
    negative_image_resized = negative_image_pil.resize((int(1675 - 1093), int(745 - 291)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    negative_image_tk = ImageTk.PhotoImage(negative_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(536, 518, image=original_image_tk, anchor="center")  # Original image
    canvas.create_image(1384, 518, image=negative_image_tk, anchor="center")  # Negative image

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_negative = negative_image_tk
