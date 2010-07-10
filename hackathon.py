import nose
import hackathon


def add(x, y):
    return x + y


def sub(x, y):
    return x - y


def double(x):
    return x * 2


def even(x):
    return x % 2 == 0


def greeting(message="Hello"):
    return message


if __name__ == '__main__':
    nose.main()


