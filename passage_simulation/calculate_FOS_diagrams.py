from constants import *
from cross_section_analysis.constraint import *

class CalculateFactorOfSafetyDiagrams:
    def __init__(self, passage_simulation):
        self.passage_simulation = passage_simulation
        self.calculate_FOS_diagrams()

    def calculate_FOS_diagrams(self):
        self.passage_simulation.tensile_rupture_FOS_diagram = [0] * (BRIDGE_LENGTH + 1)
        self.passage_simulation.compressive_crushing_FOS_diagram = [0] * (BRIDGE_LENGTH + 1)
        self.passage_simulation.matboard_shear_failure_FOS_diagram = [0] * (BRIDGE_LENGTH + 1)
        self.passage_simulation.glue_shear_failure_FOS_diagram = [0] * (BRIDGE_LENGTH + 1)
        self.calculate_tensile_rupture_FOS_diagram()
        self.calculate_compressive_crushing_FOS_diagram()
        self.calculate_matboard_shear_failure_FOS_diagram()
        self.calculate_glue_shear_failure_FOS_diagram()

    def calculate_tensile_rupture_FOS_diagram(self):
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            constraint = self.passage_simulation.beam_bridge.get_relevant_constraints(beam_x)[CONSTRAINT_AGAINST_TENSILE_RUPTURE]
            max_M = constraint.maximum_value
            self.passage_simulation.tensile_rupture_FOS_diagram[beam_x] = max_M / (self.passage_simulation.maximum_bending_moment_diagram[beam_x] + 1e-6)

    def calculate_compressive_crushing_FOS_diagram(self):
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            constraint = self.passage_simulation.beam_bridge.get_relevant_constraints(beam_x)[CONSTRAINT_AGAINST_COMPRESSIVE_CRUSHING]
            max_M = constraint.maximum_value
            self.passage_simulation.compressive_crushing_FOS_diagram[beam_x] = max_M / (self.passage_simulation.maximum_bending_moment_diagram[beam_x] + 1e-6)

    def calculate_matboard_shear_failure_FOS_diagram(self):
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            constraint = self.passage_simulation.beam_bridge.get_relevant_constraints(beam_x)[CONSTRAINT_AGAINST_MATBOARD_SHEAR_FAILURE]
            max_V = constraint.maximum_value
            self.passage_simulation.matboard_shear_failure_FOS_diagram[beam_x] = max_V / (self.passage_simulation.maximum_shear_force_diagram[beam_x] + 1e-6)

    def calculate_glue_shear_failure_FOS_diagram(self):
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            constraint = self.passage_simulation.beam_bridge.get_relevant_constraints(beam_x)[CONSTRAINT_AGAINST_GLUE_SHEAR_FAILURE]
            max_V = constraint.maximum_value
            self.passage_simulation.glue_shear_failure_FOS_diagram[beam_x] = max_V / (self.passage_simulation.maximum_shear_force_diagram[beam_x] + 1e-6)