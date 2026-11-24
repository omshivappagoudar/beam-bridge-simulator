from constants import *

class AnalyzeLocalBuckling:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.cross_section.max_M_before_case_1_buckling = 1e9
        self.cross_section.max_M_before_case_2_buckling = 1e9
        self.cross_section.max_M_before_case_3_buckling = 1e9
        self.cross_section.max_V_before_case_4_buckling = 1e9
        self.analyze_local_buckling()

    def analyze_local_buckling(self):
        for buckling_region in self.cross_section.buckling_regions:
            if buckling_region["buckling_case"] == 1:
                self.analyze_case_1_buckling(buckling_region)
            elif buckling_region["buckling_case"] == 2:
                self.analyze_case_2_buckling(buckling_region)
            elif buckling_region["buckling_case"] == 3:
                self.analyze_case_3_buckling(buckling_region)
            elif buckling_region["buckling_case"] == 4:
                self.analyze_case_4_buckling(buckling_region)

    def analyze_case_1_buckling(self, buckling_region):
        K = 4
        pi = 3.141592653589793
        E = MATBOARD_YOUNGS_MODULUS
        I = self.cross_section.moment_of_inertia
        t = buckling_region["t"]
        mu = POISSONS_RATIO
        y = self.cross_section.cross_section_height
        y_bar = self.cross_section.centroid
        b = buckling_region["b"]
        max_M = K * (pi ** 2) * E * (t ** 2) * I / (12 * (1 - mu ** 2) * (y - y_bar) * (b ** 2))
        self.cross_section.max_M_before_case_1_buckling = min(
            self.cross_section.max_M_before_case_1_buckling,
            max_M
        )

    def analyze_case_2_buckling(self, buckling_region):
        K = 0.425
        pi = 3.141592653589793
        E = MATBOARD_YOUNGS_MODULUS
        I = self.cross_section.moment_of_inertia
        t = buckling_region["t"]
        mu = POISSONS_RATIO
        y = self.cross_section.cross_section_height
        y_bar = self.cross_section.centroid
        b = buckling_region["b"]
        max_M = K * (pi ** 2) * E * (t ** 2) * I / (12 * (1 - mu ** 2) * (y - y_bar) * (b ** 2))
        self.cross_section.max_M_before_case_2_buckling = min(
            self.cross_section.max_M_before_case_2_buckling,
            max_M
        )

    def analyze_case_3_buckling(self, buckling_region):
        K = 6
        pi = 3.141592653589793
        E = MATBOARD_YOUNGS_MODULUS
        I = self.cross_section.moment_of_inertia
        t = buckling_region["t"]
        mu = POISSONS_RATIO
        y = buckling_region["b"]
        b = buckling_region["b"]
        max_M = K * (pi ** 2) * E * (t ** 2) * I / (12 * (1 - mu ** 2) * y * (b ** 2))
        self.cross_section.max_M_before_case_3_buckling = min(
            self.cross_section.max_M_before_case_3_buckling,
            max_M
        )

    def analyze_case_4_buckling(self, buckling_region):
        K = 5
        pi = 3.141592653589793
        E = MATBOARD_YOUNGS_MODULUS
        mu = POISSONS_RATIO
        I = self.cross_section.moment_of_inertia
        Q = self.cross_section.greatest_shear_Q
        t = buckling_region["t"]
        h = buckling_region["h"]
        a = buckling_region["a"]
        b = self.cross_section.greatest_shear_b
        
        tau_failure = K * (pi ** 2) * E / (12 * (1 - mu ** 2)) * ((t / h) ** 2 + (t / a) ** 2)
        max_V = tau_failure * I * b / Q
        
        self.cross_section.max_V_before_case_4_buckling = min(
            self.cross_section.max_V_before_case_4_buckling,
            max_V
        )