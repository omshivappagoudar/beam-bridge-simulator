"""

===== TO-DO LIST =====

1. Test the shear stress calculations for tau_xy in beam_properties.py
2. Implement a way to save computations into a file
3. Implement Factors of Safety calculations
4. Look into the calculation of the Shear Force Diagram; it could be sped up with a difference array approach.

===== NOTES =====
Full analysis of passage took 5 minutes, 7 seconds.

"""


from constants_and_conventions import *
from beam_properties import CrossSectionAnalysis
from loading_cases import GenerateLoadingCases
from testing import *
from simulate_passage import PassageSimulation
from initialization import *

"""
Refer to documentation.py for instructions on utilizing this library.
"""

def main():

    # Generating all load cases to be tested
    loading_case_generator = GenerateLoadingCases()

    # Picking a specific load case
    loading_case = loading_case_generator.loading_cases[0]

    # Simulating a train passage between only a start and end location
    # passage_simulation = PassageSimulation(loading_case, start_train_x = 165, end_train_x = 175)
    
    # Simulating an entire train passage (This takes about 5 minutes to complete)
    passage_simulation = PassageSimulation(loading_case)

if __name__ == "__main__":
    main()