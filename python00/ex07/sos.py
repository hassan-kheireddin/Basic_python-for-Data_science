import sys


def dec_morse(str):
    morse_dic = {
        'A': '.-',
        'B': '-...',
        'C': '-.-.',
        'D': '-..',
        'E': '.',
        'F': '..-.',
        'G': '--.',
        'H': '....',
        'I': '..',
        'J': '.---',
        'K': '-.-',
        'L': '.-..',
        'M': '--',
        'N': '-.',
        'O': '---',
        'P': '.--.',
        'Q': '--.-',
        'R': '.-.',
        'S': '...',
        'T': '-',
        'U': '..-',
        'V': '...-',
        'W': '.--',
        'X': '-..-',
        'Y': '-.--',
        'Z': '--..',
        '0': '-----',
        '1': '.----',
        '2': '..---',
        '3': '...--',
        '4': '....-',
        '5': '.....',
        '6': '-....',
        '7': '--...',
        '8': '---..',
        '9': '----.'}
    message = ""
    try:
        for code in str:
            message += morse_dic[code.upper()] + " "
    except KeyError:
        print("AssertionError: the argument are bad")
        sys.exit()
    return message[:len(message) - 1]


def main():
    """converts an input string into Morse code.
    It takes the string from the command line argument and outputs
    the corresponding Morse code representation. If there is an invalid
    argument or character, it raises an error."""
    try:
        if len(sys.argv) != 2:
            raise AssertionError("the number of arguments are bad")
    except AssertionError as error:
        print(f"AssertionError: {error}")
        sys.exit()
    str = sys.argv[1]
    result = dec_morse(str)
    print(result)


if __name__ == "__main__":
    main()
