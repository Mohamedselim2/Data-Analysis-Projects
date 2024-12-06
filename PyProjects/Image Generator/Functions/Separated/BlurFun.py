import cv2 # pip install opencv-python
from PIL import Image, ImageTk  # Make sure Pillow is imported
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

def apply_blur(canvas, file_path):
    # Check if a file was selected
    if not file_path:
        messagebox.showerror("File Error", "No file selected.")  # Show a pop-up error
        return

    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("Error: Image not loaded correctly.")
        return

    # Convert the image to RGB (Tkinter doesn't support BGR directly)
    original_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # Apply a blur filter
    blurred_image = cv2.blur(image, (5, 5))
    blurred_image_rgb = cv2.cvtColor(blurred_image, cv2.COLOR_BGR2RGB)

    # Convert OpenCV images to PIL format
    original_image_pil = Image.fromarray(original_image_rgb)
    blurred_image_pil = Image.fromarray(blurred_image_rgb)

    # Resize images to fit the rectangles
    original_image_resized = original_image_pil.resize((int(827 - 245), int(745 - 291)))  # Rectangle 1 size
    blurred_image_resized = blurred_image_pil.resize((int(1675 - 1093), int(745 - 291)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    blurred_image_tk = ImageTk.PhotoImage(blurred_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(536, 518, image=original_image_tk, anchor="center")  # Adjust position
    canvas.create_image(1384, 518, image=blurred_image_tk, anchor="center")  # Adjust position

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_blurred = blurred_image_tk