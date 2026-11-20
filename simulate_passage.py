from analyze_FBD import *
from constants import *
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

    def __init__(self, loading_case, trial_number, start_train_x = -TRAIN_LENGTH, end_train_x = SUPPORT_SPAN):
        self._loading_case = loading_case
        self._trial_number = trial_number
        self._start_train_x = start_train_x
        self._end_train_x = end_train_x
        self._analyze_passage()
        self._calculate_extreme_values()
        self._package_FOS()
        self.report_analysis()

    def report_analysis(self):
        print(f"\n\n\033[1m===== REPORT: TRIAL {self._trial_number} =====\033[0m")
        print()
        self._print_loading_case()
        print()
        self._print_cross_section_analysis()
        print()
        self._print_maximum_stresses()

    def get_frame_analysis(self, train_x):
        return self.passage_analysis[train_x]

    def get_greatest_shear_force_information(self):
        return self._greatest_shear_force_information

    def get_greatest_bending_moment_information(self):
        return self._greatest_bending_moment_information

    def get_greatest_shear_stress_information(self):
        return self._greatest_shear_stress_information

    def get_greatest_tensile_stress_information(self):
        return self._greatest_tensile_stress_information

    def get_greatest_compressive_stress_information(self):
        return self._greatest_compressive_stress_information

    def _analyze_passage(self):
        self.passage_analysis = {}
        whole_start = time.time()
        for train_x in range(self._start_train_x, self._end_train_x):
            self.passage_analysis[train_x] = AnalyzeFBD(self._loading_case, train_x)

            percentage = (train_x - (-TRAIN_LENGTH)) / (SUPPORT_SPAN - (-TRAIN_LENGTH)) * 100
            # if train_x % 100 == 0: print(f"Analysis is {percentage:.2f}% complete.")
        whole_end = time.time()
        # print(f"Finished analyzing the passage from train_x = {self._start_train_x} mm to train_x = {self._end_train_x} mm. Total computation time: {whole_end - whole_start:.2f} seconds.")

    def _calculate_extreme_values(self):
        self._greatest_shear_force_information = {"V": 0, "beam_x": 0, "train_x": 0}
        self._greatest_bending_moment_information = {"M": 0, "beam_x": 0, "train_x": 0}
        self._greatest_shear_stress_information = {"tau_xy": 0, "beam_x": 0, "train_x": 0, "FOS": 0}
        self._greatest_tensile_stress_information = {"sigma_t": 0, "beam_x": 0, "train_x": 0, "FOS": 0}
        self._greatest_compressive_stress_information = {"sigma_c": 0, "beam_x": 0, "train_x": 0, "FOS": 0}
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
        self._greatest_shear_stress_information["FOS"] = abs(MATBOARD_SHEAR_FAILURE_STRESS / self._greatest_shear_stress_information["tau_xy"])
        self._greatest_tensile_stress_information["FOS"] = abs(MATBOARD_TENSILE_FAILURE_STRESS / self._greatest_tensile_stress_information["sigma_t"])
        self._greatest_compressive_stress_information["FOS"] = abs(MATBOARD_COMPRESSIVE_FAILURE_STRESS / self._greatest_compressive_stress_information["sigma_c"])

    def _print_loading_case(self):
        print("LOADING CASE TESTED.")
        print(f"Left Cart Weight: {self._loading_case[0] + self._loading_case[1]:.2f} N")
        print(f"Center Cart Weight: {self._loading_case[2] + self._loading_case[3]:.2f} N")
        print(f"Right Cart Weight: {self._loading_case[4] + self._loading_case[5]:.2f} N")

    def _print_cross_section_analysis(self):
        print("CROSS SECTION ANALYSIS.")
        print(f"Cross-sectional Area: {cross_section.area:.2f} mm^2")
        print(f"Cross-sectional Centroid: {cross_section.centroid:.2f} mm from the bottom")
        print(f"Cross-sectional Moment of Inertia: {cross_section.moment_of_inertia:.2f} mm^4")

    def _FOS_color(self, FOS):
        if FOS < 1:
            return "\033[1;31m"
        else:
            return "\033[1;32m"

    def _print_maximum_stresses(self):
        print("TENSILE STRESS ANALYSIS.")
        print(f"Maximum Tensile Stress During Train Passage: {self._greatest_tensile_stress_information["sigma_t"]:.2f} MPa")
        print(f"Train Location Inducing Maximum Tensile Stress: Left-most wheel {self._greatest_tensile_stress_information["train_x"]:.2f} mm from the center of the left support")
        print(f"Beam Location Experiencing Maximum Tensile Stress: {self._greatest_tensile_stress_information["beam_x"]:.2f} mm from the center of the left support")
        print(f"{self._FOS_color(self.FOS["tensile"])}Factor of Safety Against Tensile Rupture Failure: {self.FOS["tensile"]:.2f}\033[0m")
        print()
        print("COMPRESSIVE STRESS ANALYSIS.")
        print(f"Maximum Compressive Stress During Train Passage: {self._greatest_compressive_stress_information["sigma_c"]:.2f} MPa")
        print(f"Train Location Inducing Maximum Compressive Stress: Left-most wheel {self._greatest_compressive_stress_information["train_x"]:.2f} mm from the center of the left support")
        print(f"Beam Location Experiencing Maximum Compressive Stress: {self._greatest_compressive_stress_information["beam_x"]:.2f} mm from the center of the left support")
        print(f"{self._FOS_color(self.FOS["compressive"])}Factor of Safety Against Compressive Crushing Failure: {self.FOS["compressive"]:.2f}\033[0m")
        print()
        print("SHEAR STRESS ANALYSIS.")
        print(f"Maximum Shear Stress During Train Passage: {self._greatest_shear_stress_information["tau_xy"]:.4f} MPa")
        print(f"Train Location Inducing Maximum Shear Stress: Left-most wheel {self._greatest_shear_stress_information["train_x"]:.2f} mm from the center of the left support")
        print(f"Beam Location Experiencing Maximum Shear Stress: {self._greatest_shear_stress_information["beam_x"]:.2f} mm from the center of the left support")
        print(f"Cross-sectional Beam Elevation Experiencing Maximum Shear Stress: {cross_section._shear_weakest_y:.2f} mm from the bottom")
        print(f"{self._FOS_color(self.FOS["shear"])}Factor of Safety Against Shear Failure: {self.FOS["shear"]:.2f}, assuming failure at {MATBOARD_SHEAR_FAILURE_STRESS} MPa\033[0m")
        print()

    def _package_FOS(self):
        self.FOS = {
            "tensile": self._greatest_tensile_stress_information["FOS"],
            "compressive": self._greatest_compressive_stress_information["FOS"],
            "shear": self._greatest_shear_stress_information["FOS"]
        }