def callLimit(limit: int):
    """
    Takes an integer 'limit' as input and returns a decorator that restricts
    the number of times a decorated function can be called.
    When the decorated function is called, its execution is allowed only up
    to the specified 'limit'. If the function is called more times than the
    limit, a 'AssertionError' is raised.
    """

    count = 0

    def callLimiter(function):
        """
        Decorator:
        This inner function is used to wrap around the target function.
        It tracks the number of times the target function is called
        using the 'count' variable.
        """

        def limit_function(*args, **kwds):
            """
            Wrapper:
            Used as a wrapper around the decorated function.
            It increments the 'count' variable each time the wrapped
            function is called. If the 'count' is within the limit,
            the wrapped function is executed.
            Raises:
            AssertionError: If the call limit has been exceeded.
            """
            try:
                nonlocal count
                count += 1
                if count <= limit:
                    return function(*args, **kwds)
                else:
                    raise AssertionError(f"{function} call too many times")
            except AssertionError as error:
                print("Error:", error)
        return limit_function

    return callLimiter
