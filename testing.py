from constants_and_conventions import *
from beam_properties import *
from analyze_FBD import *

# ===== RESULT PRINTING =====

def verify_response(test_suite_name, test_name, response, expected_response, threshold = 0.01):
    if type(expected_response) != type(response):
        print(f"\033[91mTest Case Failed! (Test Suite: {test_suite_name} | Test Case: {test_name} | Response Type: {type(response)} | Expected Response Type: {type(expected_response)})\033[0m")
        return

    if isinstance(expected_response, int) or isinstance(expected_response, float):
        response_correct = numbers_match(response, expected_response)
    elif isinstance(expected_response, list):
        response_correct = lists_match(response, expected_response)
    
    if abs((response - expected_response) / expected_response) < threshold:
        print(f"\033[92mTest Case Passed! (Test Suite: {test_suite_name} | Test Case: {test_name})\033[0m")
        return
    else:
        print(f"\033[91mTest Case Failed! (Test Suite: {test_suite_name} | Test Case: {test_name}\033[0m")
        if not (isinstance(expected_response, list) or isinstance(response, list)):
            print(f"\033[91m\tResponse: {response:.2f} | Expected Response: {expected_response:.2f})\033[0m")
        return

def numbers_match(num1, num2, threshold = 0.01):
    return abs((num1 - num2) / num2) < threshold

def lists_match(list1, list2, threshold = 0.01):
    if len(list1) != len(list2):
        return False
    for i in range(len(list1)):
        if list1[i] != list2[i]:
            return False
    return True
    

# ===== TESTS =====

def run_full_test_suite():
    test_BeamProperties_class()
    test_AnalyzeFBD_class()

def test_BeamProperties_class(): # Test Cases for beam_properties.py

    # ===== TEST CASE =====
    # CIV102 Bridge Design Project Deliverable 1 - Question 4 (Design 0)
    pieces = [
        {"b": 100, "h": 1.27, "y": 75 + 1.27 / 2}, # Piece 1
        {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 2
        {"b": 6.27, "h": 1.27, "y": 75 - 1.27 / 2}, # Piece 3
        {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 4
        {"b": 1.27, "h": 75 - 2 * 1.27, "y": 75 / 2}, # Piece 5
        {"b": 80, "h": 1.27, "y": 1.27 / 2}, # Piece 6
    ]
    beam_properties = BeamProperties(pieces)

    verify_response(
        test_suite_name = "BeamProperties Class",
        test_name = "Design 0 Area",
        response = beam_properties.area,
        expected_response = 428.57,
        threshold = 0.01
    )

    verify_response(
        test_suite_name = "BeamProperties Class",
        test_name = "Design 0 Centroid",
        response = beam_properties.centroid,
        expected_response = 41.431,
        threshold = 0.01
    )

    verify_response(
        test_suite_name = "BeamProperties Class",
        test_name = "Design 0 Moment of Inertia",
        response = beam_properties.moment_of_inertia,
        expected_response = 418352.21,
        threshold = 0.01
    )

def test_AnalyzeFBD_class():

    # ===== TEST CASE =====
    # CIV102 Bridge Design Project Deliverable 1 - Question 3 (Base Case Loading; 452 N)
    train_loads = [-67.5, -67.5, -67.5, -67.5, -91.0, -91.0]
    train_location = 172
    FBD_analysis = AnalyzeFBD(train_loads, train_location)

    verify_response(
        test_suite_name = "AnalyzeFBD Class",
        test_name = "Base Case Loading Left Reaction Force",
        response = FBD_analysis._left_reaction_force_y,
        expected_response = 212.7,
        threshold = 0.01
    )

    verify_response(
        test_suite_name = "AnalyzeFBD Class",
        test_name = "Base Case Loading Right Reaction Force",
        response = FBD_analysis._right_reaction_force_y,
        expected_response = 239.3,
        threshold = 0.01
    )

    verify_response(
        test_suite_name = "AnalyzeFBD Class",
        test_name = "Base Case Loading Shear Force Diagram at x = 600 mm",
        response = FBD_analysis.shear_force_diagram[600],
        expected_response = 10.20,
        threshold = 0.01
    )

    verify_response(
        test_suite_name = "AnalyzeFBD Class",
        test_name = "Base Case Loading Bending Moment Diagram at x = 852 mm",
        response = FBD_analysis.bending_moment_diagram[852],
        expected_response = 67300.0,
        threshold = 0.01
    )