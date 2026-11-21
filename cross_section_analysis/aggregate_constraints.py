from cross_section_analysis.constraint import *

class AggregateConstraints:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.aggregate_constraints()

    def aggregate_constraints(self):

        self.cross_section.constraints = {}

        self.cross_section.constraints[CONSTRAINT_AGAINST_TENSILE_RUPTURE] = Constraint(
            constraint_type = CONSTRAINT_AGAINST_TENSILE_RUPTURE,
            constrained_variable = CONSTRAINT_ON_M,
            start_beam_x = self.cross_section.start_beam_x,
            end_beam_x = self.cross_section.end_beam_x,
            maximum_value = self.cross_section.max_M_before_tensile_rupture
        )
        
        self.cross_section.constraints[CONSTRAINT_AGAINST_COMPRESSIVE_CRUSHING] = Constraint(
            constraint_type = CONSTRAINT_AGAINST_COMPRESSIVE_CRUSHING,
            constrained_variable = CONSTRAINT_ON_M,
            start_beam_x = self.cross_section.start_beam_x,
            end_beam_x = self.cross_section.end_beam_x,
            maximum_value = self.cross_section.max_M_before_compressive_crushing
        )
        
        self.cross_section.constraints[CONSTRAINT_AGAINST_MATBOARD_SHEAR_FAILURE] = Constraint(
            constraint_type = CONSTRAINT_AGAINST_MATBOARD_SHEAR_FAILURE,
            constrained_variable = CONSTRAINT_ON_V,
            start_beam_x = self.cross_section.start_beam_x,
            end_beam_x = self.cross_section.end_beam_x,
            maximum_value = self.cross_section.max_V_before_matboard_shear_failure
        )
        
        self.cross_section.constraints[CONSTRAINT_AGAINST_GLUE_SHEAR_FAILURE] = Constraint(
            constraint_type = CONSTRAINT_AGAINST_GLUE_SHEAR_FAILURE,
            constrained_variable = CONSTRAINT_ON_V,
            start_beam_x = self.cross_section.start_beam_x,
            end_beam_x = self.cross_section.end_beam_x,
            maximum_value = self.cross_section.max_V_before_glue_shear_failure
        )