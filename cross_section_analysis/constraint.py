CONSTRAINT_AGAINST_TENSILE_RUPTURE = 0
CONSTRAINT_AGAINST_COMPRESSIVE_CRUSHING = 1
CONSTRAINT_AGAINST_MATBOARD_SHEAR_FAILURE = 2
CONSTRAINT_AGAINST_GLUE_SHEAR_FAILURE = 3

CONSTRAINT_ON_V = 0
CONSTRAINT_ON_M = 1

class Constraint:
    def __init__(self, constraint_type, constrained_variable, start_beam_x, end_beam_x, maximum_value):
        self.constraint_type = constraint_type
        self.constrained_variable = constrained_variable
        self.start_beam_x = start_beam_x
        self.end_beam_x = end_beam_x
        self.maximum_value = maximum_value