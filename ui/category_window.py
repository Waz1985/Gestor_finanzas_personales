import FreeSimpleGUI as sg

def create_category_window():
    layout = [
        [sg.Text("Category name")],
        [sg.Input(key="-CATEGORY-")],
<<<<<<< HEAD
        [sg.Text("Color")],
        [sg.ColorChooserButton("Choose color", target="-COLOR-INPUT-")],
        [sg.Input(key="-COLOR-INPUT-", visible=False)],
=======
>>>>>>> 5ffba0d3c4643ecb282352d5bf2d92b6faa91972
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    return sg.Window(
        "Add Category",
        layout,
        modal=True,
        finalize=True
    )
