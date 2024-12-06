import cv2 # pip install opencv-python
import numpy as np # pip install numpy
import matplotlib.pyplot as plt
from PIL import Image, ImageTk  # Make sure Pillow is imported
from tkinter.filedialog import askopenfilename
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


def upload(canvas):
    
    # Open a file dialog to select the image
    file_path = askopenfilename(
        filetypes=[("Image Files", "*.jpg;*.jpeg;*.png;*.bmp;*.tiff")]
    )
    image_path = file_path
    image = cv2.imread(file_path)
    # Convert the image to RGB (Tkinter doesn't support BGR directly)
    original_image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    # Convert OpenCV images to PIL format
    original_image_pil = Image.fromarray(original_image_rgb)
    # Resize images to fit the rectangles
    original_image_resized = original_image_pil.resize((int(827 - 245), int(745 - 291)))  # Rectangle 1 size
    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    # Display images in the specified rectangles
    canvas.create_image(536, 518, image=original_image_tk, anchor="center")  # Adjust position
    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    return image_path