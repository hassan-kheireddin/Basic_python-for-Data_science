import os


def wheel():
    os.system("pip install wheel")
    print()


def setup():
    os.system("python3 setup.py sdist bdist_wheel")
    print()


def install():
    os.system("pip install ./dist/ft_package-0.0.1-py3-none-any.whl")
    print()


def show():
    os.system("pip3 show -v ft_package")
    print()


def test():
    os.system("python3.10 tester.py")


if __name__ == "__main__":
    wheel()
    setup()
    install()
    show()
    test()
