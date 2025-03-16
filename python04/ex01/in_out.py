def square(x: int | float) -> int | float:
    """
    compute x power 2
    """
    return x * x


def pow(x: int | float) -> int | float:
    """
    compute x power x
    """
    return x ** x


def outer(x: int | float, function) -> object:
    """
    it return an function as object and it is called callable function.
    it can be called more than one time and update the value every time
    """
    count = 0

    def inner() -> float:
        """
        inner is using nonlocal variable wich act as global variable but
        it is local inside the function and modify its value every time
        """
        nonlocal count
        nonlocal x
        count += 1
        result = function(x)
        x = result
        return float(result)

    return inner
