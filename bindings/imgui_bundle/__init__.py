# Part of ImGui Bundle - MIT License - Copyright (c) 2022-2023 Pascal Thomet - https://github.com/pthom/imgui_bundle
#from imgui_bundle._imgui_bundle import hhh as hhh  # type: ignore
import os
from imgui_bundle._imgui_bundle import __bundle_submodules__ # type: ignore
from imgui_bundle._imgui_bundle import __version__, compilation_time


def has_submodule(submodule_name):
    return submodule_name in __bundle_submodules__


__all__ = ["__version__", "compilation_time"]


#
# Import native submodules
#
if has_submodule("imgui"):
    from imgui_bundle._imgui_bundle import imgui as imgui
    from imgui_bundle._imgui_bundle.imgui import ImVec2, ImVec4, ImColor, FLT_MIN, FLT_MAX  # type: ignore # noqa: F401
    from imgui_bundle import imgui_pydantic as imgui_pydantic
    from imgui_bundle.imgui_pydantic import (
        ImVec4_Pydantic as ImVec4_Pydantic,
        ImVec2_Pydantic as ImVec2_Pydantic,
        ImColor_Pydantic as ImColor_Pydantic,
    )
    from imgui_bundle.im_col32 import IM_COL32  # noqa: F401, E402
    from imgui_bundle import imgui_ctx as imgui_ctx  # noqa: E402

    __all__.extend([
        "imgui",
        "ImVec2",
        "ImVec4",
        "ImColor",
        "FLT_MIN",
        "FLT_MAX",
        "IM_COL32",
        "imgui_ctx",
        # Pydantic types
        "imgui_pydantic",
        "ImVec4_Pydantic",
        "ImVec2_Pydantic",
        "ImColor_Pydantic",
    ])


    # Patch after imgui v1.90.9, where
    # the enum ImGuiDir_ was renamed to ImGuiDir and ImGuiSortDirection_ was renamed to ImGuiSortDirection
    # this enables old python to continue to work
    imgui.Dir_ = imgui.Dir
    imgui.SortDirection_ = imgui.SortDirection


if has_submodule("hello_imgui"):
    from imgui_bundle._imgui_bundle import hello_imgui as hello_imgui
    __all__.extend(["hello_imgui"])
if has_submodule("implot"):
    from imgui_bundle._imgui_bundle import implot as implot
    __all__.extend(["implot"])
    # Flag types for ImPlot
    implot.LineFlags = int  # see implot.LineFlags_
    implot.ScatterFlags = int  # see implot.ScatterFlags_
    implot.StairsFlags = int  # see implot.StairsFlags_
    implot.ShadedFlags = int  # see implot.ShadedFlags_
    implot.BarsFlags = int  # see implot.BarsFlags_
    implot.PieChartFlags = int  # see implot.PieChartFlags_
    implot.HistogramFlags = int  # see implot.HistogramFlags_
if has_submodule("imgui_color_text_edit"):
    from imgui_bundle._imgui_bundle import imgui_color_text_edit as imgui_color_text_edit
    __all__.extend(["imgui_color_text_edit"])
if has_submodule("imgui_node_editor"):
    from imgui_bundle._imgui_bundle import imgui_node_editor as imgui_node_editor
    from imgui_bundle import imgui_node_editor_ctx as imgui_node_editor_ctx  # noqa: E402
    __all__.extend(["imgui_node_editor", "imgui_node_editor_ctx"])
if has_submodule("imgui_knobs"):
    from imgui_bundle._imgui_bundle import imgui_knobs as imgui_knobs
    __all__.extend(["imgui_knobs"])
if has_submodule("im_file_dialog"):
    from imgui_bundle._imgui_bundle import im_file_dialog as im_file_dialog
    __all__.extend(["im_file_dialog"])
if has_submodule("imspinner"):
    from imgui_bundle._imgui_bundle import imspinner as imspinner
    __all__.extend(["imspinner"])
if has_submodule("imgui_md"):
    from imgui_bundle._imgui_bundle import imgui_md as imgui_md
    __all__.extend(["imgui_md"])
if has_submodule("immvision"):
    from imgui_bundle._imgui_bundle import immvision as immvision
    __all__.extend(["immvision"])
if has_submodule("imguizmo"):
    from imgui_bundle._imgui_bundle import imguizmo as imguizmo
    __all__.extend(["imguizmo"])
if has_submodule("imgui_tex_inspect"):
    from imgui_bundle._imgui_bundle import imgui_tex_inspect as imgui_tex_inspect
    __all__.extend(["imgui_tex_inspect"])
if has_submodule("imgui_toggle"):
    from imgui_bundle._imgui_bundle import imgui_toggle as imgui_toggle
    __all__.extend(["imgui_toggle"])
if has_submodule("portable_file_dialogs"):
    from imgui_bundle._imgui_bundle import portable_file_dialogs as portable_file_dialogs
    __all__.extend(["portable_file_dialogs"])
if has_submodule("imgui_command_palette"):
    from imgui_bundle._imgui_bundle import imgui_command_palette as imgui_command_palette
    __all__.extend(["imgui_command_palette"])
if has_submodule("imcoolbar"):
    from imgui_bundle._imgui_bundle import im_cool_bar as im_cool_bar
    __all__.extend(["im_cool_bar"])
if has_submodule("nanovg"):
    from imgui_bundle._imgui_bundle import nanovg as nanovg
    __all__.extend(["nanovg"])

if has_submodule("immapp_cpp"):  # immapp is a Python wrapper around immapp_cpp
    from imgui_bundle import immapp as immapp
    # Note: to enable font awesome 6:
    #     runner_params.callbacks.default_icon_font = hello_imgui.DefaultIconFont.font_awesome6
    from imgui_bundle.immapp import icons_fontawesome_4 as icons_fontawesome_4
    from imgui_bundle.immapp import icons_fontawesome_4 as icons_fontawesome  # v4  # noqa: F401
    from imgui_bundle.immapp import icons_fontawesome_6 as icons_fontawesome_6
    __all__.extend(["immapp", "icons_fontawesome_4", "icons_fontawesome", "icons_fontawesome_6"])


#
# Import Python submodules
#

try:
    # if matplotlib is not installed, we can't import imgui_fig
    from imgui_bundle import imgui_fig as imgui_fig
    __all__.extend(["imgui_fig"])
except ImportError:
    pass




# Glfw setup:
# By importing imgui_bundle.glfw_utils, we make sure that glfw provided by pip will use our glfw dynamic library.
# (imgui_bundle.glfw_utils will call _set_glfw_pip_search_path automatically)
if has_submodule("with_glfw"):
    from imgui_bundle._glfw_set_search_path import _glfw_set_search_path

    _glfw_set_search_path()
    from imgui_bundle import glfw_utils as glfw_utils  # noqa: E402


#

# Override assets folder
#
THIS_DIR = os.path.dirname(__file__)
hello_imgui.override_assets_folder(THIS_DIR + "/assets")
