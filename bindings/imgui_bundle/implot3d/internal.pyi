"""ImPlot: Immediate Mode 3D Plotting for ImGui
Python bindings for https://github.com/brenocq/implot3d
"""
# ruff: noqa: E741, B008
from typing import Any, Optional, Tuple, overload

from imgui_bundle.imgui import ImVec2, ImVec4, ImU32, ID, ImVec2Like, ImVec4Like, ImDrawList
from imgui_bundle.imgui.internal import ImRect
from imgui_bundle.implot3d import (
    Colormap, Marker, Flags, Col, Point, LegendFlags, AxisFlags, Location,
    Quat, Ray, Range, Cond, Style, ItemFlags
    )


# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# <litgen_stub> // Autogenerated code below! Do not edit!
####################    <generated_from:implot3d_internal.h>    ####################
#--------------------------------------------------
# ImPlot3D v0.1
# implot3_internal.h
# Date: 2024-11-17
# Author: Breno Cunha Queiroz (brenocq.com)
#
# Acknowledgments:
#  ImPlot3D is heavily inspired by ImPlot
#  (https://github.com/epezent/implot) by Evan Pezent,
#  and follows a similar code style and structure to
#  maintain consistency with ImPlot's API.
#--------------------------------------------------

# Table of Contents:
# [SECTION] Constants
# [SECTION] Generic Helpers
# [SECTION] Forward Declarations
# [SECTION] Callbacks
# [SECTION] Structs
# [SECTION] Context Pointer
# [SECTION] Context Utils
# [SECTION] Style Utils
# [SECTION] Item Utils
# [SECTION] Plot Utils
# [SECTION] Setup Utils
# [SECTION] Formatter
# [SECTION] Locator



# #ifndef IMGUI_DISABLE
#

#-----------------------------------------------------------------------------
# [SECTION] Constants
#-----------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# [SECTION] Generic Helpers
#-----------------------------------------------------------------------------


# static inline float ImLog10(float x) { return log10f(x); }    /* original C++ signature */
def im_log10(x: float) -> float:
    """ Computes the common (base-10) logarithm
    (private API)
    """
    pass
# Flips a flag in a flagset
# static inline bool ImNan(float val) { return isnan(val); }    /* original C++ signature */
def im_nan(val: float) -> bool:
    """ Returns True if val is NAN
    (private API)
    """
    pass
# static inline bool ImNanOrInf(float val) { return !(val >= -FLT_MAX && val <= FLT_MAX) || ImNan(val); }    /* original C++ signature */
def im_nan_or_inf(val: float) -> bool:
    """ Returns True if val is NAN or INFINITY
    (private API)
    """
    pass
# static inline double ImConstrainNan(float val) { return ImNan(val) ? 0 : val; }    /* original C++ signature */
def im_constrain_nan(val: float) -> float:
    """ Turns NANs to 0s
    (private API)
    """
    pass
# static inline double ImConstrainInf(double val) { return val >= FLT_MAX ? FLT_MAX : val <= -FLT_MAX ? -FLT_MAX    /* original C++ signature */
#                                                                                                     : val; }
def im_constrain_inf(val: float) -> float:
    """ Turns infinity to floating point maximums
    (private API)
    """
    pass
# static inline bool ImAlmostEqual(double v1, double v2, int ulp = 2) { return ImAbs(v1 - v2) < FLT_EPSILON * ImAbs(v1 + v2) * ulp || ImAbs(v1 - v2) < FLT_MIN; }    /* original C++ signature */
def im_almost_equal(v1: float, v2: float, ulp: int = 2) -> bool:
    """ True if two numbers are approximately equal using units in the last place.
    (private API)
    """
    pass
# static inline ImU32 ImAlphaU32(ImU32 col, float alpha) {    /* original C++ signature */
#     return col & ~((ImU32)((1.0f - alpha) * 255) << IM_COL32_A_SHIFT);
# }
def im_alpha_u32(col: ImU32, alpha: float) -> ImU32:
    """ Set alpha channel of 32-bit color from float in range [0.0 1.0]
    (private API)
    """
    pass
# static inline ImU32 ImMixU32(ImU32 a, ImU32 b, ImU32 s) {    /* original C++ signature */
# #ifdef IMPLOT3D_MIX64
#     const ImU32 af = 256 - s;
#     const ImU32 bf = s;
#     const ImU64 al = (a & 0x00ff00ff) | (((ImU64)(a & 0xff00ff00)) << 24);
#     const ImU64 bl = (b & 0x00ff00ff) | (((ImU64)(b & 0xff00ff00)) << 24);
#     const ImU64 mix = (al * af + bl * bf);
#     return ((mix >> 32) & 0xff00ff00) | ((mix & 0xff00ff00) >> 8);
# #else
#     const ImU32 af = 256 - s;
#     const ImU32 bf = s;
#     const ImU32 al = (a & 0x00ff00ff);
#     const ImU32 ah = (a & 0xff00ff00) >> 8;
#     const ImU32 bl = (b & 0x00ff00ff);
#     const ImU32 bh = (b & 0xff00ff00) >> 8;
#     const ImU32 ml = (al * af + bl * bf);
#     const ImU32 mh = (ah * af + bh * bf);
#     return (mh & 0xff00ff00) | ((ml & 0xff00ff00) >> 8);
# #endif
# }
def im_mix_u32(a: ImU32, b: ImU32, s: ImU32) -> ImU32:
    """ Mix color a and b by factor s in [0 256]
    (private API)
    """
    pass



