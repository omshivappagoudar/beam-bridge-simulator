from constants_and_conventions import *

"""

DOCUMENTATION OF THE AnalyzeFBD CLASS.

===== CONSTRUCTOR INPUTS =====

loading_case = [P1, P2, P3, P4, P5, P6] is a list containing the six train-induced point loads, in Newtons.

train_location is a scalar, denoting the distance from the center of the left
support to the left-most point-load of the train, in millimeters.

===== CLASS OUTPUTS =====

self._point_loads = [
    {"beam_x": distance from left support, "P": point-load},
    {"beam_x": distance from left support, "P": point-load},
    {"beam_x": distance from left support, "P": point-load},
    ...
    {"beam_x": distance from left support, "P": point-load},
] 
(beam_x is in millimeters, P is in Newtons)
(Including point-loads from train wheels)
(NOT including reaction forces)
(Only includes 0 mm <= beam_x <= 1200 mm)

self._left_reaction_force_y         Left Reaction Force [N]
self._right_reaction_force_y        Right Reaction Force [N]

self._FBD = [
    {"beam_x": distance from left support, "P": point-load},
    {"beam_x": distance from left support, "P": point-load},
    {"beam_x": distance from left support, "P": point-load},
    ...
    {"beam_x": distance from left support, "P": point-load},
] 
(beam_x is in millimeters, P is in Newtons)
(Including point-loads from train wheels)
(Including the two reaction forces)
(Only includes 0 mm <= beam_x <= 1200 mm)

self._shear_force_diagram is a list of length 1201. If 0 <= beam_x <= 1200, then
self._shear_force_diagram[beam_x] returns the shear force, in N,
at beam_x millimeters to the right of the left support.

self._bending_moment_diagram is a list of length 1201. If 0 <= beam_x <= 1200, then
self._bending_moment_diagram[beam_x] returns the bending moment, in N * mm,
at beam_x millimeters to the right of the left support.

self._greatest_shear_force["beam_x"] returns the position of the greatest shear force (in magnitude) in units of [mm]
self._greatest_shear_force["V"] returns the signed value of the greatest shear force in units of [N]
self._greatest_bending_moment["beam_x"] returns the position of the greatest bending moment (in magnitude) in units of [mm]
self._greatest_shear_force["beam_x"] returns the signed value of the greatest bending moment in units of [N * mm]

"""

class AnalyzeFBD:
    def __init__(self, loading_case, train_location):
        
        self._loading_case = loading_case
        self._train_location = train_location
        self._calculate_point_loads()
        self._calculate_reactions()
        self._calculate_FBD()
        self._calculate_shear_force_diagram()
        self._calculate_bending_moment_diagram()
        self._calculate_extreme_values()

    def get_shear_force(self, beam_x):
        return self.shear_force_diagram[beam_x]

    def get_bending_moment(self, beam_x):
        return self.bending_moment_diagram[beam_x]

    def get_greatest_shear_force_information(self):
        return self._greatest_shear_force_information

    def get_greatest_bending_moment_information(self):
        return self._greatest_bending_moment_information

    def _calculate_point_loads(self):
        self._point_loads = []
        for wheel in range(6):
            point_load_location = self._train_location + TRAIN_POINT_LOAD_LOCATIONS[wheel]
            point_load_force = self._loading_case[wheel]
            if point_load_location >= 0 and point_load_location <= BRIDGE_LENGTH:
                self._point_loads.append({
                    "beam_x": point_load_location,
                    "P": point_load_force
                })

    def _calculate_reactions(self):
        point_moment_sum = 0.0
        point_load_sum = 0.0
        for point_load in self._point_loads:
            point_moment_sum += point_load["beam_x"] * point_load["P"]
            point_load_sum += point_load["P"]
        right_reaction_force_y = -point_moment_sum / BRIDGE_LENGTH
        left_reaction_force_y = -point_load_sum - right_reaction_force_y
        self._left_reaction_force_y = left_reaction_force_y
        self._right_reaction_force_y = right_reaction_force_y

    def _calculate_FBD(self):
        self.FBD = []
        self.FBD.append({"beam_x": 0, "P": self._left_reaction_force_y})
        for point_load in self._point_loads:
            self.FBD.append(point_load)
        self.FBD.append({"beam_x": BRIDGE_LENGTH, "P": self._right_reaction_force_y})

    def _calculate_shear_force_diagram(self):
        self.shear_force_diagram = [0] * (BRIDGE_LENGTH + 1)
        for force in self.FBD:
            for beam_x in range(force["beam_x"], (BRIDGE_LENGTH + 1)):
                self.shear_force_diagram[beam_x] += force["P"]

    def _calculate_bending_moment_diagram(self):
        self.bending_moment_diagram = [0]
        for beam_x in range(1, (BRIDGE_LENGTH + 1)):
            self.bending_moment_diagram.append(self.bending_moment_diagram[-1] + self.shear_force_diagram[beam_x - 1])

    def _calculate_extreme_values(self):
        self._greatest_shear_force_information = {"V": 0, "beam_x": 0}
        self._greatest_bending_moment_information = {"M": 0, "beam_x": 0}
        for beam_x in range(0, 1201):
            shear = self.get_shear_force(beam_x)
            bending_moment = self.get_bending_moment(beam_x)
            if abs(shear) > abs(self._greatest_shear_force_information["V"]):
                self._greatest_shear_force_information["V"] = shear
                self._greatest_shear_force_information["beam_x"] = beam_x
            if abs(bending_moment) > abs(self._greatest_bending_moment_information["M"]):
                self._greatest_bending_moment_information["M"] = bending_moment
                self._greatest_bending_moment_information["beam_x"] = beam_x