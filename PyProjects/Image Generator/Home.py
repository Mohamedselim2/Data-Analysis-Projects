from pathlib import Path
from tkinter import Tk, Canvas,  Button, PhotoImage
import generator

def show_generation_page(window):
    generator.create_generation_page(window)  # Call the function to create the generation page

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame0")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

window = Tk()
window.title("Image Generator")
window.geometry("1920x1080")
window.configure(bg = "#0C0B2B")

canvas = Canvas(
    window,
    bg = "#0C0B2B",
    height = 1080,
    width = 1920,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    4099.0,
    1080.0,
    fill="#141414",
    outline="")

canvas.create_text(
    740.0,
    56.0,
    anchor="nw",
    text="Welcome",
    fill="#FFFFFF",
    font=("RocknRollOne Regular", 96 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    959.0,
    490.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: show_generation_page(window),
    relief="flat"
)

button_1.place(
    x=822.0,
    y=789.0,
    width=285.0,
    height=70.0
)

window.resizable(False, False)
window.mainloop()