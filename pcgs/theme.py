import dearpygui.dearpygui as dpg


def _rgb(hex_str):
    h = hex_str.lstrip("#")
    return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))


def apply_moo_dark_theme():
    with dpg.theme() as theme:
        with dpg.theme_component(dpg.mvAll):
            dpg.add_theme_color(dpg.mvThemeCol_WindowBg, _rgb("#121212"))
            dpg.add_theme_color(dpg.mvThemeCol_Border, _rgb("#3F3F46"))
            dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1)

            dpg.add_theme_color(dpg.mvThemeCol_Text, _rgb("#FAFAFA"))
            dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, _rgb("#71717A"))

            dpg.add_theme_color(dpg.mvThemeCol_Button, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, _rgb("#E6CF00"))
            dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, _rgb("#FFE94A"))

            dpg.add_theme_color(dpg.mvThemeCol_FrameBg, _rgb("#1C1C1F"))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, _rgb("#27272A"))
            dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, _rgb("#3F3F46"))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, _rgb("#E6CF00"))

            dpg.add_theme_color(dpg.mvThemeCol_Tab, _rgb("#1C1C1F"))
            dpg.add_theme_color(dpg.mvThemeCol_TabHovered, _rgb("#27272A"))
            dpg.add_theme_color(dpg.mvThemeCol_TabActive, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, _rgb("#1C1C1F"))
            dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, _rgb("#27272A"))

            dpg.add_theme_color(dpg.mvThemeCol_Header, _rgb("#1C1C1F"))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, _rgb("#27272A"))
            dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, _rgb("#3F3F46"))

            dpg.add_theme_color(dpg.mvThemeCol_Separator, _rgb("#3F3F46"))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, _rgb("#E6CF00"))

            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, _rgb("#121212"))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, _rgb("#3F3F46"))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, _rgb("#52525B"))
            dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, _rgb("#71717A"))

            dpg.add_theme_color(dpg.mvThemeCol_CheckMark, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_PopupBg, _rgb("#1A1A1A"))

            dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, _rgb("#3F3F46"))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, _rgb("#FCE300"))
            dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, _rgb("#E6CF00"))

            dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 6)
            dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6)
            dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 6)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 6)
            dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 6)
            dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4)
            dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 8, 8)
            dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 4, 4)
            dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 12)

    dpg.bind_theme(theme)
