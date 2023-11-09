class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def print_longest_side(self):
        sides = [self.side1, self.side2, self.side3]
        longest_side = max(sides)
        print(f"El lado con mayor tamaño es: {longest_side}")

    def determine_type(self):
        if self.side1 == self.side2 == self.side3:
            print("El triángulo es equilátero.")
        elif self.side1 == self.side2 or self.side1 == self.side3 or self.side2 == self.side3:
            print("El triángulo es isósceles.")
        else:
            print("El triángulo es escaleno")

# Example of usage
side1 = 20
side2 = 10
side3 = 5
triangle = Triangle(side1, side2, side3)

triangle.print_longest_side()
triangle.determine_type()

