from cross_section_analysis.cross_section import *
from cross_section_analysis.beam_bridge import *

cross_section_0_pieces = [
    {"b": 100, "h": 1.27, "y": 75 + 1.27 / 2}, # Piece 1
    {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 2
    {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 3
    {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 4
    {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 5
    {"b": 80, "h": 1.27, "y": 1.27 / 2}, # Piece 6
]
glue_y_list_0 = [1.27, 75]
cross_section_0 = CrossSection(
    pieces = cross_section_0_pieces,
    glue_y_list = glue_y_list_0,
    start_beam_x = 0,
    end_beam_x = 1200,
    cross_section_id = 0
)

cross_sections = [cross_section_0]

beam_bridge = BeamBridge(cross_sections)