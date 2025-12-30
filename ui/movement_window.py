<<<<<<< HEAD
from datetime import date
import FreeSimpleGUI as sg



def create_movement_window(categories, movement_type):
    today = date.today().isoformat() 

    layout = [
        [sg.Text(f"Add {movement_type}")],
        [sg.Text("Date (YYYY-MM-DD)"), sg.Input(default_text=today, key="-DATE-")],
=======
import FreeSimpleGUI as sg

def create_movement_window(categories, movement_type):
    layout = [
        [sg.Text(f"Add {movement_type}")],
        [sg.Text("Date (YYYY-MM-DD)"), sg.Input(key="-DATE-")],
>>>>>>> 5ffba0d3c4643ecb282352d5bf2d92b6faa91972
        [sg.Text("Title"), sg.Input(key="-TITLE-")],
        [sg.Text("Amount"), sg.Input(key="-AMOUNT-")],
        [sg.Text("Category"), sg.Combo(categories, key="-CATEGORY-", readonly=True)],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    return sg.Window(
        f"Add {movement_type}",
        layout,
        modal=True,
        finalize=True
    )

