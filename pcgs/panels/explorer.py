import dearpygui.dearpygui as dpg


def build_explorer(parent=None):
    with dpg.child_window(
        label="Explorer",
        tag="__explorer__",
        border=True,
    ):
        dpg.add_text("Project Files", color=(252, 227, 0))
        dpg.add_separator()
        with dpg.tree_node(label="My Game", default_open=True):
            dpg.add_tree_node(label="Assets")
            dpg.add_tree_node(label="Scenes")
            dpg.add_tree_node(label="Scripts")
            dpg.add_tree_node(label="Materials")
        dpg.add_separator()
        dpg.add_text("No project loaded", color=(113, 113, 122))
