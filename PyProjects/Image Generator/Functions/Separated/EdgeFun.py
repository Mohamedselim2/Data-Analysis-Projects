import cv2
from PIL import Image, ImageTk
from tkinter import messagebox

def apply_edge_detection(canvas, file_path):

    # Check if a file was selected
    if not file_path:
        messagebox.showerror("File Error", "No file selected.")  # Show a pop-up error
        return

    # Read the image
    image = cv2.imread(file_path)
    if image is None:
        messagebox.showerror("File Error", "Image not loaded correctly.")  # Show a pop-up error
        return

    # Convert the image to grayscale
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply Canny edge detection
    edges = cv2.Canny(gray_image, 100, 200)

    # Convert OpenCV images to PIL format
    original_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    original_image_pil = Image.fromarray(original_image_rgb)
    edges_image_pil = Image.fromarray(edges)

    # Resize images to fit the rectangles
    original_image_resized = original_image_pil.resize((int(827 - 245), int(745 - 291)))  # Rectangle 1 size
    edges_image_resized = edges_image_pil.resize((int(1675 - 1093), int(745 - 291)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    edges_image_tk = ImageTk.PhotoImage(edges_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(536, 518, image=original_image_tk, anchor="center")  # Original image
    canvas.create_image(1384, 518, image=edges_image_tk, anchor="center")  # Edge-detected image

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_edges = edges_image_tk