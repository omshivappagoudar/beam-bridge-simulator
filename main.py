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

    # Simulating and analyzing a train passage
    passage_simulation = PassageSimulation(loading_case = [-67.5, -67.5, -67.5, -67.5, -91.0, -91.0])

if __name__ == "__main__":
    main()