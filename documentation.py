from constants import *
from cross_section_analysis import CrossSectionAnalysis
from loading_cases import GenerateLoadingCases
from simulate_passage import PassageSimulation

# Generating all load cases to be tested
loading_case_generator = GenerateLoadingCases()

# Picking a specific load case
loading_case = loading_case_generator.loading_cases[0]

# Simulating a train passage between only a start and end location
passage_simulation = PassageSimulation(loading_case, start_train_x = 165, end_train_x = 175)

# Simulating an entire train passage
# passage_simulation = PassageSimulation(loading_case)

print("\n===== OUTPUTS =====")

# ===== RETRIEVING A VALUE AT A SPECIFIC TRAIN LOCATION AND SPECIFIC BEAM LOCATION =====

# Getting V at a specific train location (train_x = 172) at a specific beam location (beam_x = 1028)
print("1. train_x = 172, beam_x = 1028 => V(beam_x):", passage_simulation.get_frame_analysis(train_x = 172).get_shear_force(beam_x = 1028))

# Getting M at a specific train location (train_x = 172) at a specific beam location (beam_x = 1028)
print("2. train_x = 172, beam_x = 1028 => M(beam_x):", passage_simulation.get_frame_analysis(train_x = 172).get_bending_moment(beam_x = 1028))

# Getting the maximum tau_xy, in magnitude, over the depth of the cross-section at a specific
# train location (train_x = 172), at a specific beam location (beam_x = 1028)
print("3. train_x = 172, beam_x = 1028 => tau_xy_max(beam_x):", passage_simulation.get_frame_analysis(train_x = 172).get_maximum_shear_stress_at_beam_x(beam_x = 1028))

# Getting the maximum tensile stress, in magnitude, over the depth of the cross-section at a specific
# train location (train_x = 172), at a specific beam location (beam_x = 1028)
print("4. train_x = 172, beam_x = 1028 => sigma_tensile_max(beam_x):", passage_simulation.get_frame_analysis(train_x = 172).get_maximum_tensile_stress_at_beam_x(beam_x = 1028))

# Getting the maximum compressive stress, in magnitude, over the depth of the cross-section at a specific
# train location (train_x = 172), at a specific beam location (beam_x = 1028)
print("5. train_x = 172, beam_x = 1028 => sigma_compressive_max(beam_x):", passage_simulation.get_frame_analysis(train_x = 172).get_maximum_compressive_stress_at_beam_x(beam_x = 1028))


# ===== SPECIFIC TRAIN LOCATION, RETRIEVING A MAXIMUM VALUE OVER THE ENTIRE BEAM =====

# Getting the greatest V, in magnitude, along the entire beam at a specific train location (train_x = 172)
print("6. train_x = 172 => V_max:", passage_simulation.get_frame_analysis(train_x = 172).get_greatest_shear_force_information())

# Getting the greatest M, in magnitude, along the entire beam at a specific train location (train_x = 172)
print("7. train_x = 172 => M_max:", passage_simulation.get_frame_analysis(train_x = 172).get_greatest_bending_moment_information())

# Getting the maximum tau_xy, in magnitude, over the depth of the cross-section, along the entire beam
# at a specific train location (train_x = 172)
print("8. train_x = 172 => tau_xy_max:", passage_simulation.get_frame_analysis(train_x = 172).get_greatest_shear_stress_information())

# Getting the maximum tensile stress, in magnitude, over the depth of the cross-section, along the entire beam
# at a specific train location (train_x = 172)
print("9. train_x = 172 => sigma_tensile_max:", passage_simulation.get_frame_analysis(train_x = 172).get_greatest_tensile_stress_information())

# Getting the maximum compressive stress, in magnitude, over the depth of the cross-section, along the entire beam
# at a specific train location (train_x = 172)
print("10. train_x = 172 => sigma_compressive_max:", passage_simulation.get_frame_analysis(train_x = 172).get_greatest_compressive_stress_information())


# ===== RETRIEVING A MAXIMUM VALUE OVER THE ENTIRE TRAIN PASSAGE =====

# Getting the greatest V, in magnitude, throughout the entire train passage
print("11. Greatest Shear Force V During Train Passage:", passage_simulation.get_greatest_shear_force_information())

# Getting the greatest M, in magnitude, throughout the entire train passage
print("12. Greatest Bending moment M During Train Passage:", passage_simulation.get_greatest_bending_moment_information())

# Getting the greatest tau_xy, in magnitude, throughout the entire train passage
print("13. Greatest Shear Stress tau_xy During Train Passage:", passage_simulation.get_greatest_shear_stress_information())

# Getting the greatest tensile stress, in magnitude, throughout the entire train passage
print("14. Greatest Tensile Stress sigma_t During Train Passage:", passage_simulation.get_greatest_tensile_stress_information())

# Getting the greatest compressive stress, in magnitude, throughout the entire train passage
print("15. Greatest Compressive Stress sigma_c During Train Passage:", passage_simulation.get_greatest_compressive_stress_information())