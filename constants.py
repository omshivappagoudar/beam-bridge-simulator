# ===== MATERIAL PROPERTIES =====

BRIDGE_LENGTH = 1200                         # mm

MATBOARD_YOUNGS_MODULUS = 4000              # MPa
MATBOARD_TENSILE_FAILURE_STRESS = 30        # MPa
MATBOARD_COMPRESSIVE_FAILURE_STRESS = 6     # MPa
MATBOARD_SHEAR_FAILURE_STRESS = 4           # MPa
CONTACT_CEMENT_SHEAR_FAILURE_STRESS = 2     # MPa (If properly cured)

# ===== TRAIN GEOMETRY =====

B1 = 0                                      # mm
B2 = 176                                    # mm
B3 = 176 + 164                              # mm
B4 = 176 + 164 + 176                        # mm
B5 = 176 + 164 + 176 + 164                  # mm
B6 = 176 + 164 + 176 + 164 + 176            # mm
TRAIN_POINT_LOAD_LOCATIONS = [B1, B2, B3, B4, B5, B6]
TRAIN_LENGTH = B6 - B1