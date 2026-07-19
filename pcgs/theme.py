import dearpygui.dearpygui as dpg


def apply_moo_dark_theme():
    dpg.create_theme()

    # ── Global ──────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_WindowBg, "#121212", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Border, "#3F3F46", category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowBorderSize, 1, category=dpg.mvThemeCat_Core)

    # ── Text ────────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_Text, "#FAFAFA", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TextDisabled, "#71717A", category=dpg.mvThemeCat_Core)

    # ── Accent ──────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_Button, "#FCE300", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonActive, "#E6CF00", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ButtonHovered, "#FFE94A", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_Text, "#0A0A0A", category=dpg.mvThemeCat_Core)

    # ── Inputs / Sliders ────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_FrameBg, "#1C1C1F", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBgHovered, "#27272A", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_FrameBgActive, "#3F3F46", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_SliderGrab, "#FCE300", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_SliderGrabActive, "#E6CF00", category=dpg.mvThemeCat_Core)

    # ── Tabs ────────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_Tab, "#1C1C1F", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabHovered, "#27272A", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabActive, "#FCE300", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabUnfocused, "#1C1C1F", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_TabUnfocusedActive, "#27272A", category=dpg.mvThemeCat_Core)

    # ── Headers / Titles ────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_Header, "#1C1C1F", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_HeaderHovered, "#27272A", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_HeaderActive, "#3F3F46", category=dpg.mvThemeCat_Core)

    # ── Separators ──────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_Separator, "#3F3F46", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_SeparatorHovered, "#FCE300", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_SeparatorActive, "#E6CF00", category=dpg.mvThemeCat_Core)

    # ── Scrollbar ───────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_ScrollbarBg, "#121212", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrab, "#3F3F46", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabHovered, "#52525B", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ScrollbarGrabActive, "#71717A", category=dpg.mvThemeCat_Core)

    # ── Check / Radio ───────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_CheckMark, "#FCE300", category=dpg.mvThemeCat_Core)

    # ── Popup ───────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_PopupBg, "#1A1A1A", category=dpg.mvThemeCat_Core)

    # ── Resize Grip ─────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_ResizeGrip, "#3F3F46", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ResizeGripHovered, "#FCE300", category=dpg.mvThemeCat_Core)
    dpg.add_theme_color(dpg.mvThemeCol_ResizeGripActive, "#E6CF00", category=dpg.mvThemeCat_Core)

    # ── Tooltip ─────────────────────────────────────────────────────────
    dpg.add_theme_color(dpg.mvThemeCol_TooltipBg, "#1A1A1A", category=dpg.mvThemeCat_Core)

    # ── Styles ──────────────────────────────────────────────────────────
    dpg.add_theme_style(dpg.mvStyleVar_WindowRounding, 6, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FrameRounding, 6, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_PopupRounding, 6, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ScrollbarRounding, 6, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_GrabRounding, 6, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_FramePadding, 8, 4, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_WindowPadding, 8, 8, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemSpacing, 8, 4, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ItemInnerSpacing, 4, 4, category=dpg.mvThemeCat_Core)
    dpg.add_theme_style(dpg.mvStyleVar_ScrollbarSize, 12, category=dpg.mvThemeCat_Core)

    # ── Fonts ───────────────────────────────────────────────────────────
    dpg.add_theme_font(dpg.mvFontDefault, category=dpg.mvThemeCat_Core)

    dpg.bind_theme()
