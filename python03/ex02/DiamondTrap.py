from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """
    A class representing a King, inheriting from the Baratheon
    and Lannister families.

    The King class initializes a king with a name and alive status,
    and provides setter and getter methods for attributes like eyes
    and hair color.
    """
    def __init__(self, first_name, is_alive=True):
        """
        Initializes a King object with a given first name and alive status.
        """
        super().__init__(first_name, is_alive)

    def set_eyes(self, color):
        """
        Sets the eye color of the King.
        """
        self.eyes = color

    def get_eyes(self):
        """
        Returns the eye color of the King.
        """
        return self.eyes

    def set_hairs(self, color):
        """
        Sets the hair color of the King.
        """
        self.hairs = color

    def get_hairs(self):
        """
        Returns the hair color of the King.
        """
        return self.hairs
