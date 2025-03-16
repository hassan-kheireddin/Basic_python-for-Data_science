from abc import ABC, abstractmethod


class Character(ABC):
    """
    character is an abstract class inherit ABC and conain abstract methods.
    methods are not implemented in the abstract class but are marked as
    abstract using @abstractmethod.
    """
    def __init__(self, first_name, is_alive=True):
        """
        intialize the name and is alive of this abstract class.
        """
        self.first_name = first_name
        self.is_alive = is_alive

    @abstractmethod
    def die(self):
        """
        die here is the abstract method of the abstract class.
        """
        pass


class Stark(Character):
    """
    Stark is subclass of the abstract class and inherit from character
    and must implement the abstract methods.
    """
    def die(self):
        """
        assign is alive with false.
        """
        self.is_alive = False
