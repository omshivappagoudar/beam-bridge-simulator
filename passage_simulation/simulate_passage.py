from passage_simulation.analyze_FBD import *
from passage_simulation.calculate_FOS_diagrams import *
from passage_simulation.calculate_FOS import *
from passage_simulation.judge_results import *
from passage_simulation.graph_results import *
from constants import *

class PassageSimulation:

    def __init__(self, beam_bridge, loading_case, trial_id, start_train_x = -TRAIN_LENGTH, end_train_x = SUPPORT_SPAN):
        self.beam_bridge = beam_bridge
        self.loading_case = loading_case
        self.trial_id = trial_id
        self.start_train_x = start_train_x
        self.end_train_x = end_train_x

        self.analyze_passage()
        self.calculate_extreme_values()

        CalculateFactorOfSafetyDiagrams(self)
        CalculateFactorsOfSafety(self)
        JudgeResults(self)

        if self.bridge_failure:
            GraphResults(self)

    def get_frame_analysis(self, train_x):
        return self.passage_analysis[train_x]

    def analyze_passage(self):
        self.passage_analysis = {}
        for train_x in range(self.start_train_x, self.end_train_x):
            self.passage_analysis[train_x] = AnalyzeFBD(self.loading_case, train_x)

    def calculate_extreme_values(self):
        self.maximum_shear_force_diagram = [0] * (SUPPORT_SPAN + 1)
        self.maximum_bending_moment_diagram = [0] * (SUPPORT_SPAN + 1)
        for train_x in range(self.start_train_x, self.end_train_x):
            passage_analysis = self.passage_analysis[train_x]
            train_x_shear_force_diagram = passage_analysis.shear_force_diagram
            train_x_bending_moment_diagram = passage_analysis.bending_moment_diagram
            for beam_x in range(0, SUPPORT_SPAN + 1):
                self.maximum_shear_force_diagram[beam_x] = max(self.maximum_shear_force_diagram[beam_x], abs(train_x_shear_force_diagram[beam_x]))
                self.maximum_bending_moment_diagram[beam_x] = max(self.maximum_bending_moment_diagram[beam_x], abs(train_x_bending_moment_diagram[beam_x]))