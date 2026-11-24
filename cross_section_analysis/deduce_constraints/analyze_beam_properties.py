from constants import *

class AnalyzeBeamProperties:
    def __init__(self, cross_section):
        self.cross_section = cross_section

        self.calculate_area()
        self.calculate_centroid()
        self.calculate_moment_of_inertia()
        self.calculate_cross_section_height()
        self.calculate_cross_section_volume()
        self.calculate_cross_section_weight()

    def calculate_area(self):
        total_area = 0
        for piece in self.cross_section.pieces:
            total_area += piece["b"] * piece["h"]
        self.cross_section.area = total_area

    def calculate_centroid(self):
        first_moment = 0
        for piece in self.cross_section.pieces:
            area = piece["b"] * piece["h"]
            first_moment += area * piece["y"]
        self.cross_section.centroid = first_moment / self.cross_section.area

    def calculate_moment_of_inertia(self):
        I = 0
        for piece in self.cross_section.pieces:
            b = piece["b"]
            h = piece["h"]
            y = piece["y"]
            area = b * h
            I_local = b * (h ** 3) / 12
            I += I_local + area * ((y - self.cross_section.centroid) ** 2)
        self.cross_section.moment_of_inertia = I

    def calculate_cross_section_height(self):
        self.cross_section.cross_section_height = 0
        for piece in self.cross_section.pieces:
            self.cross_section.cross_section_height = max(self.cross_section.cross_section_height, piece["y"] + piece["h"] / 2)

    def calculate_cross_section_volume(self):
        self.cross_section.volume = self.cross_section.area * (self.cross_section.end_beam_x - self.cross_section.start_beam_x)

    def calculate_cross_section_weight(self):
        self.cross_section.weight = self.cross_section.volume * MATBOARD_DENSITY