from math import inf, isfinite, isclose, pi
from constants import *


class AnalyzePlateBuckling:
    def __init__(self, cross_section):
        self.cross_section = cross_section
        self.analyze()

    def analyze(self):
        section = self.cross_section
        E = MATBOARD_YOUNGS_MODULUS
        nu = MATBOARD_POISSON_RATIO
        I = section.moment_of_inertia

        if not isfinite(E) or E <= 0:
            raise ValueError("Young's modulus must be positive and finite.")

        if not isfinite(nu) or not -1 < nu < 0.5:
            raise ValueError("Invalid Poisson's ratio.")

        if not isfinite(I) or I <= 0:
            raise ValueError("Second moment of area must be positive.")

        section.plate_buckling_results = []
        section.plate_buckling_unchecked = []
        section.max_M_before_plate_buckling = inf
        section.plate_buckling_governing_piece = None

        for index, piece in enumerate(section.pieces):
            name = piece.get("name", f"piece_{index}")
            buckling = piece.get("buckling")

            if buckling is None:
                section.plate_buckling_unchecked.append(name)
                continue

            case = buckling["case"]

            if case not in PLATE_BUCKLING_COEFFICIENTS:
                raise ValueError(
                    f"{name}: unsupported buckling case {case!r}."
                )

            thickness = buckling["thickness"]
            width = buckling["unsupported_width"]

            if (
                not isfinite(thickness)
                or not isfinite(width)
                or thickness <= 0
                or width <= 0
            ):
                raise ValueError(
                    f"{name}: buckling dimensions must be positive "
                    "and finite."
                )

            # These two implemented cases are horizontal flange cases.
            # Reject vertical-web geometry rather than applying the
            # flange equation to it accidentally.
            if not isclose(
                thickness, piece["h"], rel_tol=1e-9, abs_tol=1e-9
            ):
                raise ValueError(
                    f"{name}: implemented flange cases require "
                    "buckling thickness to equal piece height."
                )

            top_y = piece["y"] + piece["h"] / 2
            bottom_y = piece["y"] - piece["h"] / 2
            c = top_y - section.centroid

            if c <= 0:
                section.plate_buckling_results.append({
                    "name": name,
                    "case": case,
                    "status": "not in compression",
                    "critical_stress": None,
                    "moment_capacity": inf,
                })
                continue

            if bottom_y < section.centroid:
                raise ValueError(
                    f"{name}: this piece crosses the neutral axis. "
                    "A suitable stress-gradient buckling case is needed."
                )

            k = PLATE_BUCKLING_COEFFICIENTS[case]

            critical_stress = (
                k * pi**2 * E
                / (12 * (1 - nu**2))
                * (thickness / width)**2
            )

            # Compare critical stress with the maximum compressive
            # bending stress in this flange region.
            moment_capacity = critical_stress * I / c

            section.plate_buckling_results.append({
                "name": name,
                "case": case,
                "status": "checked",
                "critical_stress": critical_stress,
                "moment_capacity": moment_capacity,
            })

            if moment_capacity < section.max_M_before_plate_buckling:
                section.max_M_before_plate_buckling = moment_capacity
                section.plate_buckling_governing_piece = name