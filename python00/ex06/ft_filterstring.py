import sys
from ft_filter import ft_filter


def main():
    """It takes two command-line arguments:
    A string containing multiple words.
    An integer specifying a length threshold.
The script filters out words from the string that are shorter than
or equal to the given length using a custom filtering function
(ft_filter)."""

    try:
        if len(sys.argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            strin = list(sys.argv[1].split())
            num = int(sys.argv[2])
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit()
    finished = list(ft_filter(lambda string: len(string) > num, strin))
    print(finished)


if __name__ == "__main__":
    main()
