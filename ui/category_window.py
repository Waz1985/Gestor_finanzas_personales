import FreeSimpleGUI as sg

def create_category_window():
    layout = [
        [sg.Text("Category name")],
        [sg.Input(key="-CATEGORY-")],
        [sg.Button("Save"), sg.Button("Cancel")]
    ]

    return sg.Window(
        "Add Category",
        layout,
        modal=True,
        finalize=True
    )
