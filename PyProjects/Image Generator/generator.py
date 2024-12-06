from tkinter.filedialog import askopenfilename
from pathlib import Path
import tkinter as tk
from tkinter import Canvas, Button, PhotoImage
from Functions import Master

def create_generation_page(parent):
    OUTPUT_PATH = Path(__file__).parent
    ASSETS_PATH = OUTPUT_PATH / Path(r"assets\frame1")

    def relative_to_assets(path: str) -> Path:
        return ASSETS_PATH / Path(path)


    # Define a variable to store the return value
    uploaded_image_path = {"path": None}  # Use a mutable object to store the value
    # Helper function to store the return value
    def handle_upload(canvas):
        uploaded_image_path["path"] = Master.upload(canvas)  # Call the function and store its return value
        print(f"Uploaded file path: {uploaded_image_path['path']}")  # Debug or use the value


    window = tk.Frame(parent)
    window.pack(fill="both", expand=True)

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
        15.0,
        4099.0,
        1095.0,
        fill="#161616",
        outline="")

    canvas.create_rectangle(
        0.0,
        0.0,
        1920.0,
        113.0,
        fill="#1E1E2A",
        outline="")

    canvas.create_rectangle(
        243.0,
        234.0137455261438,
        532.0000459449166,
        237.0,
        fill="#FFFFFF",
        outline="")

    canvas.create_text(
        246.0,
        176.0,
        anchor="nw",
        text="Generate Image",
        fill="#FFFFFF",
        font=("Roboto Bold", 40 * -1)
    )

    canvas.create_rectangle(
        1093.0,
        291.0,
        1675.0,
        745.0,
        fill="#D9D9D9",
        outline="")

    canvas.create_rectangle(
        246.0,
        291.0,
        828.0,
        745.0,
        fill="#D9D9D9",
        outline="")

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"))
    button_1 = Button(
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: handle_upload(canvas),
        relief="flat"
    )
    button_1.place(
        x=458.0,
        y=799.0,
        width=157.0,
        height=46.0
    )


    button_image_2 = PhotoImage(
        file=relative_to_assets("button_2.png"))
    button_2 = Button(
        image=button_image_2,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Master.apply_blur(canvas, uploaded_image_path['path']),
        relief="flat"
    )
    button_2.place(
        x=873.0,
        y=395.0,
        width=175.0,
        height=56.0
    )

    button_image_3 = PhotoImage(
        file=relative_to_assets("button_3.png"))
    button_3 = Button(
        image=button_image_3,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Master.apply_edge_detection(canvas,  uploaded_image_path['path']),
        relief="flat"
    )
    button_3.place(
        x=873.0,
        y=531.0,
        width=175.0,
        height=56.0
    )

    button_image_4 = PhotoImage(
        file=relative_to_assets("button_4.png"))
    button_4 = Button(
        image=button_image_4,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Master.apply_median(canvas,  uploaded_image_path['path']),
        relief="flat"
    )
    button_4.place(
        x=873.0,
        y=463.0,
        width=175.0,
        height=56.0
    )

    button_image_5 = PhotoImage(
        file=relative_to_assets("button_5.png"))
    button_5 = Button(
        image=button_image_5,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: Master.apply_negative(canvas,  uploaded_image_path['path']),
        relief="flat"
    )
    button_5.place(
        x=873.0,
        y=599.0,
        width=175.0,
        height=56.0
    )

    image_image_1 = PhotoImage(
        file=relative_to_assets("image_1.png"))
    image_1 = canvas.create_image(
        287.0,
        53.0,
        image=image_image_1
    )
    window.mainloop()