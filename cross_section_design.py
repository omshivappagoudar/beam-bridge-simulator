from cross_section_analysis import CrossSectionAnalysis

# ===== POTENTIAL DESIGNS =====

DESIGN_0 = [
    {"b": 100, "h": 1.27, "y": 75 + 1.27 / 2}, # Piece 1
    {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 2
    {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 3
    {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 4
    {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 5
    {"b": 80, "h": 1.27, "y": 1.27 / 2}, # Piece 6
]

# ===== CHOSEN DESIGN =====

CHOSEN_DESIGN = DESIGN_0

cross_section = CrossSectionAnalysis(DESIGN_0)