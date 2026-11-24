def calculate_centroid(pieces):
    first_moment = 0
    total_area = 0
    for piece in pieces:
        area = piece["b"] * piece["h"]
        total_area += area
        first_moment += area * piece["y"]
    return first_moment / total_area

def calculate_total_height(pieces):
    cross_section_height = 0
    for piece in pieces:
        cross_section_height = max(cross_section_height, piece["y"] + piece["h"] / 2)
    return cross_section_height