from analyze_FBD import *

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

===== CLASS OUTPUTS =====

(To-do)

"""

class PassageSimulation:

    def __init__(self, train_loads):
        self._train_loads = train_loads