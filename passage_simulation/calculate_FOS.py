from constants import *

class CalculateFactorsOfSafety:
    def __init__(self, passage_simulation):
        self.passage_simulation = passage_simulation
        self.calculate_factors_of_safety()

    def calculate_factors_of_safety(self):
        self.calculate_tensile_rupture_FOS_information()
        self.calculate_compressive_crushing_FOS_information()
        self.calculate_matboard_shear_failure_FOS_information()
        self.calculate_glue_shear_failure_FOS_information()

    def calculate_tensile_rupture_FOS_information(self):
        minimum_FOS = 1e9
        minimum_FOS_beam_x = 0
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            FOS = self.passage_simulation.tensile_rupture_FOS_diagram[beam_x]
            if FOS < minimum_FOS:
                minimum_FOS = FOS
                minimum_FOS_beam_x = beam_x
        self.passage_simulation.tensile_rupture_FOS_information = {
            "FOS": minimum_FOS,
            "beam_x": minimum_FOS_beam_x
        }

    def calculate_compressive_crushing_FOS_information(self):
        minimum_FOS = 1e9
        minimum_FOS_beam_x = 0
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            FOS = self.passage_simulation.compressive_crushing_FOS_diagram[beam_x]
            if FOS < minimum_FOS:
                minimum_FOS = FOS
                minimum_FOS_beam_x = beam_x
        self.passage_simulation.compressive_crushing_FOS_information = {
            "FOS": minimum_FOS,
            "beam_x": minimum_FOS_beam_x
        }

    def calculate_matboard_shear_failure_FOS_information(self):
        minimum_FOS = 1e9
        minimum_FOS_beam_x = 0
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            FOS = self.passage_simulation.matboard_shear_failure_FOS_diagram[beam_x]
            if FOS < minimum_FOS:
                minimum_FOS = FOS
                minimum_FOS_beam_x = beam_x
        self.passage_simulation.matboard_shear_failure_FOS_information = {
            "FOS": minimum_FOS,
            "beam_x": minimum_FOS_beam_x
        }

    def calculate_glue_shear_failure_FOS_information(self):
        minimum_FOS = 1e9
        minimum_FOS_beam_x = 0
        for beam_x in range(0, BRIDGE_LENGTH + 1):
            FOS = self.passage_simulation.glue_shear_failure_FOS_diagram[beam_x]
            if FOS < minimum_FOS:
                minimum_FOS = FOS
                minimum_FOS_beam_x = beam_x
        self.passage_simulation.glue_shear_failure_FOS_information = {
            "FOS": minimum_FOS,
            "beam_x": minimum_FOS_beam_x
        }