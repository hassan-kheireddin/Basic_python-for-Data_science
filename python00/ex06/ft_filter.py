def ft_filter(ft_function, listIterable):
    """filter(function or None, iterable) --> filter object

Return an iterator yielding those items of iterable for which function(item)
is true. If function is None, return the items that are true."""
    return (str for str in listIterable if ft_function(str))
