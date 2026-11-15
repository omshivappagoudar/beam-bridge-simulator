from beam_properties import BeamProperties


def main():

    ## For now this is just a test case
    pieces = [{"b": 10.0, "h": 20.0, "y": 10.0}]

    beam = BeamProperties(pieces)

    print(f"Area: {beam.area:.2f} mm^2")
    print(f"Centroid: {beam.y_bar:.2f} mm")
    print(f"Moment of inertia: {beam.I:.2f} mm^4")


if __name__ == "__main__":
    main()