#-----------------------------------------------------------------------------
# [SECTION] Forward Declarations
#-----------------------------------------------------------------------------


#------------------------------------------------------------------------------
# [SECTION] Callbacks
#------------------------------------------------------------------------------


#-----------------------------------------------------------------------------
# [SECTION] Structs
#-----------------------------------------------------------------------------


class NextItemData:
    # float LineWeight;    /* original C++ signature */
    line_weight: float
    # ImPlot3DMarker Marker;    /* original C++ signature */
    marker: Marker
    # float MarkerSize;    /* original C++ signature */
    marker_size: float
    # float MarkerWeight;    /* original C++ signature */
    marker_weight: float
    # float FillAlpha;    /* original C++ signature */
    fill_alpha: float
    # bool RenderLine;    /* original C++ signature */
    render_line: bool
    # bool RenderFill;    /* original C++ signature */
    render_fill: bool
    # bool RenderMarkerLine;    /* original C++ signature */
    render_marker_line: bool
    # bool RenderMarkerFill;    /* original C++ signature */
    render_marker_fill: bool
    # bool IsAutoFill;    /* original C++ signature */
    is_auto_fill: bool
    # bool IsAutoLine;    /* original C++ signature */
    is_auto_line: bool
    # bool Hidden;    /* original C++ signature */
    hidden: bool

    # ImPlot3DNextItemData() { Reset(); }    /* original C++ signature */
    def __init__(self) -> None:
        pass

    # void Reset() {    /* original C++ signature */
    #         for (int i = 0; i < 4; i++)
    #             Colors[i] = IMPLOT3D_AUTO_COL;
    #         LineWeight = IMPLOT3D_AUTO;
    #         Marker = IMPLOT3D_AUTO;
    #         MarkerSize = IMPLOT3D_AUTO;
    #         MarkerWeight = IMPLOT3D_AUTO;
    #         FillAlpha = IMPLOT3D_AUTO;
    #         RenderLine = false;
    #         RenderFill = false;
    #         RenderMarkerLine = true;
    #         RenderMarkerFill = true;
    #         IsAutoFill = true;
    #         IsAutoLine = true;
    #         Hidden = false;
    #     }
    def reset(self) -> None:
        """(private API)"""
        pass

