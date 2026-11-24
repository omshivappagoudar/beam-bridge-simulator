from constants import *

from cross_section_analysis.deduce_constraints.analyze_beam_properties import *
from cross_section_analysis.deduce_constraints.analyze_matboard_shear import *
from cross_section_analysis.deduce_constraints.analyze_glue_shear import *
from cross_section_analysis.deduce_constraints.analyze_tensile_stress import *
from cross_section_analysis.deduce_constraints.analyze_compressive_stress import *
from cross_section_analysis.deduce_constraints.analyze_local_buckling import *
from cross_section_analysis.aggregate_constraints import *

class CrossSection:

    def __init__(self, pieces, glue_list, buckling_regions, start_beam_x, end_beam_x, cross_section_id):
        self.pieces = pieces
        self.glue_list = glue_list
        self.buckling_regions = buckling_regions
        self.start_beam_x = start_beam_x
        self.end_beam_x = end_beam_x
        self.cross_section_id = cross_section_id

        AnalyzeBeamProperties(self)
        AnalyzeMatboardShear(self)
        AnalyzeGlueShear(self)
        AnalyzeTensileStress(self)
        AnalyzeCompressiveStress(self)
        AnalyzeLocalBuckling(self)

        AggregateConstraints(self)

    def get_area(self):
        return self.area

    def get_centroid(self):
        return self.centroid

    def get_moment_of_inertia(self):
        return self.moment_of_inertia
    
    def calculate_b(self, y):
        total_intersection = 0
        for piece in self.pieces:
            deviation = y - piece["y"]
            if -piece["h"] / 2 - 1e-10 < deviation and deviation <= piece["h"] / 2 - 1e-10:
                total_intersection += piece["b"]
        return total_intersection

    def calculate_Q(self, y):
        Q = 0
        for piece in self.pieces:
            y_top = piece["y"] + piece["h"] / 2
            height_above_y = max(0, y_top - y)
            if height_above_y < 1e-6:
                continue
            height_above_y = min(height_above_y, piece["h"])
            d = (y_top - height_above_y / 2) - self.centroid
            Q += piece["b"] * height_above_y * d
        return Q