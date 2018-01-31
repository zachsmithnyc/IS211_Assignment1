
def factorial(n):
    """
    Calculate the factorial of a number

    :param n: integer
    :return: factorial
    """
    if n in [0, 1]:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    print "I'm inside main"

    print factorial(5)
