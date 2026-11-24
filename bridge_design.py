from cross_section_analysis.cross_section import *
from cross_section_analysis.beam_bridge import *


def flange_piece(name, sheet_id, width, thickness, y, case):
    """Create a horizontal flange region."""
    return {
        "name": name,
        "sheet_id": sheet_id,
        "b": width,
        "h": thickness,
        "y": y,
        "buckling": {
            "case": case,
            "thickness": thickness,
            "unsupported_width": width,
        },
    }


# Example dimensions for testing.
thickness = 1.27
left_overhang = 10.0
middle_width = 80.0
right_overhang = 10.0

cross_section_0_pieces = [
    flange_piece(
        "top_left_overhang",
        "top_sheet",
        left_overhang,
        thickness,
        75 + thickness / 2,
        "one_edge_free",
    ),
    flange_piece(
        "top_between_webs",
        "top_sheet",
        middle_width,
        thickness,
        75 + thickness / 2,
        "both_edges_supported",
    ),
    flange_piece(
        "top_right_overhang",
        "top_sheet",
        right_overhang,
        thickness,
        75 + thickness / 2,
        "one_edge_free",
    ),
    {
        "name": "left_glue_tab",
        "sheet_id": "left_glue_tab",
        "b": 6.27,
        "h": thickness,
        "y": 75 - thickness / 2,
        "buckling": None,
    },
    {
        "name": "right_glue_tab",
        "sheet_id": "right_glue_tab",
        "b": 6.27,
        "h": thickness,
        "y": 75 - thickness / 2,
        "buckling": None,
    },
    {
        "name": "left_web",
        "sheet_id": "left_web",
        "b": thickness,
        "h": 75 - 2 * thickness,
        "y": 75 / 2,
        "buckling": None,
    },
    {
        "name": "right_web",
        "sheet_id": "right_web",
        "b": thickness,
        "h": 75 - 2 * thickness,
        "y": 75 / 2,
        "buckling": None,
    },
    {
        "name": "bottom_flange",
        "sheet_id": "bottom_sheet",
        "b": 80,
        "h": thickness,
        "y": thickness / 2,
        "buckling": None,
    },
]

cross_section_0 = CrossSection(
    pieces=cross_section_0_pieces,
    glue_y_list=[1.27, 75],
    start_beam_x=0,
    end_beam_x=1200,
    cross_section_id=0,
)

beam_bridge = BeamBridge([cross_section_0])