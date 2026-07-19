import dearpygui.dearpygui as dpg


def build_viewport(parent=None):
    with dpg.child_window(
        label="Viewport",
        tag="__viewport__",
        border=True,
    ):
        with dpg.tab_bar():
            with dpg.tab(label="3D Viewport"):
                dpg.add_text("Viewport placeholder", color=(113, 113, 122))
                dpg.add_text("OpenGL rendering will go here")
            with dpg.tab(label="Script Editor"):
                dpg.add_text("Script editor placeholder")
            with dpg.tab(label="Asset Preview"):
                dpg.add_text("Asset preview placeholder")