class ColormapData:
    """ Colormap data storage"""
    # int Count;    /* original C++ signature */
    count: int

    # ImPlot3DColormapData() { Count = 0; }    /* original C++ signature */
    def __init__(self) -> None:
        pass

    # int Append(const char* name, const ImU32* keys, int count, bool qual) {    /* original C++ signature */
    #         if (GetIndex(name) != -1)
    #             return -1;
    #         KeyOffsets.push_back(Keys.size());
    #         KeyCounts.push_back(count);
    #         Keys.reserve(Keys.size() + count);
    #         for (int i = 0; i < count; ++i)
    #             Keys.push_back(keys[i]);
    #         TextOffsets.push_back(Text.size());
    #         Text.append(name, name + strlen(name) + 1);
    #         Quals.push_back(qual);
    #         ImGuiID id = ImHashStr(name);
    #         int idx = Count++;
    #         Map.SetInt(id, idx);
    #         _AppendTable(idx);
    #         return idx;
    #     }
    def append(self, name: str, keys: ImU32, count: int, qual: bool) -> int:
        """(private API)"""
        pass

    # void _AppendTable(ImPlot3DColormap cmap) {    /* original C++ signature */
    #         int key_count = GetKeyCount(cmap);
    #         const ImU32* keys = GetKeys(cmap);
    #         int off = Tables.size();
    #         TableOffsets.push_back(off);
    #         if (IsQual(cmap)) {
    #             Tables.reserve(key_count);
    #             for (int i = 0; i < key_count; ++i)
    #                 Tables.push_back(keys[i]);
    #             TableSizes.push_back(key_count);
    #         } else {
    #             int max_size = 255 * (key_count - 1) + 1;
    #             Tables.reserve(off + max_size);
    #             // ImU32 last = keys[0];
    #             // Tables.push_back(last);
    #             // int n = 1;
    #             for (int i = 0; i < key_count - 1; ++i) {
    #                 for (int s = 0; s < 255; ++s) {
    #                     ImU32 a = keys[i];
    #                     ImU32 b = keys[i + 1];
    #                     ImU32 c = ImPlot3D::ImMixU32(a, b, s);
    #                     // if (c != last) {
    #                     Tables.push_back(c);
    #                     // last = c;
    #                     // n++;
    #                     // }
    #                 }
    #             }
    #             ImU32 c = keys[key_count - 1];
    #             // if (c != last) {
    #             Tables.push_back(c);
    #             // n++;
    #             // }
    #             // TableSizes.push_back(n);
    #             TableSizes.push_back(max_size);
    #         }
    #     }
    def _append_table(self, cmap: Colormap) -> None:
        """(private API)"""
        pass

    # void RebuildTables() {    /* original C++ signature */
    #         Tables.resize(0);
    #         TableSizes.resize(0);
    #         TableOffsets.resize(0);
    #         for (int i = 0; i < Count; ++i)
    #             _AppendTable(i);
    #     }
    def rebuild_tables(self) -> None:
        """(private API)"""
        pass

    # inline bool IsQual(ImPlot3DColormap cmap) const { return Quals[cmap]; }    /* original C++ signature */
    def is_qual(self, cmap: Colormap) -> bool:
        """(private API)"""
        pass
    # inline const char* GetName(ImPlot3DColormap cmap) const { return cmap < Count ? Text.Buf.Data + TextOffsets[cmap] : nullptr; }    /* original C++ signature */
    def get_name(self, cmap: Colormap) -> str:
        """(private API)"""
        pass
    # inline ImPlot3DColormap GetIndex(const char* name) const {    /* original C++ signature */
    #         ImGuiID key = ImHashStr(name);
    #         return Map.GetInt(key, -1);
    #     }
    def get_index(self, name: str) -> Colormap:
        """(private API)"""
        pass

    # inline const ImU32* GetKeys(ImPlot3DColormap cmap) const { return &Keys[KeyOffsets[cmap]]; }    /* original C++ signature */
    def get_keys(self, cmap: Colormap) -> ImU32:
        """(private API)"""
        pass
    # inline int GetKeyCount(ImPlot3DColormap cmap) const { return KeyCounts[cmap]; }    /* original C++ signature */
    def get_key_count(self, cmap: Colormap) -> int:
        """(private API)"""
        pass
    # inline ImU32 GetKeyColor(ImPlot3DColormap cmap, int idx) const { return Keys[KeyOffsets[cmap] + idx]; }    /* original C++ signature */
    def get_key_color(self, cmap: Colormap, idx: int) -> ImU32:
        """(private API)"""
        pass
    # inline void SetKeyColor(ImPlot3DColormap cmap, int idx, ImU32 value) {    /* original C++ signature */
    #         Keys[KeyOffsets[cmap] + idx] = value;
    #         RebuildTables();
    #     }
    def set_key_color(self, cmap: Colormap, idx: int, value: ImU32) -> None:
        """(private API)"""
        pass

    # inline const ImU32* GetTable(ImPlot3DColormap cmap) const { return &Tables[TableOffsets[cmap]]; }    /* original C++ signature */
    def get_table(self, cmap: Colormap) -> ImU32:
        """(private API)"""
        pass
    # inline int GetTableSize(ImPlot3DColormap cmap) const { return TableSizes[cmap]; }    /* original C++ signature */
    def get_table_size(self, cmap: Colormap) -> int:
        """(private API)"""
        pass
    # inline ImU32 GetTableColor(ImPlot3DColormap cmap, int idx) const { return Tables[TableOffsets[cmap] + idx]; }    /* original C++ signature */
    def get_table_color(self, cmap: Colormap, idx: int) -> ImU32:
        """(private API)"""
        pass

    # inline ImU32 LerpTable(ImPlot3DColormap cmap, float t) const {    /* original C++ signature */
    #         int off = TableOffsets[cmap];
    #         int siz = TableSizes[cmap];
    #         int idx = Quals[cmap] ? ImClamp((int)(siz * t), 0, siz - 1) : (int)((siz - 1) * t + 0.5f);
    #         return Tables[off + idx];
    #     }
    def lerp_table(self, cmap: Colormap, t: float) -> ImU32:
        """(private API)"""
        pass

class Item:
    """ State information for plot items"""
    # ImGuiID ID;    /* original C++ signature */
    id_: ID
    # ImU32 Color;    /* original C++ signature */
    color: ImU32
    # int NameOffset;    /* original C++ signature */
    name_offset: int
    # bool Show;    /* original C++ signature */
    show: bool
    # bool LegendHovered;    /* original C++ signature */
    legend_hovered: bool
    # bool SeenThisFrame;    /* original C++ signature */
    seen_this_frame: bool

    # ImPlot3DItem() {    /* original C++ signature */
    #         ID = 0;
    #         Color = IM_COL32_WHITE;
    #         NameOffset = -1;
    #         Show = true;
    #         LegendHovered = false;
    #         SeenThisFrame = false;
    #     }
    def __init__(self) -> None:
        pass

