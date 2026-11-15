# Beam Bridge Simulator

A Python tool for evaluating matboard box-girder bridge designs for CIV102. Our team creates the designs; the simulator calculates their structural properties and, as development progresses, their response to a moving train load.

## Current Features

- Define cross-sections using rectangular pieces.
- Calculate cross-sectional area, centroid, and second moment of area.

## Planned Features

- Moving train loads and support reactions.
- Shear-force and bending-moment envelopes.
- Stress, buckling, and factor-of-safety calculations.
    - Ideally want to display graphs of these as well to visualize information for the report
- Ideally will be able to pass through possible designs in csv format to parse through and calculate for multiple proposed cross sections

## Running

Requires Python 3. No external packages needed for now

```bash
python main.py