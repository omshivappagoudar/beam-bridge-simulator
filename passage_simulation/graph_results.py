import matplotlib.pyplot as plt

from constants import *

class GraphResults:
    def __init__(self, passage_simulation):
        self.passage_simulation = passage_simulation
        self.graph_results()

    def graph_results(self):
        beam_x_coordinates = list(range(SUPPORT_SPAN + 1))

        fig, axes = plt.subplots(2, 4, figsize=(12, 8))

        # Tensile rupture
        axes[0, 0].plot(
            beam_x_coordinates,
            self.passage_simulation.tensile_rupture_FOS_diagram
        )
        axes[0, 0].set_xlabel("Location along the beam [mm]")
        axes[0, 0].set_ylabel("Factor of Safety Against Tensile Rupture")
        axes[0, 0].set_xlim(0, SUPPORT_SPAN)
        axes[0, 0].set_ylim(0, 5)
        axes[0, 0].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[0, 0].grid(True)

        # Compressive crushing
        axes[0, 1].plot(
            beam_x_coordinates,
            self.passage_simulation.compressive_crushing_FOS_diagram
        )
        axes[0, 1].set_xlabel("Location along the beam [mm]")
        axes[0, 1].set_ylabel("Factor of Safety Against Compressive Crushing")
        axes[0, 1].set_xlim(0, SUPPORT_SPAN)
        axes[0, 1].set_ylim(0, 5)
        axes[0, 1].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[0, 1].grid(True)

        # Matboard shear failure
        axes[0, 2].plot(
            beam_x_coordinates,
            self.passage_simulation.matboard_shear_failure_FOS_diagram
        )
        axes[0, 2].set_xlabel("Location along the beam [mm]")
        axes[0, 2].set_ylabel("Factor of Safety Against Matboard Shear Failure")
        axes[0, 2].set_xlim(0, SUPPORT_SPAN)
        axes[0, 2].set_ylim(0, 5)
        axes[0, 2].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[0, 2].grid(True)

        # Glue shear failure
        axes[0, 3].plot(
            beam_x_coordinates,
            self.passage_simulation.glue_shear_failure_FOS_diagram
        )
        axes[0, 3].set_xlabel("Location along the beam [mm]")
        axes[0, 3].set_ylabel("Factor of Safety Against Glue Shear Failure")
        axes[0, 3].set_xlim(0, SUPPORT_SPAN)
        axes[0, 3].set_ylim(0, 5)
        axes[0, 3].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[0, 3].grid(True)

        # Local Buckling Case 1
        axes[1, 0].plot(
            beam_x_coordinates,
            self.passage_simulation.local_buckling_case_1_FOS_diagram
        )
        axes[1, 0].set_xlabel("Location along the beam [mm]")
        axes[1, 0].set_ylabel("Factor of Safety Against Case 1 Local Buckling")
        axes[1, 0].set_xlim(0, SUPPORT_SPAN)
        axes[1, 0].set_ylim(0, 5)
        axes[1, 0].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[1, 0].grid(True)

        # Local Buckling Case 2
        axes[1, 1].plot(
            beam_x_coordinates,
            self.passage_simulation.local_buckling_case_2_FOS_diagram
        )
        axes[1, 1].set_xlabel("Location along the beam [mm]")
        axes[1, 1].set_ylabel("Factor of Safety Against Case 2 Local Buckling")
        axes[1, 1].set_xlim(0, SUPPORT_SPAN)
        axes[1, 1].set_ylim(0, 5)
        axes[1, 1].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[1, 1].grid(True)

        # Local Buckling Case 3
        axes[1, 2].plot(
            beam_x_coordinates,
            self.passage_simulation.local_buckling_case_3_FOS_diagram
        )
        axes[1, 2].set_xlabel("Location along the beam [mm]")
        axes[1, 2].set_ylabel("Factor of Safety Against Case 3 Local Buckling")
        axes[1, 2].set_xlim(0, SUPPORT_SPAN)
        axes[1, 2].set_ylim(0, 5)
        axes[1, 2].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[1, 2].grid(True)

        # Local Buckling Case 4
        axes[1, 3].plot(
            beam_x_coordinates,
            self.passage_simulation.local_buckling_case_4_FOS_diagram
        )
        axes[1, 3].set_xlabel("Location along the beam [mm]")
        axes[1, 3].set_ylabel("Factor of Safety Against Case 4 Local Buckling")
        axes[1, 3].set_xlim(0, SUPPORT_SPAN)
        axes[1, 3].set_ylim(0, 5)
        axes[1, 3].axhline(y=1, color="red", linestyle="--", label="FOS = 1")
        axes[1, 3].grid(True)

        plt.tight_layout()
        plt.show()