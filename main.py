"""

===== COMPLETED =====
1. Tensile Rupture FOS Computation (1 Failure Mode)
2. Compressive Crushing FOS Computation (1 Failure Mode)
3. Matboard Shear Failure FOS Computation (1 Failure Mode)
4. Glue Shear Failure FOS Computation (1 Failure Mode)

===== TO-DO LIST =====
1. Implement Local Buckling FOS Computation (4 Failure Modes)
2. Implement Euler Buckling Checking (1 Failure Mode)
3. Implement Allowed vs Actual Shear Force and Bending Moment Diagram Graphing

"""

from bridge_design import *
from passage_simulation.loading_until_failure import *

"""
Refer to documentation.py for instructions on utilizing this library.
"""

def main():
    LoadUntilFailure(beam_bridge)

if __name__ == "__main__":
    main()