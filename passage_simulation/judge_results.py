from math import isfinite


class JudgeResults:
    MODES = [
        ("Tensile rupture", "tensile_rupture"),
        ("Compressive crushing", "compressive_crushing"),
        ("Matboard shear", "matboard_shear_failure"),
        ("Glue shear", "glue_shear_failure"),
        ("Flange plate buckling", "plate_buckling"),
    ]

    def __init__(self, passage_simulation):
        self.passage_simulation = passage_simulation
        self.judge_results()

    def judge_results(self):
        simulation = self.passage_simulation

        simulation.tensile_rupture_failure = (
            simulation.tensile_rupture_FOS_information["FOS"] < 1
        )
        simulation.compressive_crushing_failure = (
            simulation.compressive_crushing_FOS_information["FOS"] < 1
        )
        simulation.matboard_shear_failure = (
            simulation.matboard_shear_failure_FOS_information["FOS"] < 1
        )
        simulation.glue_shear_failure = (
            simulation.glue_shear_failure_FOS_information["FOS"] < 1
        )
        simulation.plate_buckling_failure = (
            simulation.plate_buckling_FOS_information["FOS"] < 1
        )

        simulation.minimum_FOS = min(
            getattr(simulation, f"{attribute}_FOS_information")["FOS"]
            for _, attribute in self.MODES
        )

        simulation.bridge_failure = simulation.minimum_FOS < 1
        self.print_results()

    def FOS_color(self, FOS):
        if FOS < 1:
            return "\033[1;31m"  # Bold red
        return "\033[1;32m"      # Bold green

    def print_results(self):
        simulation = self.passage_simulation

        print(f"\n===== REPORT: TRIAL {simulation.trial_id} =====")
        print(
            "Axle loads:",
            ", ".join(f"{load:.2f} N" for load in simulation.loading_case),
        )
        print(f"Total train load: {sum(simulation.loading_case):.2f} N")

        for title, attribute in self.MODES:
            information = getattr(
                simulation, f"{attribute}_FOS_information"
            )
            FOS = information["FOS"]

            print(f"\n{title}")

            reset = "\033[0m"

            if isfinite(FOS):
                color = self.FOS_color(FOS)

                print(f"{color}Factor of safety: {FOS:.3f}{reset}")
                print(
                    f"{color}Critical bridge position: "
                    f"{information['beam_x']} mm{reset}"
                )
            else:
                print(
                    "\033[1;33m"
                    "No finite FOS for this loading/check."
                    "\033[0m"
                )
                print("See coverage notes below.")

        print("\nBUCKLING COVERAGE")
        print("Implemented: the two assigned flange compression cases.")
        print("Web compression buckling and shear buckling: NOT IMPLEMENTED.")

        for section in simulation.beam_bridge.cross_sections:
            unchecked = section.plate_buckling_unchecked
            if unchecked:
                print(
                    f"Section {section.cross_section_id}, "
                    f"unassigned pieces: {', '.join(unchecked)}"
                )

            for result in section.plate_buckling_results:
                if result["status"] == "not in compression":
                    print(
                        f"Section {section.cross_section_id}, "
                        f"{result['name']}: not compressed under "
                        "positive bending."
                    )
        
        reset = "\033[0m"
        color = self.FOS_color(simulation.minimum_FOS)

        print(
            f"\n{color}Minimum FOS of evaluated modes: "
            f"{simulation.minimum_FOS:.3f}{reset}"
        )

        if simulation.bridge_failure:
            print(
                f"{color}"
                "VERDICT: FAILURE PREDICTED IN AN EVALUATED MODE"
                f"{reset}"
            )
        else:
            print(
                f"{color}"
                "VERDICT: NO FAILURE PREDICTED IN EVALUATED MODES"
                f"{reset}"
            )

        print(
            "\033[1;33m"
            "This is not a complete assessment of all buckling modes."
            "\033[0m"
        )