class Legend:
    """ Holds legend state"""
    # ImPlot3DLegendFlags Flags;    /* original C++ signature */
    flags: LegendFlags
    # ImPlot3DLegendFlags PreviousFlags;    /* original C++ signature */
    previous_flags: LegendFlags
    # ImPlot3DLocation Location;    /* original C++ signature */
    location: Location
    # ImPlot3DLocation PreviousLocation;    /* original C++ signature */
    previous_location: Location
    # ImRect Rect;    /* original C++ signature */
    rect: ImRect
    # bool Hovered;    /* original C++ signature */
    hovered: bool
    # bool Held;    /* original C++ signature */
    held: bool

    # ImPlot3DLegend() {    /* original C++ signature */
    #         PreviousFlags = Flags = ImPlot3DLegendFlags_None;
    #         Hovered = Held = false;
    #         PreviousLocation = Location = ImPlot3DLocation_NorthWest;
    #     }
    def __init__(self) -> None:
        pass

    # void Reset() {    /* original C++ signature */
    #         Indices.shrink(0);
    #         Labels.Buf.shrink(0);
    #     }
    def reset(self) -> None:
        """(private API)"""
        pass

class ItemGroup:
    """ Holds items"""
    # ImPlot3DLegend Legend;    /* original C++ signature */
    legend: Legend
    # int ColormapIdx;    /* original C++ signature */
    colormap_idx: int

    # ImPlot3DItemGroup() {    /* original C++ signature */
    #         ColormapIdx = 0;
    #     }
    def __init__(self) -> None:
        pass

    # int GetItemCount() const { return ItemPool.GetBufSize(); }    /* original C++ signature */
    def get_item_count(self) -> int:
        """(private API)"""
        pass
    # ImGuiID GetItemID(const char* label_id) { return ImGui::GetID(label_id); }    /* original C++ signature */
    def get_item_id(self, label_id: str) -> ID:
        """(private API)"""
        pass
    # ImPlot3DItem* GetItem(ImGuiID id) { return ItemPool.GetByKey(id); }    /* original C++ signature */
    @overload
    def get_item(self, id_: ID) -> Item:
        """(private API)"""
        pass
    # ImPlot3DItem* GetItem(const char* label_id) { return GetItem(GetItemID(label_id)); }    /* original C++ signature */
    @overload
    def get_item(self, label_id: str) -> Item:
        """(private API)"""
        pass
    # ImPlot3DItem* GetOrAddItem(ImGuiID id) { return ItemPool.GetOrAddByKey(id); }    /* original C++ signature */
    def get_or_add_item(self, id_: ID) -> Item:
        """(private API)"""
        pass
    # ImPlot3DItem* GetItemByIndex(int i) { return ItemPool.GetByIndex(i); }    /* original C++ signature */
    def get_item_by_index(self, i: int) -> Item:
        """(private API)"""
        pass
    # int GetItemIndex(ImPlot3DItem* item) { return ItemPool.GetIndex(item); }    /* original C++ signature */
    def get_item_index(self, item: Item) -> int:
        """(private API)"""
        pass
    # int GetLegendCount() const { return Legend.Indices.size(); }    /* original C++ signature */
    def get_legend_count(self) -> int:
        """(private API)"""
        pass
    # ImPlot3DItem* GetLegendItem(int i) { return ItemPool.GetByIndex(Legend.Indices[i]); }    /* original C++ signature */
    def get_legend_item(self, i: int) -> Item:
        """(private API)"""
        pass
    # const char* GetLegendLabel(int i) { return Legend.Labels.Buf.Data + GetLegendItem(i)->NameOffset; }    /* original C++ signature */
    def get_legend_label(self, i: int) -> str:
        """(private API)"""
        pass
    # void Reset() {    /* original C++ signature */
    #         ItemPool.Clear();
    #         Legend.Reset();
    #         ColormapIdx = 0;
    #     }
    def reset(self) -> None:
        """(private API)"""
        pass

class Tick:
    """ Tick mark info"""
    # float PlotPos;    /* original C++ signature */
    plot_pos: float
    # bool Major;    /* original C++ signature */
    major: bool
    # bool ShowLabel;    /* original C++ signature */
    show_label: bool
    # ImVec2 LabelSize;    /* original C++ signature */
    label_size: ImVec2
    # int TextOffset;    /* original C++ signature */
    text_offset: int
    # int Idx;    /* original C++ signature */
    idx: int

    # ImPlot3DTick(double value, bool major, bool show_label) {    /* original C++ signature */
    #         PlotPos = (float)value;
    #         Major = major;
    #         ShowLabel = show_label;
    #         TextOffset = -1;
    #     }
    def __init__(self, value: float, major: bool, show_label: bool) -> None:
        pass

