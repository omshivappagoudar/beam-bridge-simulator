from constants import *

class AnalyzeGlueShear:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.analyze_glue_shear()

    def analyze_glue_shear(self):
        self.cross_section.max_V_before_glue_shear_failure = 1e9
        for glue in self.cross_section.glue_list:
            current_max_V = self.glue_section_max_V(glue)
            self.cross_section.max_V_before_glue_shear_failure = min(self.cross_section.max_V_before_glue_shear_failure, current_max_V)

    def glue_section_max_V(self, glue):
        I = self.cross_section.moment_of_inertia
        b = glue["b"]
        Q = self.cross_section.calculate_Q(glue["y"])
        max_V = abs(CONTACT_CEMENT_SHEAR_FAILURE_STRESS * I * b / Q)
        return max_V