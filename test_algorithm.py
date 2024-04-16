# test_algorithm.py
from algorithm import group_people
import pandas as pd

def run_tests():
    test_data = pd.DataFrame([
        {'gender': 'M', 'age': 20},
        {'gender': 'F', 'age': 25}
    ])
    result = group_people(test_data, {'gender': True})
    assert ('M',) in result and ('F',) in result, "Test Failed: Gender grouping not found."
    print("All tests passed!")

