from cross_section_analysis.constraint import *
from constants import *

class BeamBridge:
    def __init__(self, cross_sections):
        self.cross_sections = cross_sections

    def get_relevant_constraints(self, beam_x):
        for cross_section in self.cross_sections:
            if cross_section.start_beam_x <= beam_x and beam_x <= cross_section.end_beam_x:
                return cross_section.constraints