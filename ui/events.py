import FreeSimpleGUI as sg

def event_add_expense(manager, create_movement_window, save_movements, MOVEMENTS_PATH, window, build_table_data):
    category_names = [c.name for c in manager.categories]
    mov_window = create_movement_window(category_names, "EXPENSE")

    while True:
        mov_event, mov_values = mov_window.read()

        if mov_event in (None, "Cancel"):
            break

        if mov_event == "Save":
            try:
                manager.add_movement(
                    mov_values["-DATE-"],
                    mov_values["-TITLE-"],
                    mov_values["-AMOUNT-"],
                    mov_values["-CATEGORY-"],
                    "EXPENSE"
                )

                save_movements(MOVEMENTS_PATH, manager.movements)

                # 🔄 refrescar tabla
                window["-TABLE-"].update(
                    values=build_table_data(manager.movements)
                )

                break

            except (ValueError, TypeError) as e:
                sg.popup_error(str(e))

    mov_window.close()

def event_add_income(manager, create_movement_window, save_movements, MOVEMENTS_PATH, window, build_table_data):
    category_names = [c.name for c in manager.categories]
    mov_window = create_movement_window(category_names, "INCOME")

    while True:
        mov_event, mov_values = mov_window.read()

        if mov_event in (None, "Cancel"):
            break

        if mov_event == "Save":
            try:
                manager.add_movement(
                    mov_values["-DATE-"],
                    mov_values["-TITLE-"],
                    mov_values["-AMOUNT-"],
                    mov_values["-CATEGORY-"],
                    "INCOME"
                )

                save_movements(MOVEMENTS_PATH, manager.movements)

                window["-TABLE-"].update(
                    values=build_table_data(manager.movements)
                )

                break

            except (ValueError, TypeError) as e:
                sg.popup_error(str(e))

    mov_window.close()

def event_add_category(manager, cat_window, Category, save_categories, CATEGORIES_PATH):
    while True:
        cat_event, cat_values = cat_window.read()

        if cat_event in (None, "Cancel"):
            break

        if cat_event == "Save":
            try:
                name = cat_values["-CATEGORY-"]
                category = Category(name)
                manager.add_category(category)

                save_categories(CATEGORIES_PATH, manager.categories)

                break

            except ValueError as e:
                sg.popup_error(str(e))

    cat_window.close()