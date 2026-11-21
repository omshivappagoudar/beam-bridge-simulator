from constants import *

class AnalyzeMatboardShear:
    def __init__(self, cross_section):
        self.cross_section = cross_section

        self.calculate_weakest_y_for_shear_failure()
        self.analyze_shear_failure()

    def calculate_weakest_y_for_shear_failure(self):
        candidate_y = []
        for piece in self.cross_section.pieces:
            y_top = piece["y"] + piece["h"] / 2
            y_bottom = piece["y"] - piece["h"] / 2
            if abs(y_top - self.cross_section.centroid) < abs(y_bottom - self.cross_section.centroid):
                candidate_y.append(y_top + 1e-6)
                candidate_y.append(y_top - 1e-6)
            else:
                candidate_y.append(y_bottom + 1e-6)
                candidate_y.append(y_bottom - 1e-6)
        candidate_y.append(self.cross_section.centroid)
        self.cross_section.greatest_shear_y = 0
        self.cross_section.greatest_shear_Q = 0
        weakest_Qb = 0
        for y in candidate_y:
            intersection = self.cross_section.calculate_b(y)
            if intersection < 1e-6: continue
            Q = self.cross_section.calculate_Q(y)
            Qb_ratio = Q / intersection
            if abs(Qb_ratio) > abs(weakest_Qb):
                self.cross_section.greatest_shear_y = y
                self.cross_section.greatest_shear_Q = Q
                self.cross_section.greatest_shear_b = intersection
                weakest_Qb = Qb_ratio

    def analyze_shear_failure(self):
        self.cross_section.max_V_before_matboard_shear_failure = abs(MATBOARD_SHEAR_FAILURE_STRESS * self.cross_section.moment_of_inertia * self.cross_section.greatest_shear_b / self.cross_section.greatest_shear_Q)