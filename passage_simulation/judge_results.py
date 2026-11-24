class JudgeResults:
    def __init__(self, passage_simulation):
        self.passage_simulation = passage_simulation
        self.judge_results()

    def judge_results(self):
        self.judge_tensile_rupture_FOS()
        self.judge_compressive_crushing_FOS()
        self.judge_matboard_shear_failure_FOS()
        self.judge_glue_shear_failure_FOS()
        self.judge_local_buckling_case_1_FOS()
        self.judge_local_buckling_case_2_FOS()
        self.judge_local_buckling_case_3_FOS()
        self.judge_local_buckling_case_4_FOS()
        self.determine_minimum_FOS()
        self.determine_failure()
        self.print_results()

    def judge_tensile_rupture_FOS(self):
        FOS = self.passage_simulation.tensile_rupture_FOS_information["FOS"]
        self.passage_simulation.tensile_rupture_failure = (FOS < 1)

    def judge_compressive_crushing_FOS(self):
        FOS = self.passage_simulation.compressive_crushing_FOS_information["FOS"]
        self.passage_simulation.compressive_crushing_failure = (FOS < 1)

    def judge_matboard_shear_failure_FOS(self):
        FOS = self.passage_simulation.matboard_shear_failure_FOS_information["FOS"]
        self.passage_simulation.matboard_shear_failure = (FOS < 1)

    def judge_glue_shear_failure_FOS(self):
        FOS = self.passage_simulation.glue_shear_failure_FOS_information["FOS"]
        self.passage_simulation.glue_shear_failure = (FOS < 1)

    def judge_local_buckling_case_1_FOS(self):
        FOS = self.passage_simulation.local_buckling_case_1_FOS_information["FOS"]
        self.passage_simulation.local_buckling_case_1 = (FOS < 1)

    def judge_local_buckling_case_2_FOS(self):
        FOS = self.passage_simulation.local_buckling_case_2_FOS_information["FOS"]
        self.passage_simulation.local_buckling_case_2 = (FOS < 1)

    def judge_local_buckling_case_3_FOS(self):
        FOS = self.passage_simulation.local_buckling_case_3_FOS_information["FOS"]
        self.passage_simulation.local_buckling_case_3 = (FOS < 1)

    def judge_local_buckling_case_4_FOS(self):
        FOS = self.passage_simulation.local_buckling_case_4_FOS_information["FOS"]
        self.passage_simulation.local_buckling_case_4 = (FOS < 1)

    def determine_minimum_FOS(self):
        self.passage_simulation.minimum_FOS = min([
            self.passage_simulation.tensile_rupture_FOS_information["FOS"],
            self.passage_simulation.compressive_crushing_FOS_information["FOS"],
            self.passage_simulation.matboard_shear_failure_FOS_information["FOS"],
            self.passage_simulation.glue_shear_failure_FOS_information["FOS"],
            self.passage_simulation.local_buckling_case_1_FOS_information["FOS"],
            self.passage_simulation.local_buckling_case_2_FOS_information["FOS"],
            self.passage_simulation.local_buckling_case_3_FOS_information["FOS"],
            self.passage_simulation.local_buckling_case_4_FOS_information["FOS"],
        ])

    def determine_failure(self):
        self.passage_simulation.bridge_failure = (self.passage_simulation.minimum_FOS < 1)
    
    def FOS_color(self, FOS):
        if FOS < 1:
            return "\033[1;31m"
        else:
            return "\033[1;32m"
    
    def print_results(self):
        print(f"\n\n===== REPORT: TRIAL {self.passage_simulation.trial_id} =====\n")

        print("MATERIAL USAGE.")
        weight = self.passage_simulation.beam_bridge.weight
        area = self.passage_simulation.beam_bridge.volume / 1.27
        print(f"Matboard Area Used: {area:.2f} mm^2 out of 826008.00 mm^2 ({area / 826008 * 100:.2f}%)")
        print(f"Total Bridge Weight: {weight:.2f} N")
        print()

        print("LOADING CASE TESTED.")
        print(f"Left Cart Weight: {self.passage_simulation.loading_case[0] + self.passage_simulation.loading_case[1]:.2f} N")
        print(f"Center Cart Weight: {self.passage_simulation.loading_case[2] + self.passage_simulation.loading_case[3]:.2f} N")
        print(f"Right Cart Weight: {self.passage_simulation.loading_case[4] + self.passage_simulation.loading_case[5]:.2f} N")
        print()

        FOS_info = self.passage_simulation.tensile_rupture_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("I. Analysis of Tensile Rupture")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.compressive_crushing_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("II. Analysis of Compressive Crushing")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.matboard_shear_failure_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("III. Analysis of Matboard Shear Failure")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.glue_shear_failure_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("IV. Analysis of Glue Shear Failure")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.local_buckling_case_1_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("V. Analysis of Case 1 Local Buckling")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.local_buckling_case_2_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("VI. Analysis of Case 2 Local Buckling")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.local_buckling_case_3_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("VII. Analysis of Case 3 Local Buckling")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        FOS_info = self.passage_simulation.local_buckling_case_4_FOS_information
        color = self.FOS_color(FOS_info["FOS"])
        print("VIII. Analysis of Case 4 Local Buckling")
        print(f"{color}Factor of Safety: {FOS_info["FOS"]:.2f}\033[0m")
        print(f"{color}Beam Location with Lowest Factor of Safety: {FOS_info["beam_x"]:.2f} mm\033[0m")
        print()

        if self.passage_simulation.bridge_failure:
            print("\033[1;31mVERDICT: BRIDGE FAILURE\033[0m")
            print("\n===== FINAL RESULT =====")
            print(f"Failure Loading: [{self.passage_simulation.loading_case[0]:.2f} N, {self.passage_simulation.loading_case[1]:.2f} N, {self.passage_simulation.loading_case[2]:.2f} N, {self.passage_simulation.loading_case[3]:.2f} N, {self.passage_simulation.loading_case[4]:.2f} N, {self.passage_simulation.loading_case[5]:.2f} N]")
            failure_load = 0
            for point_load in self.passage_simulation.loading_case:
                failure_load += point_load
            print(f"Total Load: {failure_load:.2f} N")
            print(f"Strength to Weight Ratio: {failure_load / weight:.2f}")
        else:
            print("\033[1;32mVERDICT: NO BRIDGE FAILURE\033[0m")
            print("\n===== FINAL RESULT =====")
            print(f"Successful Loading: [{self.passage_simulation.loading_case[0]:.2f} N, {self.passage_simulation.loading_case[1]:.2f} N, {self.passage_simulation.loading_case[2]:.2f} N, {self.passage_simulation.loading_case[3]:.2f} N, {self.passage_simulation.loading_case[4]:.2f} N, {self.passage_simulation.loading_case[5]:.2f} N]")
            successful_load = 0
            for point_load in self.passage_simulation.loading_case:
                successful_load += point_load
            print(f"Total Load: {successful_load:.2f} N")
        print()