class Ticker:
    """ Collection of ticks"""

    # ImPlot3DTicker() {    /* original C++ signature */
    #         Reset();
    #     }
    def __init__(self) -> None:
        pass

    # ImPlot3DTick& AddTick(double value, bool major, bool show_label, const char* label) {    /* original C++ signature */
    #         ImPlot3DTick tick(value, major, show_label);
    #         if (show_label && label != nullptr) {
    #             tick.TextOffset = TextBuffer.size();
    #             TextBuffer.append(label, label + strlen(label) + 1);
    #             tick.LabelSize = ImGui::CalcTextSize(TextBuffer.Buf.Data + tick.TextOffset);
    #         }
    #         return AddTick(tick);
    #     }
    @overload
    def add_tick(self, value: float, major: bool, show_label: bool, label: str) -> Tick:
        """(private API)"""
        pass


    # inline ImPlot3DTick& AddTick(ImPlot3DTick tick) {    /* original C++ signature */
    #         tick.Idx = Ticks.size();
    #         Ticks.push_back(tick);
    #         return Ticks.back();
    #     }
    @overload
    def add_tick(self, tick: Tick) -> Tick:
        """(private API)"""
        pass

    # const char* GetText(int idx) const {    /* original C++ signature */
    #         return TextBuffer.Buf.Data + Ticks[idx].TextOffset;
    #     }
    @overload
    def get_text(self, idx: int) -> str:
        """(private API)"""
        pass

    # const char* GetText(const ImPlot3DTick& tick) const {    /* original C++ signature */
    #         return GetText(tick.Idx);
    #     }
    @overload
    def get_text(self, tick: Tick) -> str:
        """(private API)"""
        pass

    # void Reset() {    /* original C++ signature */
    #         Ticks.shrink(0);
    #         TextBuffer.Buf.shrink(0);
    #     }
    def reset(self) -> None:
        """(private API)"""
        pass

    # int TickCount() const {    /* original C++ signature */
    #         return Ticks.Size;
    #     }
    def tick_count(self) -> int:
        """(private API)"""
        pass

class Axis:
    """ Holds axis information"""
    # ImPlot3DAxisFlags Flags;    /* original C++ signature */
    flags: AxisFlags
    # ImPlot3DAxisFlags PreviousFlags;    /* original C++ signature */
    previous_flags: AxisFlags
    # ImPlot3DRange Range;    /* original C++ signature */
    range: Range
    # ImPlot3DCond RangeCond;    /* original C++ signature */
    range_cond: Cond
    # Ticks
    # ImPlot3DTicker Ticker;    /* original C++ signature */
    ticker: Ticker
    # void* FormatterData;    /* original C++ signature */
    formatter_data: Any
    # Fit data
    # bool FitThisFrame;    /* original C++ signature */
    fit_this_frame: bool
    # ImPlot3DRange FitExtents;    /* original C++ signature */
    fit_extents: Range
    # bool Held;    /* original C++ signature */
    # User input
    held: bool

    # ImPlot3DAxis() {    /* original C++ signature */
    #         PreviousFlags = Flags = ImPlot3DAxisFlags_None;
    #         // Range
    #         Range.Min = 0.0f;
    #         Range.Max = 1.0f;
    #         RangeCond = ImPlot3DCond_None;
    #         // Ticks
    #         Formatter = nullptr;
    #         FormatterData = nullptr;
    #         Locator = nullptr;
    #         // Fit data
    #         FitThisFrame = true;
    #         FitExtents.Min = HUGE_VAL;
    #         FitExtents.Max = -HUGE_VAL;
    #         // User input
    #         Held = false;
    #     }
    def __init__(self) -> None:
        """ Constructor"""
        pass

    # inline void SetRange(double v1, double v2) {    /* original C++ signature */
    #         Range.Min = (float)ImMin(v1, v2);
    #         Range.Max = (float)ImMax(v1, v2);
    #     }
    def set_range(self, v1: float, v2: float) -> None:
        """(private API)"""
        pass

    # inline bool SetMin(double _min, bool force = false) {    /* original C++ signature */
    #         if (!force && IsLockedMin())
    #             return false;
    #         _min = ImPlot3D::ImConstrainNan((float)ImPlot3D::ImConstrainInf(_min));
    #         if (_min >= Range.Max)
    #             return false;
    #         Range.Min = (float)_min;
    #         return true;
    #     }
    def set_min(self, _min: float, force: bool = False) -> bool:
        """(private API)"""
        pass

    # inline bool SetMax(double _max, bool force = false) {    /* original C++ signature */
    #         if (!force && IsLockedMax())
    #             return false;
    #         _max = ImPlot3D::ImConstrainNan((float)ImPlot3D::ImConstrainInf(_max));
    #         if (_max <= Range.Min)
    #             return false;
    #         Range.Max = (float)_max;
    #         return true;
    #     }
    def set_max(self, _max: float, force: bool = False) -> bool:
        """(private API)"""
        pass

    # inline bool IsRangeLocked() const { return RangeCond == ImPlot3DCond_Always; }    /* original C++ signature */
    def is_range_locked(self) -> bool:
        """(private API)"""
        pass
    # inline bool IsLockedMin() const { return IsRangeLocked() || ImPlot3D::ImHasFlag(Flags, ImPlot3DAxisFlags_LockMin); }    /* original C++ signature */
    def is_locked_min(self) -> bool:
        """(private API)"""
        pass
    # inline bool IsLockedMax() const { return IsRangeLocked() || ImPlot3D::ImHasFlag(Flags, ImPlot3DAxisFlags_LockMax); }    /* original C++ signature */
    def is_locked_max(self) -> bool:
        """(private API)"""
        pass
    # inline bool IsLocked() const { return IsLockedMin() && IsLockedMax(); }    /* original C++ signature */
    def is_locked(self) -> bool:
        """(private API)"""
        pass

    # inline void SetLabel(const char* label) {    /* original C++ signature */
    #         Label.Buf.shrink(0);
    #         if (label && ImGui::FindRenderedTextEnd(label, nullptr) != label)
    #             Label.append(label, label + strlen(label) + 1);
    #     }
    def set_label(self, label: str) -> None:
        """(private API)"""
        pass

    # inline const char* GetLabel() const { return Label.Buf.Data; }    /* original C++ signature */
    def get_label(self) -> str:
        """(private API)"""
        pass

    # bool HasLabel() const;    /* original C++ signature */
    def has_label(self) -> bool:
        """(private API)"""
        pass
    # bool HasGridLines() const;    /* original C++ signature */
    def has_grid_lines(self) -> bool:
        """(private API)"""
        pass
    # bool HasTickLabels() const;    /* original C++ signature */
    def has_tick_labels(self) -> bool:
        """(private API)"""
        pass
    # bool HasTickMarks() const;    /* original C++ signature */
    def has_tick_marks(self) -> bool:
        """(private API)"""
        pass
    # bool IsAutoFitting() const;    /* original C++ signature */
    def is_auto_fitting(self) -> bool:
        """(private API)"""
        pass
    # void ExtendFit(float value);    /* original C++ signature */
    def extend_fit(self, value: float) -> None:
        """(private API)"""
        pass
    # void ApplyFit();    /* original C++ signature */
    def apply_fit(self) -> None:
        """(private API)"""
        pass

