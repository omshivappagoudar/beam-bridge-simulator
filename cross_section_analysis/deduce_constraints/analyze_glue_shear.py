from constants import *

class AnalyzeGlueShear:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.analyze_glue_shear()

    def analyze_glue_shear(self):
        self.cross_section.max_V_before_glue_shear_failure = 1e9
        for glue_y in self.cross_section.glue_y_list:
            current_max_V = self.glue_y_max_V(glue_y)
            self.cross_section.max_V_before_glue_shear_failure = min(self.cross_section.max_V_before_glue_shear_failure, current_max_V)

    def glue_y_max_V(self, glue_y):
        I = self.cross_section.moment_of_inertia
        b = self.cross_section.calculate_b(glue_y)
        Q = self.cross_section.calculate_Q(glue_y)
        max_V = abs(CONTACT_CEMENT_SHEAR_FAILURE_STRESS * I * b / Q)
        return max_V