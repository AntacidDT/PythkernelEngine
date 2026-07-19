import dearpygui.dearpygui as dpg


def build_menu_bar():
    with dpg.menu_bar():
        with dpg.menu(label="File"):
            dpg.add_menu_item(label="New Project")
            dpg.add_menu_item(label="Open Project")
            dpg.add_menu_item(label="Save")
            dpg.add_menu_item(label="Save As")
            dpg.add_separator()
            dpg.add_menu_item(label="Exit")

        with dpg.menu(label="Edit"):
            dpg.add_menu_item(label="Undo")
            dpg.add_menu_item(label="Redo")
            dpg.add_separator()
            dpg.add_menu_item(label="Preferences")

        with dpg.menu(label="View"):
            dpg.add_menu_item(label="Explorer")
            dpg.add_menu_item(label="Properties")
            dpg.add_menu_item(label="Terminal")

        with dpg.menu(label="PKS"):
            dpg.add_menu_item(label="Package Manager")
            dpg.add_menu_item(label="Asset Browser")

        with dpg.menu(label="Help"):
            dpg.add_menu_item(label="Documentation")
            dpg.add_menu_item(label="About")
