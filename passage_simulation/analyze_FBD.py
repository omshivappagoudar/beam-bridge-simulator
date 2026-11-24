from constants import *

class AnalyzeFBD:
    def __init__(self, loading_case, train_location):
        
        self.loading_case = loading_case
        self.train_location = train_location
        self.calculate_point_loads()
        self.calculate_reactions()
        self.calculate_FBD()
        self.calculate_shear_force_diagram()
        self.calculate_bending_moment_diagram()

    def get_shear_force(self, beam_x):
        return self.shear_force_diagram[beam_x]

    def get_bending_moment(self, beam_x):
        return self.bending_moment_diagram[beam_x]

    def calculate_point_loads(self):
        self._point_loads = []
        for wheel in range(6):
            point_load_location = self.train_location + TRAIN_POINT_LOAD_LOCATIONS[wheel]
            point_load_force = self.loading_case[wheel]
            if point_load_location >= 0.01 and point_load_location <= SUPPORT_SPAN - 0.01:
                self._point_loads.append({
                    "beam_x": point_load_location,
                    "P": -point_load_force
                })

    def calculate_reactions(self):
        point_moment_sum = 0.0
        point_load_sum = 0.0
        for point_load in self._point_loads:
            point_moment_sum += point_load["beam_x"] * point_load["P"]
            point_load_sum += point_load["P"]
        right_reaction_force_y = -point_moment_sum / SUPPORT_SPAN
        left_reaction_force_y = -point_load_sum - right_reaction_force_y
        self._left_reaction_force_y = left_reaction_force_y
        self._right_reaction_force_y = right_reaction_force_y

    def calculate_FBD(self):
        self.FBD = []
        self.FBD.append({"beam_x": 0, "P": self._left_reaction_force_y})
        for point_load in self._point_loads:
            self.FBD.append(point_load)
        self.FBD.append({"beam_x": SUPPORT_SPAN, "P": self._right_reaction_force_y})

    def calculate_shear_force_diagram(self):
        self.shear_force_diagram = [0] * (SUPPORT_SPAN + 1)
        running_shear_force = 0
        shear_force_index = 0
        for beam_x in range(0, 1201):
            if self.FBD[shear_force_index]["beam_x"] == beam_x:
                running_shear_force += self.FBD[shear_force_index]["P"]
                shear_force_index += 1
            self.shear_force_diagram[beam_x] = running_shear_force

    def calculate_bending_moment_diagram(self):
        self.bending_moment_diagram = [0]
        for beam_x in range(1, (SUPPORT_SPAN + 1)):
            self.bending_moment_diagram.append(self.bending_moment_diagram[-1] + self.shear_force_diagram[beam_x - 1])