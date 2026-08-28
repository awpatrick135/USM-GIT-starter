import math

# --- Calculation Functions ---
import math


def getArea(a, b):
    return a * b

def getPerimeter(a, b):
    return 2 * (a + b)

def getCircleArea(radius):
    return math.pi * radius ** 2

def getCirclePerimeter(radius):
    return 2 * math.pi * radius

def getCircleDiameter(radius):
    return 2 * radius

def getCircleCircumference(radius):
    return 2 * math.pi * radius


# --- Main Menu System ---

def main():
    while True:
        print("Select a shape to calculate:")
        print("1. Rectangle")
        print("2. Circle")
        print("3. Exit")

        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            length = float(input("Enter the length of the rectangle: "))
            width = float(input("Enter the width of the rectangle: "))
            print(f"Area: {getArea(length, width)}")
            print(f"Perimeter: {getPerimeter(length, width)}")

        elif choice == "2":
            radius = float(input("Enter the radius of the circle:"))
            print(f"Area: {getCircleArea(radius)}")
            print(f"Perimeter: {getCirclePerimeter(radius)}")

        elif choice == "3":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
# --- Run the Program ---
if __name__ == "__main__":
    main()