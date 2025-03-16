import sys


def main():
    """It counts the number of uppercase letters, lowercase letters,
    digits, spaces, and punctuation marks in the input text.
    It prints these counts to the console."""
    temp = sys.argv
    str = ""
    try:
        if len(temp) > 2:
            raise AssertionError("Error too many arguments!")
        elif len(temp) == 2:
            str = temp[1]
        else:
            print("What is the text to count?")
            while True:
                line = sys.stdin.readline()
                if line == "":
                    break
                str += line
    except AssertionError as error:
        print(f"AsserationError : {error}")
        sys.exit()
    punc_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    upper_chars = sum(1 for check in str if check.isupper())
    lower_chars = sum(1 for check in str if check.islower())
    digits = sum(1 for check in str if check.isdigit())
    spaces = sum(1 for check in str if check.isspace())
    punc = sum(1 for check in str if check in punc_chars)
    print(f"The text contains {len(str)} characters:")
    print(f"{upper_chars} upper letters")
    print(f"{lower_chars} lower letters")
    print(f"{punc} punctuation letters")
    print(f"{spaces} spaces")
    print(f"{digits} digits")


if __name__ == "__main__":
    main()
