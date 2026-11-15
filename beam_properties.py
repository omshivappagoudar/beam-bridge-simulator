class BeamProperties:

    def __init__(self, pieces):
        # Each instance stores its own copy of the pieces
        self._pieces = [piece.copy() for piece in pieces]

        # Calculate important properties of the cross section
        self.area = self._calculate_area()
        self.y_bar = self._calculate_centroid()
        self.I = self._calculate_moment_of_inertia()

    def _calculate_area(self):
        total_area = 0.0

        for piece in self._pieces:
            total_area += piece["b"] * piece["h"]

        return total_area

    def _calculate_centroid(self):
        first_moment = 0.0

        for piece in self._pieces:
            area = piece["b"] * piece["h"]
            first_moment += area * piece["y"]

        return first_moment / self.area

    def _calculate_moment_of_inertia(self):
        y_bar = self.y_bar
        I = 0.0

        for piece in self._pieces:
            b = piece["b"]
            h = piece["h"]
            y = piece["y"]

            area = b * h
            I_local = b * h**3 / 12

            I += I_local + area * (y - self.y_bar)**2

        return I