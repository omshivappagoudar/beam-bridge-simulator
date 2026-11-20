from constants import *
import numpy as np

"""

DOCUMENTATION OF THE CrossSectionAnalysis CLASS.

===== CONSTRUCTOR INPUTS =====

pieces = [
    {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 1
    {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 2
    {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)}, # Piece 3
    ...
    {"b": base (mm), "h": height (mm), "y": distance from bottom (mm)} # Piece N
]

"""

class CrossSectionAnalysis:

    def __init__(self, pieces):
        self._pieces = pieces
        self.area = self._calculate_area()
        self.centroid = self._calculate_centroid()
        self.moment_of_inertia = self._calculate_moment_of_inertia()
        self._calculate_cross_section_height()
        self._calculate_weakest_y_with_respect_to_shear_stress()
        self._calculate_bridge_volume()
        self._calculate_bridge_weight()

    def get_area(self):
        return self.area

    def get_centroid(self):
        return self.centroid

    def get_moment_of_inertia(self):
        return self.moment_of_inertia

    def get_volume(self):
        return self.volume

    def get_weight(self):
        return self.weight

    def calculate_shear_stress(self, V, y): # tau_xy = VQ/Ib, in MPa
        return V * self._calculate_Q(y) / (self.moment_of_inertia * self._calculate_total_intersection(y))

    def calculate_greatest_shear_stress_information(self, V):
        return {"tau_xy": self.calculate_shear_stress(V, self._shear_weakest_y), "y": self._shear_weakest_y}

    def calculate_maximum_tensile_stress(self, M):
        y = self.centroid
        return M * y / self.moment_of_inertia

    def calculate_maximum_compressive_stress(self, M):
        y = self._max_height - self.centroid
        return M * y / self.moment_of_inertia

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

    def _calculate_bridge_volume(self):
        self.volume = self.area * BRIDGE_LENGTH

    def _calculate_bridge_weight(self):
        self.weight = self.volume * MATBOARD_WEIGHT_DENSITY
    
    def _calculate_total_intersection(self, y): # in mm; the total length of the intersection of the beam with the horizontal line at height y
        total_intersection = 0
        for piece in self._pieces:
            deviation = y - piece["y"]
            if -piece["h"] / 2 - 1e-10 < deviation and deviation <= 0:
                total_intersection += piece["b"]
            elif 0 < deviation and deviation <= piece["h"] / 2 - 1e-10:
                total_intersection += piece["b"]
        return total_intersection

    def _calculate_Q(self, y, dy = 0.1):
        Q = 0
        for y_current in np.arange(0, y, dy):
            Q += (y_current - self.get_centroid()) * self._calculate_total_intersection(y_current) * dy
        return Q

    def _calculate_cross_section_height(self):
        self._max_height = 0
        for piece in self._pieces:
            self._max_height = max(self._max_height, piece["y"] + piece["h"] / 2)

    def _calculate_weakest_y_with_respect_to_shear_stress(self, dy = 0.1):
        self._shear_weakest_y = 0
        weakest_Qb = 0
        for y in np.arange(0, int(self._max_height + 1), dy):
            intersection = self._calculate_total_intersection(y)
            if intersection < 1e-6: continue
            Qb_ratio = self._calculate_Q(y) / intersection
            if abs(Qb_ratio) > abs(weakest_Qb):
                self._shear_weakest_y = y
                weakest_Qb = Qb_ratio