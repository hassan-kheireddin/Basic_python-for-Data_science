from S1E9 import Character


class Baratheon(Character):
    """
    Baratheon family class, inheriting from Character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        intialize the name and is alive of this abstract class
        by super().__init__() take input from parent and assign other
        manually.
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Baratheon"
        self.eyes = "brown"
        self.hairs = "dark"

    def die(self):
        """
        assign is alive with false
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Return the string representation for the Lannister family.
        """
        return f"bound method Baratheon.__str__ of Vector: (\
'{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Return the formal string representation for debugging.
        """
        return f"bound method Baratheon.__repr__ of Vector: (\
'{self.family_name}', '{self.eyes}', '{self.hairs}')"


class Lannister(Character):
    """
    Lannister family class, inheriting from Character.
    """
    def __init__(self, first_name, is_alive=True):
        """
        intialize the name and is alive of this abstract class
        by super().__init__() take input from parent and assign other
        manually
        """
        super().__init__(first_name, is_alive)
        self.family_name = "Lannister"
        self.eyes = "blue"
        self.hairs = "light"

    def die(self):
        """
        assign is alive with false
        """
        self.is_alive = False

    def __str__(self) -> str:
        """
        Return the string representation for the Lannister family.
        """
        return f"bound method Baratheon.__str__ of Vector: (\
'{self.family_name}', '{self.eyes}', '{self.hairs}')"

    def __repr__(self) -> str:
        """
        Return the formal string representation for debugging.
        """
        return f"bound method Baratheon.__repr__ of Vector: (\
'{self.family_name}', '{self.eyes}', '{self.hairs}')"

    @classmethod
    def create_lannister(cls, first_name, is_alive=True):
        """
        Class method to create a Lannister character.
        """
        return cls(first_name, is_alive)
