from beam_properties import BeamProperties


def main():

    # TEST CASE (for beam_properties.py)
    # CIV102 Bridge Design Project Deliverable 1 - Question 4 (Design 0)
    pieces = [
        {"b": 100, "h": 1.27, "y": 75 + 1.27 / 2}, # Piece 1
        {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 2
        {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 3
        {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 4
        {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 5
        {"b": 80, "h": 1.27, "y": 1.27 / 2}, # Piece 6
    ]
    # Correct Answer achieved for both the centroid and the moment of inertia!

    beam = BeamProperties(pieces)

    print(f"Area: {beam.area:.2f} mm^2")
    print(f"Centroid: {beam.y_bar:.2f} mm")
    print(f"Moment of inertia: {beam.I:.2f} mm^4")


if __name__ == "__main__":
    main()