from constants import *

class GenerateLoadingCases:
    def __init__(self):
        self.loading_cases = []
        self._generate_loading_cases()

    def _generate_loading_cases(self):

        # Loading Case 1
        P = 400.0 / 6
        self.loading_cases.append([P, P, P, P, P, P])

        # Load Case 2 (Base Case)
        P = 135.0 / 2
        self.loading_cases.append([P, P, P, P, P * 1.35, P * 1.35])

        # Load Case 2 (Progressive)
        base_P = 135.0 / 2
        for P in range(int(base_P), int(50 * base_P), int(0.1 * base_P)):
            self.loading_cases.append([P * 1.10, P * 1.10, P, P, P * 1.35, P * 1.35])

    def calculate_total_load(self, loading_case):
        total = 0
        for load in loading_case:
            total += load
        return total