# main.py
from data_handler import load_data
from algorithm import group_people
from test_algorithm import run_tests

def main():
    try:
        data = load_data()
        grouped_data = group_people(data)
        print("Grouping Completed.")
        print(grouped_data)
        run_tests()
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
