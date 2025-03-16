from typing import Any


def ft_statistics(*args: Any, **kwargs: Any) -> None:
    """
    Calculates various statistical measures such as mean, median,
    quartile, standard deviation, and variance based on the input values
    provided as positional arguments. Additionally, the function supports
    keyword arguments that allow you to request specific statistical
    measures for printing."
    """
# convert tuple to list then modify it
    args_list = list(args)
    values = []
    num_args = 0
    for argument in args:
        # Check if the argument is numeric (either int or float)
        if not isinstance(argument, (int, float)):
            print("ERROR: All arguments must be numeric.")
            return
        num_args += 1
        values.append(argument)
    if num_args == 0:
        for value in kwargs.items():
            print("ERROR")
        return

# compute mean by adding all numbers then divide by total
    total = 0
    for arg in args_list:
        total += arg
    mean = total / num_args
# make bubble sort for median and quartiles:
    i = 0
    while i < num_args - 1:
        j = 0
        while j < num_args - i - 1:
            if values[j] > values[j + 1]:
                values[j], values[j + 1] = values[j + 1], values[j]
            j += 1
        i += 1
# compute median for even and odd total number
    median_index = num_args // 2
    if num_args % 2 == 0:
        median = (values[median_index - 1] + values[median_index]) / 2
    else:
        median = values[median_index]
# compute 1st and 4st quartile
    q1_index = num_args // 4
    q3_index = q1_index * 3
    quartile = [float(values[q1_index]), float(values[q3_index])]
# compute variance
    variance_total = 0
    for value in values:
        variance_total += (value - mean) ** 2
    variance = variance_total / num_args
# compute standard deviation
    std_deviation = (variance ** 0.5)
# put the values as they need in dictionary to access them directly.
    result = {"mean": mean, "median": median, "quartile": quartile,
              "std": std_deviation, "var": variance}
# print the result
    for key, value in kwargs.items():
        if value in result:
            print(f"{value} : {result[value]}")
