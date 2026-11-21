from constants import *

class AnalyzeTensileStress:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.analyze_tensile_rupture()

    def analyze_tensile_rupture(self):
        I = self.cross_section.moment_of_inertia
        sigma_t_max = MATBOARD_TENSILE_FAILURE_STRESS
        y = self.cross_section.centroid
        self.cross_section.max_M_before_tensile_rupture = I * sigma_t_max / y