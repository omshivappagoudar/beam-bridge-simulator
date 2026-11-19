from constants_and_conventions import *
from beam_properties import BeamProperties
from loading_cases import GenerateLoadingCases
from testing import *
from simulate_passage import PassageSimulation

# Generating all load cases to be tested
loading_case_generator = GenerateLoadingCases()

# Picking a specific load case
loading_case = loading_case_generator.loading_cases[0]

# Simulating a train passage
passage_simulation = PassageSimulation(loading_case)

# Getting V and M at a specific train location (train_x = 172) at a specific beam location (beam_x = 1028)
print(passage_simulation.get_frame_analysis(train_x = 172).get_shear_force(beam_x = 1028))
print(passage_simulation.get_frame_analysis(train_x = 172).get_bending_moment(beam_x = 1028))

# Getting the greatest V and M, in magnitude, along the beam at a specific train location (train_x = 172)
print(passage_simulation.get_frame_analysis(train_x = 172).get_greatest_shear_force_information())
print(passage_simulation.get_frame_analysis(train_x = 172).get_greatest_bending_moment_information())

# Getting the greatest V and M, in magnitude, throughout the entire train passage
print(passage_simulation.get_greatest_shear_force_information())
print(passage_simulation.get_greatest_bending_moment_information())

# Testing the code using test cases in testing.py
print("\n===== TESTING =====")
run_full_test_suite()
print()