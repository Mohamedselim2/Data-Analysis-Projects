import cv2 # pip install opencv-python
from PIL import Image, ImageTk  # Make sure Pillow is imported
from tkinter.filedialog import askopenfilename
from tkinter import messagebox

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
    original_image_resized = original_image_pil.resize((int(486 - 46), int(587 - 227)))  # Rectangle 1 size
    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    # Display images in the specified rectangles
    canvas.create_image(266, 407, image=original_image_tk, anchor="center")  # Adjust position
    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    return image_path

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
    original_image_resized = original_image_pil.resize((int(486 - 46), int(587 - 227)))  # Rectangle 1 size
    blurred_image_resized = blurred_image_pil.resize((int(1155 - 715), int(587 - 227)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    blurred_image_tk = ImageTk.PhotoImage(blurred_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(266, 407, image=original_image_tk, anchor="center")  # Adjust position
    canvas.create_image(935, 407, image=blurred_image_tk, anchor="center")  # Adjust position

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_blurred = blurred_image_tk

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
    original_image_resized = original_image_pil.resize((int(486 - 46), int(587 - 227)))  # Rectangle 1 size
    edges_image_resized = edges_image_pil.resize((int(1155 - 715), int(587 - 227)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    edges_image_tk = ImageTk.PhotoImage(edges_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(266, 407, image=original_image_tk, anchor="center")  # Original image
    canvas.create_image(935, 407, image=edges_image_tk, anchor="center")  # Edge-detected image

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_edges = edges_image_tk

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
    original_image_resized = original_image_pil.resize((int(486 - 46), int(587 - 227)))  # Rectangle 1 size
    negative_image_resized = negative_image_pil.resize((int(1155 - 715), int(587 - 227))) # Rectangle 2 size

    # Convert PIL images to ImageTk format
    original_image_tk = ImageTk.PhotoImage(original_image_resized)
    negative_image_tk = ImageTk.PhotoImage(negative_image_resized)

    # Display images in the specified rectangles
    canvas.create_image(266, 407, image=original_image_tk, anchor="center")  # Original image
    canvas.create_image(935, 407, image=negative_image_tk, anchor="center")  # Negative image

    # Save references to avoid garbage collection
    canvas.image_original = original_image_tk
    canvas.image_negative = negative_image_tk
    # Resize images to fit the rectangles
    # original_image_resized = original_image_pil.resize((int(486 - 46), int(587 - 227)))  # Rectangle 1 size
    negative_image_resized = negative_image_pil.resize((int(1155 - 715), int(587 - 227)))  # Rectangle 2 size

    # Convert PIL images to ImageTk format
    # original_image_tk = ImageTk.PhotoImage(original_image_resized)
    negative_image_tk = ImageTk.PhotoImage(negative_image_resized)

    # Display images in the specified rectangles
    # canvas.create_image(266, 407, image=original_image_tk, anchor="center")  # Original image
    canvas.create_image(935, 407, image=negative_image_tk, anchor="center")  # Negative image

    # Save references to avoid garbage collection
    # canvas.image_original = original_image_tk
    canvas.image_negative = negative_image_tk

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
    resized_image = original_image_pil.resize((int(1155 - 715), int(587 - 227))) # Example rectangle size

    # Convert to ImageTk format
    image_tk = ImageTk.PhotoImage(resized_image)

    # Display the negative transformed image on the canvas
    canvas.create_image(935, 407, image=image_tk, anchor="center")  # Adjust the coordinates as needed

    # Save references to avoid garbage collection
    canvas.image_negative = image_tk