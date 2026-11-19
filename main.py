"""

===== TO-DO LIST =====
1. Estimate total volume and matboard utilization percentage
2. Implement buckling checking

"""

from constants import *
from beam_properties import CrossSectionAnalysis
from loading_cases import GenerateLoadingCases
from testing import *
from simulate_passage import PassageSimulation
from initialization import *

"""
Refer to documentation.py for instructions on utilizing this library.
"""

def main():

    # Generate Load Cases
    load_case_generator = GenerateLoadingCases()

    # Simulating and analyzing a train passage
    for trial in range(len(load_case_generator.loading_cases)):
        current_loading_case = load_case_generator.loading_cases[trial]
        passage_simulation = PassageSimulation(loading_case = current_loading_case, trial_number = trial + 1)
        FOS_tensile = passage_simulation.FOS["tensile"]
        FOS_compressive = passage_simulation.FOS["compressive"]
        FOS_shear = passage_simulation.FOS["shear"]

        failure = False
        if FOS_tensile < 1:
            print("\033[31mTENSILE FAILURE!\033[0m")
            failure = True
        if FOS_compressive < 1:
            print("\033[31mCOMPRESSIVE FAILURE!\033[0m")
            failure = True
        if FOS_shear < 1:
            print("\033[31mSHEAR FAILURE!\033[0m")
            failure = True

        if failure:
            break
        else:
            print("\033[32mNO FAILURE!\033[0m")

if __name__ == "__main__":
    main()