"""Program code"""

# First party imports
from factorial import Factorial
from tower_of_hanoi import TowerOfHanoi


def main(*args):
    """Method to run program"""

    # Create instance of Factorial class to use
    factorial = Factorial()
    # Create instance of Tower of Hanoi
    # Don't forget to import
    hanoi = TowerOfHanoi()

    # Show menu and collect input
    print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to exit.")
    choice = input()

    # While choice is less than exit criteria.
    # NOTE: Assuming good input from user.
    while int(choice) < 3:
        # if solving factorial
        if choice == "1":
            # Do factorial
            print("What number would you like to solve? 5 is a good choice.")
            print("> ", end="")
            number = int(input())

            print()
            print(f"Solving {number}!")
            print("The answer is: ", end="")
            print(factorial.solve(number))

        elif choice == "2":
            # Do tower of Hanoi
            print("What number of discs would you like to solve? 5 is a good choice.")
            print("> ", end="")
            number = int(input())

            print()
            print(f"Solving {number} discs")
            print("See the steps below.")
            hanoi.solve(number)

        # Re-show menu and collect input
        print()
        print()
        print("Enter 1 for factorial, 2 for Tower of Hanoi, 3 to exit.")
        choice = input()
