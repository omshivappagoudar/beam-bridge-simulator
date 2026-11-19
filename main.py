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

    # Simulating and analyzing a train passage
    passage_simulation = PassageSimulation(loading_case = [67.5, 67.5, 67.5, 67.5, 91.0, 91.0])

if __name__ == "__main__":
    main()