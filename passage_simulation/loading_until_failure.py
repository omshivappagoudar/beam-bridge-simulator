from passage_simulation.loading_cases import GenerateLoadingCases
from passage_simulation.simulate_passage import PassageSimulation

class LoadUntilFailure:
    def __init__(self, beam_bridge):
        self.beam_bridge = beam_bridge
        self.load_until_failure()

    def load_until_failure(self):
        load_case_generator = GenerateLoadingCases()

        # Loading Case 1
        current_loading_case = load_case_generator.loading_cases[0]
        passage_simulation = PassageSimulation(
            beam_bridge = self.beam_bridge,
            loading_case = current_loading_case,
            trial_id = 1
        )
        if passage_simulation.bridge_failure:
            return

        # Loading Case 2 (Base Case)
        current_loading_case = load_case_generator.loading_cases[1]
        passage_simulation = PassageSimulation(
            beam_bridge = self.beam_bridge,
            loading_case = current_loading_case,
            trial_id = 2
        )
        if passage_simulation.bridge_failure:
            return

        # Loading Case 2 (Progressive Base Case)
        current_loading_case = load_case_generator.loading_cases[2]
        passage_simulation = PassageSimulation(
            beam_bridge = self.beam_bridge,
            loading_case = current_loading_case,
            trial_id = 3
        )
        if passage_simulation.bridge_failure:
            return

        # Failure Loading Case
        current_loading_case = load_case_generator.generate_failure_loading_case(passage_simulation)
        passage_simulation = PassageSimulation(
            beam_bridge = self.beam_bridge,
            loading_case = current_loading_case,
            trial_id = 4
        )
        if passage_simulation.bridge_failure:
            return