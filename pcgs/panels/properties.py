import dearpygui.dearpygui as dpg


def build_properties(parent=None):
    with dpg.child_window(
        label="Properties",
        tag="__properties__",
        border=True,
    ):
        dpg.add_text("Properties", color=(252, 227, 0))
        dpg.add_separator()

        with dpg.collapsing_header(label="Transform", default_open=True):
            dpg.add_input_floatx(label="Position", default_value=[0.0, 0.0, 0.0], size=3)
            dpg.add_input_floatx(label="Rotation", default_value=[0.0, 0.0, 0.0], size=3)
            dpg.add_input_floatx(label="Scale", default_value=[1.0, 1.0, 1.0], size=3)

        with dpg.collapsing_header(label="Mesh", default_open=True):
            dpg.add_text("No mesh selected", color=(113, 113, 122))

        with dpg.collapsing_header(label="Material"):
            dpg.add_color_picker(label="Color", default_value=[252, 227, 0, 255])
            dpg.add_slider_float(label="Metallic", default_value=0.0)
            dpg.add_slider_float(label="Roughness", default_value=0.5)

        with dpg.collapsing_header(label="Physics"):
            dpg.add_checkbox(label="Rigid Body")
            dpg.add_combo(["Static", "Dynamic", "Kinematic"], label="Type", default_value="Static")
