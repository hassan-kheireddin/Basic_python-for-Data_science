class calculator:
    """
    A class that provides static methods for performing vector operations
    such as dot product, vector addition, and vector subtraction.
    """
    @staticmethod
    def dotproduct(V1: list[float], V2: list[float]) -> None:
        """
        Calculates the dot product of two vectors.
        """
        result = 0
        for i in range(len(V1)):
            result += V1[i] * V2[i]
        print(f"Dot product is: {result}")

    @staticmethod
    def add_vec(V1: list[float], V2: list[float]) -> None:
        """
        Adds two vectors element-wise.
        """
        result = []
        for i in (range(len(V1))):
            result.append(float(V1[i]) + float(V2[i]))
        print(f"Add Vector is {result}")

    @staticmethod
    def sous_vec(V1: list[float], V2: list[float]) -> None:
        """
        Subtracts the second vector from the first vector element-wise.
        """
        result = []
        for i in (range(len(V1))):
            result.append(float(V1[i]) - float(V2[i]))
        print(f"Add Vector is: {result}")
