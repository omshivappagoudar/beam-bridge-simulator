from constants import *
from cross_section_analysis import CrossSectionAnalysis
from loading_cases import GenerateLoadingCases
from simulate_passage import PassageSimulation
from cross_section_design import *

def load_until_failure():
    # Generate Load Cases
    load_case_generator = GenerateLoadingCases()

    # Simulating and analyzing a train passage
    for trial in range(len(load_case_generator.loading_cases)):
        current_loading_case = load_case_generator.loading_cases[trial]
        passage_simulation = PassageSimulation(loading_case = current_loading_case, trial_number = trial + 1)
        FOS_tensile = passage_simulation.FOS["tensile"]
        FOS_compressive = passage_simulation.FOS["compressive"]
        FOS_shear = passage_simulation.FOS["shear"]

        if FOS_tensile < 1:
            print("\n\n===== FINAL RESULT =====")
            print("Failure Mode: Tensile Rupture")
            print(f"Failure Loading: [{current_loading_case[0]:.2f} N, {current_loading_case[1]:.2f} N, {current_loading_case[2]:.2f} N, {current_loading_case[3]:.2f} N, {current_loading_case[4]:.2f} N, {current_loading_case[5]:.2f} N]")
            failure_load = load_case_generator.calculate_total_load(current_loading_case)
            print(f"Total Load: {failure_load:.2f} N")
            print(f"Strength to Weight Ratio: {failure_load / cross_section.get_weight():.2f}")
            break
        if FOS_compressive < 1:
            print("\n\n===== FINAL RESULT =====")
            print("Failure Mode: Compressive Crushing")
            print(f"Failure Loading: [{current_loading_case[0]:.2f} N, {current_loading_case[1]:.2f} N, {current_loading_case[2]:.2f} N, {current_loading_case[3]:.2f} N, {current_loading_case[4]:.2f} N, {current_loading_case[5]:.2f} N]")
            failure_load = load_case_generator.calculate_total_load(current_loading_case)
            print(f"Total Load: {failure_load:.2f} N")
            print(f"Strength to Weight Ratio: {failure_load / cross_section.get_weight():.2f}")
            break
        if FOS_shear < 1:
            print("\n\n===== FINAL RESULT =====")
            print("Failure Mode: Shear Failure")
            print(f"Failure Loading: [{current_loading_case[0]:.2f} N, {current_loading_case[1]:.2f} N, {current_loading_case[2]:.2f} N, {current_loading_case[3]:.2f} N, {current_loading_case[4]:.2f} N, {current_loading_case[5]:.2f} N]")
            failure_load = load_case_generator.calculate_total_load(current_loading_case)
            print(f"Total Load: {failure_load:.2f} N")
            print(f"Strength to Weight Ratio: {failure_load / cross_section.get_weight():.2f}")
            break
        else:
            print("\033[32mNo failure.\033[0m")