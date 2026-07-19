import dearpygui.dearpygui as dpg

from pcgs.theme import apply_moo_dark_theme


def create_app():
    dpg.create_context()
    apply_moo_dark_theme()

    dpg.create_viewport(
        title="Pythkernel Engine",
        width=1280,
        height=720,
        min_width=800,
        min_height=600,
    )

    with dpg.window(tag="__main_window__"):
        dpg.add_text("Pythkernel Engine v0.1.0")
        dpg.add_text("Moo UI Theme Test")
        dpg.add_separator()

        dpg.add_text("Buttons")
        with dpg.group(horizontal=True):
            dpg.add_button(label="Primary")
            dpg.add_button(label="Secondary")
            dpg.add_button(label="Small", width=60)

        dpg.add_separator()
        dpg.add_text("Inputs")
        dpg.add_input_text(label="Text Input", default_value="Hello Moo UI")
        dpg.add_input_int(label="Integer", default_value=42)
        dpg.add_input_float(label="Float", default_value=3.14)

        dpg.add_separator()
        dpg.add_text("Sliders")
        dpg.add_slider_float(label="Float Slider", default_value=0.5, min_value=0.0, max_value=1.0)
        dpg.add_slider_int(label="Int Slider", default_value=50, min_value=0, max_value=100)
        dpg.add_slider_float(label="Rotation X", default_value=0.0, min_value=-180.0, max_value=180.0)

        dpg.add_separator()
        dpg.add_text("Checkboxes & Radio")
        with dpg.group(horizontal=True):
            dpg.add_checkbox(label="Enable VSync")
            dpg.add_checkbox(label="Wireframe")
            dpg.add_checkbox(label="Debug")

        dpg.add_separator()
        dpg.add_text("Combo Box")
        dpg.add_combo(["Option 1", "Option 2", "Option 3"], label="Select", default_value="Option 1")

        dpg.add_separator()
        dpg.add_text("Color Picker")
        dpg.add_color_picker(default_value=[252, 227, 0, 255], label="Accent Color")

    dpg.set_primary_window("__main_window__", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
