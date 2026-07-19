import dearpygui.dearpygui as dpg

from pcgs.menu import build_menu_bar

EXPLORER_W = 250
PROPERTIES_W = 280
TERMINAL_H = 150
SPLITTER_W = 6


def _is_hovering(tag):
    mx, my = dpg.get_mouse_pos()
    x1, y1 = dpg.get_item_pos(tag)
    x2 = x1 + (dpg.get_item_width(tag) or SPLITTER_W)
    y2 = y1 + (dpg.get_item_height(tag) or 5000)
    return x1 <= mx <= x2 and y1 <= my <= y2


def _on_global_drag(sender, app_data):
    delta = app_data
    mx, my = dpg.get_mouse_pos()

    if _is_hovering("__splitter_explorer__"):
        current = dpg.get_item_width("__explorer_panel__")
        new_w = max(150, min(600, current + int(delta)))
        dpg.set_item_width("__explorer_panel__", new_w)

    elif _is_hovering("__splitter_properties__"):
        current = dpg.get_item_width("__properties_panel__")
        new_w = max(150, min(600, current - int(delta)))
        dpg.set_item_width("__properties_panel__", new_w)

    elif _is_hovering("__splitter_terminal__"):
        current = dpg.get_item_height("__terminal_panel__")
        new_h = max(80, min(400, current - int(delta)))
        dpg.set_item_height("__terminal_panel__", new_h)


_detached = {}


def _detach_panel(panel_tag, content_tag, title, w, h):
    if panel_tag in _detached:
        return

    dpg.hide_item(f"__{panel_tag}_panel__")
    dpg.hide_item(f"__splitter_{panel_tag}__")

    vp_tag = f"__vp_{panel_tag}__"
    dpg.create_viewport(title=title, width=w, height=h, min_width=300, min_height=200)

    win = dpg.add_window(tag=f"__detach_{panel_tag}__", no_scrollbar=True)
    dpg.set_primary_window(win, True)

    _detached[panel_tag] = {"viewport": vp_tag, "window": win}

    dpg.setup_dearpygui()
    dpg.show_viewport()

    children = dpg.get_item_children(content_tag, 1)
    if children:
        for child in list(children):
            dpg.move_item(child, parent=win)


def _on_detach_explorer():
    _detach_panel("explorer", "__explorer_content__", "Explorer", 300, 500)


def _on_detach_properties():
    _detach_panel("properties", "__properties_content__", "Properties", 320, 500)


def _on_detach_terminal():
    _detach_panel("terminal", "__terminal_content__", "Terminal", 700, 200)


def build_layout():
    with dpg.window(tag="__main_window__", pos=(0, 0), no_scrollbar=True):
        build_menu_bar()

        with dpg.group(horizontal=True, tag="__content_row__"):
            # Explorer
            with dpg.child_window(
                tag="__explorer_panel__",
                width=EXPLORER_W,
                border=True,
                menubar=True,
            ):
                with dpg.menu_bar():
                    dpg.add_menu_item(label="Explorer", enabled=False)
                    dpg.add_menu_item(label="+", callback=_on_detach_explorer)
                with dpg.group(tag="__explorer_content__"):
                    _build_explorer_content()

            # Splitter left
            with dpg.child_window(
                tag="__splitter_explorer__",
                width=SPLITTER_W,
                no_scrollbar=True,
                no_scroll_with_mouse=True,
                border=True,
            ):
                pass

            # Viewport center
            with dpg.child_window(
                tag="__viewport_panel__",
                border=True,
                menubar=True,
            ):
                with dpg.menu_bar():
                    dpg.add_menu_item(label="3D Viewport", enabled=False)
                with dpg.group(tag="__viewport_content__"):
                    dpg.add_text("Viewport placeholder", color=(113, 113, 122))
                    dpg.add_text("OpenGL rendering will go here")

            # Splitter right
            with dpg.child_window(
                tag="__splitter_properties__",
                width=SPLITTER_W,
                no_scrollbar=True,
                no_scroll_with_mouse=True,
                border=True,
            ):
                pass

            # Properties
            with dpg.child_window(
                tag="__properties_panel__",
                width=PROPERTIES_W,
                border=True,
                menubar=True,
            ):
                with dpg.menu_bar():
                    dpg.add_menu_item(label="Properties", enabled=False)
                    dpg.add_menu_item(label="+", callback=_on_detach_properties)
                with dpg.group(tag="__properties_content__"):
                    _build_properties_content()

        # Terminal splitter
        with dpg.child_window(
            tag="__splitter_terminal__",
            height=SPLITTER_W,
            no_scrollbar=True,
            no_scroll_with_mouse=True,
            border=True,
        ):
            pass

        # Terminal
        with dpg.child_window(
            tag="__terminal_panel__",
            height=TERMINAL_H,
            border=True,
            menubar=True,
        ):
            with dpg.menu_bar():
                dpg.add_menu_item(label="Output", enabled=False)
                dpg.add_menu_item(label="+", callback=_on_detach_terminal)
            with dpg.group(tag="__terminal_content__"):
                _build_terminal_content()

    dpg.set_primary_window("__main_window__", True)


def _build_explorer_content():
    dpg.add_text("Project Files", color=(252, 227, 0))
    dpg.add_separator()
    with dpg.tree_node(label="My Game", default_open=True):
        dpg.add_tree_node(label="Assets")
        dpg.add_tree_node(label="Scenes")
        dpg.add_tree_node(label="Scripts")
        dpg.add_tree_node(label="Materials")
    dpg.add_separator()
    dpg.add_text("No project loaded", color=(113, 113, 122))


def _build_properties_content():
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


def _build_terminal_content():
    dpg.add_text("Output", color=(252, 227, 0))
    dpg.add_separator()
    dpg.add_input_text(
        multiline=True,
        readonly=True,
        default_value="Pythkernel Engine v0.0.4\nReady.",
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


def _on_command(sender, app_data, user_data):
    output = user_data
    cmd = dpg.get_value(sender)
    if cmd.strip():
        dpg.set_value(output, dpg.get_value(output) + f"\n> {cmd}")
        dpg.set_value(sender, "")