class Plot:
    """ Holds plot state information that must persist after EndPlot"""
    # ImGuiID ID;    /* original C++ signature */
    id_: ID
    # ImPlot3DFlags Flags;    /* original C++ signature */
    flags: Flags
    # ImPlot3DFlags PreviousFlags;    /* original C++ signature */
    previous_flags: Flags
    # bool JustCreated;    /* original C++ signature */
    just_created: bool
    # bool Initialized;    /* original C++ signature */
    initialized: bool
    # Bounding rectangles
    # ImRect FrameRect;    /* original C++ signature */
    frame_rect: ImRect            # Outermost bounding rectangle that encapsulates whole the plot/title/padding/etc
    # ImRect CanvasRect;    /* original C++ signature */
    canvas_rect: ImRect           # Frame rectangle reduced by padding
    # ImRect PlotRect;    /* original C++ signature */
    plot_rect: ImRect             # Bounding rectangle for the actual plot area
    # Rotation & axes & box
    # ImPlot3DQuat Rotation;    /* original C++ signature */
    rotation: Quat                # Current rotation quaternion
    # ImPlot3DPoint BoxScale;    /* original C++ signature */
    box_scale: Point              # Scale factor for plot box X, Y, Z axes
    # Animation
    # float AnimationTime;    /* original C++ signature */
    animation_time: float         # Remaining animation time
    # ImPlot3DQuat RotationAnimationEnd;    /* original C++ signature */
    rotation_animation_end: Quat  # End rotation for animation
    # User input
    # bool SetupLocked;    /* original C++ signature */
    setup_locked: bool
    # bool Hovered;    /* original C++ signature */
    hovered: bool
    # bool Held;    /* original C++ signature */
    held: bool
    # int HeldEdgeIdx;    /* original C++ signature */
    held_edge_idx: int            # Index of the edge being held
    # int HeldPlaneIdx;    /* original C++ signature */
    held_plane_idx: int           # Index of the plane being held
    # bool FitThisFrame;    /* original C++ signature */
    # Fit data
    fit_this_frame: bool
    # Items
    # ImPlot3DItemGroup Items;    /* original C++ signature */
    items: ItemGroup
    # ImPlot3DItem* CurrentItem;    /* original C++ signature */
    current_item: Item
    # Misc
    # bool ContextClick;    /* original C++ signature */
    context_click: bool           # True if context button was clicked (to distinguish from double click)
    # bool OpenContextThisFrame;    /* original C++ signature */
    open_context_this_frame: bool

    # ImPlot3DPlot() {    /* original C++ signature */
    #         PreviousFlags = Flags = ImPlot3DFlags_None;
    #         JustCreated = true;
    #         Initialized = false;
    #         Rotation = ImPlot3DQuat(0.0f, 0.0f, 0.0f, 1.0f);
    #         for (int i = 0; i < 3; i++)
    #             Axes[i] = ImPlot3DAxis();
    #         BoxScale = ImPlot3DPoint(1.0f, 1.0f, 1.0f);
    #         AnimationTime = 0.0f;
    #         RotationAnimationEnd = Rotation;
    #         SetupLocked = false;
    #         Hovered = Held = false;
    #         HeldEdgeIdx = -1;
    #         HeldPlaneIdx = -1;
    #         FitThisFrame = true;
    #         CurrentItem = nullptr;
    #         ContextClick = false;
    #         OpenContextThisFrame = false;
    #     }
    def __init__(self) -> None:
        pass

    # inline void SetTitle(const char* title) {    /* original C++ signature */
    #         Title.Buf.shrink(0);
    #         if (title && ImGui::FindRenderedTextEnd(title, nullptr) != title)
    #             Title.append(title, title + strlen(title) + 1);
    #     }
    def set_title(self, title: str) -> None:
        """(private API)"""
        pass
    # inline bool HasTitle() const { return !Title.empty() && !ImPlot3D::ImHasFlag(Flags, ImPlot3DFlags_NoTitle); }    /* original C++ signature */
    def has_title(self) -> bool:
        """(private API)"""
        pass
    # inline const char* GetTitle() const { return Title.Buf.Data; }    /* original C++ signature */
    def get_title(self) -> str:
        """(private API)"""
        pass

    # void ExtendFit(const ImPlot3DPoint& point);    /* original C++ signature */
    def extend_fit(self, point: Point) -> None:
        """(private API)"""
        pass
    # ImPlot3DPoint RangeMin() const;    /* original C++ signature */
    def range_min(self) -> Point:
        """(private API)"""
        pass
    # ImPlot3DPoint RangeMax() const;    /* original C++ signature */
    def range_max(self) -> Point:
        """(private API)"""
        pass
    # ImPlot3DPoint RangeCenter() const;    /* original C++ signature */
    def range_center(self) -> Point:
        """(private API)"""
        pass
    # void SetRange(const ImPlot3DPoint& min, const ImPlot3DPoint& max);    /* original C++ signature */
    def set_range(self, min: Point, max: Point) -> None:
        """(private API)"""
        pass
    # float GetBoxZoom() const;    /* original C++ signature */
    def get_box_zoom(self) -> float:
        """(private API)"""
        pass

