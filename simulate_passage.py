from analyze_FBD import *
from constants_and_conventions import *
import time

"""

DOCUMENTATION OF THE PassageSimultaion CLASS.

===== CONSTRUCTOR INPUTS =====

train_loads = [P1, P2, P3, P4, P5, P6] are the six point-loads induced by the train wheels, in Newtons.

===== CLASS OUTPUTS =====

self.passage_analysis is a dictionary, where self.passage_analysis[train_x] returns the AnalyzeFBD output
(including the shear force/bending moment diagrams) for the inputted train load configuration
when the left-most wheel of the train is x millimeters to the right of the center of the left support.

self._greatest_shear_force_information = {"V": __, "beam_x": __, "train_x": __}
self._greatest_bending_moment_information = {"M": __, "beam_x": __, "train_x": __}

"""

class PassageSimulation:

    def __init__(self, loading_case, start_train_x = -TRAIN_LENGTH, end_train_x = BRIDGE_LENGTH):
        self._loading_case = loading_case
        self._start_train_x = start_train_x
        self._end_train_x = end_train_x
        self._analyze_passage()
        self._calculate_extreme_values()

    def get_frame_analysis(self, train_x):
        return self.passage_analysis[train_x]

    def get_greatest_shear_force_information(self):
        return self._greatest_shear_force_information

    def get_greatest_bending_moment_information(self):
        return self._greatest_bending_moment_information

    def get_greatest_shear_stress_information(self):
        return self._greatest_bending_moment_information

    def get_greatest_tensile_stress_information(self):
        return self._greatest_tensile_stress_information

    def get_greatest_compressive_stress_information(self):
        return self._greatest_compressive_stress_information

    def _analyze_passage(self):
        self.passage_analysis = {}
        whole_start = time.time()
        for train_x in range(self._start_train_x, self._end_train_x):

            start = time.time()
            self.passage_analysis[train_x] = AnalyzeFBD(self._loading_case, train_x)
            end = time.time()

            percentage = (train_x - (-TRAIN_LENGTH)) / (BRIDGE_LENGTH - (-TRAIN_LENGTH)) * 100
            print(f"Finished analyzing train_x = {train_x} ({percentage:.2f}%); {end - start:.2f} seconds per frame")
        whole_end = time.time()
        print(f"Finished analyzing the passage from train_x = {self._start_train_x} mm to train_x = {self._end_train_x} mm. Total computation time: {whole_end - whole_start:.2f} seconds.")

    def _calculate_extreme_values(self):
        self._greatest_shear_force_information = {"V": 0, "beam_x": 0, "train_x": 0}
        self._greatest_bending_moment_information = {"M": 0, "beam_x": 0, "train_x": 0}
        self._greatest_shear_stress_information = {"tau_xy": 0, "beam_x": 0, "train_x": 0}
        self._greatest_tensile_stress_information = {"sigma_t": 0, "beam_x": 0, "train_x": 0}
        self._greatest_compressive_stress_information = {"sigma_c": 0, "beam_x": 0, "train_x": 0}
        for train_x in range(self._start_train_x, self._end_train_x):
            passage_analysis = self.passage_analysis[train_x]
            train_x_greatest_shear_force_information = passage_analysis.get_greatest_shear_force_information()
            train_x_greatest_bending_moment_information = passage_analysis.get_greatest_bending_moment_information()
            train_x_greatest_shear_stress_information = passage_analysis.get_greatest_shear_stress_information()
            train_x_greatest_tensile_stress_information = passage_analysis.get_greatest_tensile_stress_information()
            train_x_greatest_compressive_stress_information = passage_analysis.get_greatest_compressive_stress_information()
            if abs(train_x_greatest_shear_force_information["V"]) > abs(self._greatest_shear_force_information["V"]):
                self._greatest_shear_force_information["V"] = train_x_greatest_shear_force_information["V"]
                self._greatest_shear_force_information["beam_x"] = train_x_greatest_shear_force_information["beam_x"]
                self._greatest_shear_force_information["train_x"] = train_x
            if abs(train_x_greatest_bending_moment_information["M"]) > abs(self._greatest_bending_moment_information["M"]):
                self._greatest_bending_moment_information["M"] = train_x_greatest_bending_moment_information["M"]
                self._greatest_bending_moment_information["beam_x"] = train_x_greatest_bending_moment_information["beam_x"]
                self._greatest_bending_moment_information["train_x"] = train_x
            if abs(train_x_greatest_shear_stress_information["tau_xy"]) > abs(self._greatest_shear_stress_information["tau_xy"]):
                self._greatest_shear_stress_information["tau_xy"] = train_x_greatest_shear_stress_information["tau_xy"]
                self._greatest_shear_stress_information["beam_x"] = train_x_greatest_shear_stress_information["beam_x"]
                self._greatest_shear_stress_information["train_x"] = train_x
            if abs(train_x_greatest_tensile_stress_information["sigma_t"]) > abs(self._greatest_tensile_stress_information["sigma_t"]):
                self._greatest_tensile_stress_information["sigma_t"] = train_x_greatest_tensile_stress_information["sigma_t"]
                self._greatest_tensile_stress_information["beam_x"] = train_x_greatest_tensile_stress_information["beam_x"]
                self._greatest_tensile_stress_information["train_x"] = train_x
            if abs(train_x_greatest_compressive_stress_information["sigma_c"]) > abs(self._greatest_compressive_stress_information["sigma_c"]):
                self._greatest_compressive_stress_information["sigma_c"] = train_x_greatest_compressive_stress_information["sigma_c"]
                self._greatest_compressive_stress_information["beam_x"] = train_x_greatest_compressive_stress_information["beam_x"]
                self._greatest_compressive_stress_information["train_x"] = train_x