from constants import *

class AnalyzeCompressiveStress:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.analyze_compressive_crushing()

    def analyze_compressive_crushing(self):
        I = self.cross_section.moment_of_inertia
        sigma_c_max = MATBOARD_COMPRESSIVE_FAILURE_STRESS
        y = self.cross_section.cross_section_height - self.cross_section.centroid
        self.cross_section.max_M_before_compressive_crushing = I * sigma_c_max / y