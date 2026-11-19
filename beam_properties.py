class BeamProperties:

    def __init__(self, pieces):
        """
        pieces = [
            {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 1
            {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 2
            {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 3
            ...
            {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)} # Piece N
        ]
        """

        self._pieces = pieces
        self.area = self._calculate_area()
        self.centroid = self._calculate_centroid()
        self.moment_of_inertia = self._calculate_moment_of_inertia()

    def _calculate_area(self):
        total_area = 0
        for piece in self._pieces:
            total_area += piece["b"] * piece["h"]
        return total_area

    def _calculate_centroid(self):
        first_moment = 0
        for piece in self._pieces:
            area = piece["b"] * piece["h"]
            first_moment += area * piece["y"]
        return first_moment / self.area

    def _calculate_moment_of_inertia(self):
        y_bar = self.centroid
        I = 0
        for piece in self._pieces:
            b = piece["b"]
            h = piece["h"]
            y = piece["y"]
            area = b * h
            I_local = b * (h ** 3) / 12
            I += I_local + area * ((y - self.centroid) ** 2)
        return I