class Context:
    # ImPlot3DPlot* CurrentPlot;    /* original C++ signature */
    current_plot: Plot
    # ImPlot3DItemGroup* CurrentItems;    /* original C++ signature */
    current_items: ItemGroup
    # ImPlot3DNextItemData NextItemData;    /* original C++ signature */
    next_item_data: NextItemData
    # ImPlot3DStyle Style;    /* original C++ signature */
    style: Style
    # ImPlot3DColormapData ColormapData;    /* original C++ signature */
    colormap_data: ColormapData
    # ImPlot3DContext(ImPlot3DNextItemData NextItemData = ImPlot3DNextItemData(), ImPlot3DStyle Style = ImPlot3DStyle(), ImPlot3DColormapData ColormapData = ImPlot3DColormapData());    /* original C++ signature */
    def __init__(self, next_item_data: Optional[NextItemData] = None, style: Optional[Style] = None, colormap_data: Optional[ColormapData] = None) -> None:
        """Auto-generated default constructor with named params
        ---
        Python bindings defaults:
            If any of the params below is None, then its default value below will be used:
                NextItemData: NextItemData()
                Style: Style()
                ColormapData: ColormapData()
        """
        pass

#-----------------------------------------------------------------------------
# [SECTION] Context Pointer
#-----------------------------------------------------------------------------



#-----------------------------------------------------------------------------
# [SECTION] Context Utils
#-----------------------------------------------------------------------------

# IMPLOT3D_API void InitializeContext(ImPlot3DContext* ctx);     /* original C++ signature */
def initialize_context(ctx: Context) -> None:
    """ Initialize ImPlot3DContext"""
    pass
# IMPLOT3D_API void ResetContext(ImPlot3DContext* ctx);          /* original C++ signature */
def reset_context(ctx: Context) -> None:
    """ Reset ImPlot3DContext"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Style Utils
#-----------------------------------------------------------------------------

# IMPLOT3D_API bool IsColorAuto(const ImVec4& col);    /* original C++ signature */
@overload
def is_color_auto(col: ImVec4Like) -> bool:
    pass
# IMPLOT3D_API bool IsColorAuto(ImPlot3DCol idx);    /* original C++ signature */
@overload
def is_color_auto(idx: Col) -> bool:
    pass
# IMPLOT3D_API ImVec4 GetAutoColor(ImPlot3DCol idx);    /* original C++ signature */
def get_auto_color(idx: Col) -> ImVec4:
    pass
# IMPLOT3D_API const char* GetStyleColorName(ImPlot3DCol idx);    /* original C++ signature */
def get_style_color_name(idx: Col) -> str:
    pass

# IMPLOT3D_API const ImPlot3DNextItemData& GetItemData();    /* original C++ signature */
def get_item_data() -> NextItemData:
    """ Get styling data for next item (call between BeginItem/EndItem)"""
    pass

# IMPLOT3D_API ImU32 GetColormapColorU32(int idx, ImPlot3DColormap cmap);    /* original C++ signature */
def get_colormap_color_u32(idx: int, cmap: Colormap) -> ImU32:
    """ Returns a color from the Color map given an index >= 0 (modulo will be performed)"""
    pass

# IMPLOT3D_API ImU32 NextColormapColorU32();    /* original C++ signature */
def next_colormap_color_u32() -> ImU32:
    """ Returns the next unused colormap color and advances the colormap. Can be used to skip colors if desired"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Item Utils
