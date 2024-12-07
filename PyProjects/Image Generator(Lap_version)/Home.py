from pathlib import Path
from tkinter import Tk, Canvas,  Button, PhotoImage
import Generator2

def show_generation_page(window):
    Generator2.create_generation_page(window)  # Call the function to create the generation page

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()
window.title("Image Generator")
window.geometry("1200x700")
window.configure(bg = "#141414")


canvas = Canvas(
    window,
    bg = "#141414",
    height = 700,
    width = 1200,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1200.0,
    700.0,
    fill="#141414",
    outline="")

canvas.create_text(
    444.0,
    54.0,
    anchor="nw",
    text="Welcome",
    fill="#FFFFFF",
    font=("RocknRollOne Regular", 64 * -1)
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    600.0,
    325.0,
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
    x=458.0,
    y=552.0,
    width=285.0,
    height=70.0
)
window.resizable(False, False)
window.mainloop()
