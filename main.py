"""

===== COMPLETED =====
1. Tensile Rupture FOS Computation (1 Failure Mode)
2. Compressive Crushing FOS Computation (1 Failure Mode)
3. Matboard Shear Failure FOS Computation (1 Failure Mode)
4. Glue Shear Failure FOS Computation (1 Failure Mode)
5. Local Buckling FOS Computation (4 Failure Modes)

"""

from bridge_design import *
from passage_simulation.loading_until_failure import *

import math

def main():
    LoadUntilFailure(beam_bridge)

if __name__ == "__main__":
    main()