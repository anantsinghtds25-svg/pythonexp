def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid number.")


def get_integer(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")


def display_result(result):
    if isinstance(result, float) and result.is_integer():
        print(f"Result = {int(result)}")
    else:
        print(f"Result = {result}")


def pause():
    input("\nPress Enter to continue...")