class AnalyzeBeamProperties:
    def __init__(self, cross_section):
        self.cross_section = cross_section

        self.calculate_area()
        self.calculate_centroid()
        self.calculate_moment_of_inertia()

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