import dearpygui.dearpygui as dpg


def _on_command(sender, app_data, user_data):
    output = user_data
    cmd = dpg.get_value(sender)
    if cmd.strip():
        dpg.set_value(output, dpg.get_value(output) + f"\n> {cmd}")
        dpg.set_value(sender, "")


def build_terminal(parent=None):
    with dpg.child_window(
        label="Terminal",
        height=150,
        tag="__terminal__",
        border=True,
    ):
        dpg.add_text("Output", color=(252, 227, 0))
        dpg.add_separator()
        dpg.add_input_text(
            multiline=True,
            readonly=True,
            default_value="Pythkernel Engine v0.0.3\nReady.",
            height=80,
            tag="__terminal_output__",
        )
        dpg.add_input_text(
            hint="Type command...",
            on_enter=True,
            callback=_on_command,
            user_data="__terminal_output__",
            tag="__terminal_input__",
        )
