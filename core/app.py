import os
import dearpygui.dearpygui as dpg

from pcgs.theme import apply_moo_dark_theme
from pcgs.layout import build_layout, _on_global_drag

FONT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "fonts")


def create_app():
    dpg.create_context()

    with dpg.font_registry():
        sans = dpg.add_font(os.path.join(FONT_DIR, "Geist.ttf"), 13)
        sans_sm = dpg.add_font(os.path.join(FONT_DIR, "Geist.ttf"), 11)
        mono = dpg.add_font(os.path.join(FONT_DIR, "GeistMono.ttf"), 13)

    dpg.bind_font(sans)

    apply_moo_dark_theme()

    dpg.create_viewport(
        title="Pythkernel Engine",
        width=1280,
        height=720,
        min_width=800,
        min_height=600,
    )

    build_layout()

    with dpg.handler_registry():
        dpg.add_mouse_drag_handler(callback=_on_global_drag, threshold=1)

    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
