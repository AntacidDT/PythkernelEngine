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
        large_icon="",
    )

    # ── Main Window ─────────────────────────────────────────────────────
    with dpg.window(tag="__main_window__"):
        dpg.add_text("Pythkernel Engine v0.1.0")
        dpg.add_text("Phase 1: Moo UI Shell")
        dpg.add_separator()
        dpg.add_text("Theme applied successfully.")

    dpg.set_primary_window("__main_window__", True)
    dpg.setup_dearpygui()
    dpg.show_viewport()
    dpg.start_dearpygui()
    dpg.destroy_context()
