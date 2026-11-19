from main import BRIDGE_LENGTH

"""

DOCUMENTATION OF THE AnalyzeFBD CLASS.

===== CONSTRUCTOR INPUTS =====

train_loads = [
    {"x": distance from left-most wheel, "P": point-load},     # B1
    {"x": distance from left-most wheel, "P": point-load},     # B2
    {"x": distance from left-most wheel, "P": point-load},     # B3
    {"x": distance from left-most wheel, "P": point-load},     # B4
    {"x": distance from left-most wheel, "P": point-load},     # B5
    {"x": distance from left-most wheel, "P": point-load}      # B6
]

train_location is a scalar, denoting the distance from the center of the left
support to the left-most point-load of the train, in millimeters.

===== CLASS OUTPUTS =====

self._point_loads = [
    {"x": distance from left support, "P": point-load},
    {"x": distance from left support, "P": point-load},
    {"x": distance from left support, "P": point-load},
    ...
    {"x": distance from left support, "P": point-load},
] 
(In Newtons)
(Including point-loads from train wheels)
(NOT including reaction forces)
(Only includes 0 mm <= x <= 1200 mm)

self._left_reaction_force_y         Left Reaction Force [N]
self._right_reaction_force_y        Right Reaction Force [N]

self._FBD = [
    {"x": distance from left support, "P": point-load},
    {"x": distance from left support, "P": point-load},
    {"x": distance from left support, "P": point-load},
    ...
    {"x": distance from left support, "P": point-load},
] 
(In Newtons)
(Including point-loads from train wheels)
(Including the two reaction forces)
(Only includes 0 mm <= x <= 1200 mm)

self._shear_force_diagram is a list of length 1201. If 0 <= x <= 1200, then
self._shear_force_diagram[x] returns the shear force, in N,
at x millimeters to the right of the left support.

self._bending_moment_diagram is a list of length 1201. If 0 <= x <= 1200, then
self._bending_moment_diagram[x] returns the bending moment, in N * mm,
at x millimeters to the right of the left support.

"""

class AnalyzeFBD:
    def __init__(self, train_loads, train_location):
        
        self._train_loads = train_loads
        self._train_location = train_location
        self._calculate_point_loads()
        self._calculate_reactions()
        self._calculate_FBD()
        self._calculate_shear_force_diagram()
        self._calculate_bending_moment_diagram()

    def _calculate_point_loads(self):
        loads = []
        for point_load in self._train_loads:
            x = point_load["x"] + self._train_location
            if x >= 0 and x <= 1200:
                loads.append({
                    "x": point_load["x"] + self._train_location,
                    "P": point_load["P"]
                })
        self._point_loads = loads

    def _calculate_reactions(self):
        point_moment_sum = 0.0
        point_load_sum = 0.0
        for point_load in self._point_loads:
            point_moment_sum += point_load["x"] * point_load["P"]
            point_load_sum += point_load["P"]
        right_reaction_force_y = -point_moment_sum / BRIDGE_LENGTH
        left_reaction_force_y = -point_load_sum - right_reaction_force_y
        self._left_reaction_force_y = left_reaction_force_y
        self._right_reaction_force_y = right_reaction_force_y

    def _calculate_FBD(self):
        self._FBD = []
        self._FBD.append({"x": 0, "P": self._left_reaction_force_y})
        for point_load in self._point_loads:
            self._FBD.append(point_load)
        self._FBD.append({"x": 1200, "P": self._right_reaction_force_y})

    def _calculate_shear_force_diagram(self):
        self._shear_force_diagram = [0] * 1201
        for force in self._FBD:
            for x in range(force["x"], 1201):
                self._shear_force_diagram[x] += force["P"]

    def _calculate_bending_moment_diagram(self):
        self._bending_moment_diagram = [0]
        for x in range(1, 1201):
            self._bending_moment_diagram.append(self._bending_moment_diagram[-1] + self._shear_force_diagram[x - 1])