#-----------------------------------------------------------------------------

# IMPLOT3D_API bool BeginItem(const char* label_id, ImPlot3DItemFlags flags = 0, ImPlot3DCol recolor_from = IMPLOT3D_AUTO);    /* original C++ signature */
def begin_item(label_id: str, flags: ItemFlags = 0, recolor_from: Optional[Col] = None) -> bool:
    """---
    Python bindings defaults:
        If recolor_from is None, then its default value will be: IMPLOT3D_AUTO
    """
    pass
# IMPLOT3D_API void EndItem();    /* original C++ signature */
def end_item() -> None:
    pass

# IMPLOT3D_API ImPlot3DItem* RegisterOrGetItem(const char* label_id, ImPlot3DItemFlags flags, bool* just_created = nullptr);    /* original C++ signature */
def register_or_get_item(label_id: str, flags: ItemFlags, just_created: Optional[bool] = None) -> Tuple[Item , Optional[bool]]:
    """ Register or get an existing item from the current plot"""
    pass

# IMPLOT3D_API void BustItemCache();    /* original C++ signature */
def bust_item_cache() -> None:
    """ Busts the cache for every item for every plot in the current context"""
    pass

# IMPLOT3D_API void AddTextRotated(ImDrawList* draw_list, ImVec2 pos, float angle, ImU32 col, const char* text_begin, const char* text_end = nullptr);    /* original C++ signature */
def add_text_rotated(draw_list: ImDrawList, pos: ImVec2Like, angle: float, col: ImU32, text_begin: str, text_end: Optional[str] = None) -> None:
    """ TODO move to another place"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Plot Utils
#-----------------------------------------------------------------------------

# IMPLOT3D_API ImPlot3DPlot* GetCurrentPlot();    /* original C++ signature */
def get_current_plot() -> Plot:
    """ Gets the current plot from the current ImPlot3DContext"""
    pass

# IMPLOT3D_API void BustPlotCache();    /* original C++ signature */
def bust_plot_cache() -> None:
    """ Busts the cache for every plot in the current context"""
    pass

# IMPLOT3D_API ImVec2 GetFramePos();      /* original C++ signature */
def get_frame_pos() -> ImVec2:
    """ Get the current frame position (top-left) in pixels"""
    pass
# IMPLOT3D_API ImVec2 GetFrameSize();     /* original C++ signature */
def get_frame_size() -> ImVec2:
    """ Get the current frame size in pixels"""
    pass

# Convert a position in the current plot's coordinate system to the current plot's normalized device coordinate system (NDC)
# When the cube aspect ratio is [1,1,1], the NDC varies from [-0.5, 0.5] in each axis
# IMPLOT3D_API ImPlot3DPoint PlotToNDC(const ImPlot3DPoint& point);    /* original C++ signature */
def plot_to_ndc(point: Point) -> Point:
    pass
# IMPLOT3D_API ImPlot3DPoint NDCToPlot(const ImPlot3DPoint& point);    /* original C++ signature */
def ndc_to_plot(point: Point) -> Point:
    pass
# IMPLOT3D_API ImVec2 NDCToPixels(const ImPlot3DPoint& point);    /* original C++ signature */
def ndc_to_pixels(point: Point) -> ImVec2:
    """ Convert a position in the current plot's NDC to pixels"""
    pass
# IMPLOT3D_API ImPlot3DRay PixelsToNDCRay(const ImVec2& pix);    /* original C++ signature */
def pixels_to_ndc_ray(pix: ImVec2Like) -> Ray:
    """ Convert a pixel coordinate to a ray in the NDC"""
    pass
# IMPLOT3D_API ImPlot3DRay NDCRayToPlotRay(const ImPlot3DRay& ray);    /* original C++ signature */
def ndc_ray_to_plot_ray(ray: Ray) -> Ray:
    """ Convert a ray in the NDC to a ray in the current plot's coordinate system"""
    pass

#-----------------------------------------------------------------------------
# [SECTION] Setup Utils
#-----------------------------------------------------------------------------

# IMPLOT3D_API void SetupLock();    /* original C++ signature */
def setup_lock() -> None:
    pass

#-----------------------------------------------------------------------------
# [SECTION] Formatter
#-----------------------------------------------------------------------------


#------------------------------------------------------------------------------
# [SECTION] Locator
#------------------------------------------------------------------------------



# namespace ImPlot3D

# #endif
####################    </generated_from:implot3d_internal.h>    ####################

# </litgen_stub>
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  AUTOGENERATED CODE END !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
