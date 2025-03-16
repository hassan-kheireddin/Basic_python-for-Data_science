class calculator:
    """
    A class to represent a vector calculator.

    __add__(self, object) :
        Adds a given value or number to each element of the vector.

    __mul__(self, object) :
        Multiplies each element of the vector by a given value or number.

    __sub__(self, object) :
        Subtracts a given value or number from each element of the vector.

    __truediv__(self, object) :
        Divides each element of the vector by a given value or number.
    """
    def __init__(self, vector):
        """
        Initializes the Calculator with a vector (list of numbers).
        """
        self.vector = vector

    def __add__(self, object) -> None:
        """
        Adds the given object (a number) to each element of the vector.
        """
        for i in range(len(self.vector)):
            self.vector[i] += object
        print(self.vector)

    def __mul__(self, object) -> None:
        """
        Multiplies each element of the vector by the given object (a number).
        """
        for i in range(len(self.vector)):
            self.vector[i] *= object
        print(self.vector)

    def __sub__(self, object) -> None:
        """
        Subtracts the given object (a number) from each element of the vector.
        """
        for i in range(len(self.vector)):
            self.vector[i] -= object
        print(self.vector)

    def __truediv__(self, object) -> None:
        """
        Divides each element of the vector by the given object (a number).
        """
        try:
            if object == 0:
                raise ZeroDivisionError("division by zero")
        except ZeroDivisionError as error:
            print(ZeroDivisionError, error)
            return
        for i in range(len(self.vector)):
            self.vector[i] /= object
        print(self.vector)
