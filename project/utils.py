import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_positive_float(prompt: str) -> float:
    while True:
        try:
            val = float(input(prompt))
            if val > 0: return val
            print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")

def get_positive_int(prompt: str) -> int:
    while True:
        try:
            val = int(input(prompt))
            if val > 0: return val
            print("Value must be greater than zero.")
        except ValueError:
            print("Invalid input. Please enter an integer.")