from analyze_FBD import *
from constants_and_conventions import *

"""

DOCUMENTATION OF THE AnalyzeFBD CLASS.

===== CONSTRUCTOR INPUTS =====

train_loads = [P1, P2, P3, P4, P5, P6] are the six point-loads induced by the train wheels.

===== CLASS OUTPUTS =====

self.passage_analysis is a dictionary, where self.passage_analysis[x] returns the AnalyzeFBD output
(including the shear force/bending moment diagrams) for the inputted train load configuration
when the left-most wheel of the train is x millimeters to the right of the center of the left support.

self._greatest_shear_force_information = {"V": __, "beam_x": __, "train_x": __}
self._greatest_bending_moment_information = {"M": __, "beam_x": __, "train_x": __}

"""

class PassageSimulation:

    def __init__(self, loading_case):
        self._loading_case = loading_case
        self._analyze_passage()
        self._calculate_extreme_values()

    def get_frame_analysis(self, train_x):
        return self.passage_analysis[train_x]

    def get_greatest_shear_force_information(self):
        return self._greatest_shear_force_information

    def get_greatest_bending_moment_information(self):
        return self._greatest_bending_moment_information

    def _analyze_passage(self):
        self.passage_analysis = {}
        for train_location in range(-TRAIN_LENGTH, BRIDGE_LENGTH):
            self.passage_analysis[train_location] = AnalyzeFBD(self._loading_case, train_location)

    def _calculate_extreme_values(self):
        self._greatest_shear_force_information = {"V": 0, "beam_x": 0, "train_x": 0}
        self._greatest_bending_moment_information = {"M": 0, "beam_x": 0, "train_x": 0}
        for train_x in range(-TRAIN_LENGTH, BRIDGE_LENGTH):
            passage_analysis = self.passage_analysis[train_x]
            greatest_shear_force_information = passage_analysis.get_greatest_shear_force_information()
            greatest_bending_moment_information = passage_analysis.get_greatest_bending_moment_information()
            if abs(greatest_shear_force_information["V"]) > abs(self._greatest_shear_force_information["V"]):
                self._greatest_shear_force_information["V"] = greatest_shear_force_information["V"]
                self._greatest_shear_force_information["beam_x"] = greatest_shear_force_information["beam_x"]
                self._greatest_shear_force_information["train_x"] = train_x
            if abs(greatest_bending_moment_information["M"]) > abs(self._greatest_bending_moment_information["M"]):
                self._greatest_bending_moment_information["M"] = greatest_bending_moment_information["M"]
                self._greatest_bending_moment_information["beam_x"] = greatest_bending_moment_information["beam_x"]
                self._greatest_bending_moment_information["train_x"] = train_x