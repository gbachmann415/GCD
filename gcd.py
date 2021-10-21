"""
Gunnar Bachmann
9/16/2019
gcd.py
Write and test a tail-recursive function that determines
the greatest common divisor (GCD) of two numbers.

"""


def gcd_rec(a, b):
    """
    Recursive function to compute the GCD
    of two numbers (a and b).

    Pre-conditions: inputs are integers

    gcd(a,b) = a, if b=0
    gcd(a,b) = gcd(b,a mod b), otherwise

    :param a: number 1
    :param b: number 2
    :return:
    """
    if b == 0:
        return a
    else:
        acc = (a % b)
        return gcd_rec(b, acc)


def test_gcd_rec():
    """
    Test function to test the function gcd_rec by calling it
    several times with different inputs.

    preconditions: gcd_rec(a, b) must be working properly for this function to work properly.

    :return:
    """
    print(gcd_rec(24, 36))
    print(gcd_rec(48, 18))
    print(gcd_rec(72, 8))
    print(gcd_rec(37, 0))
    print(gcd_rec(33, 33))
    print(gcd_rec(43, 76))
    print(gcd_rec(1, 1))
    print(gcd_rec(50, 20))
    print(gcd_rec(30, 60))


def gcd_iter(a, b):
    """
    Iterative function to compute the GCD of
    2 numbers (a and b).

    preconditions: inputs are integers

    :param a: number 1
    :param b: number 2
    :return:
    """
    while True:
        if b == 0:
            return a
        else:
            acc = (a % b)
            return gcd_rec(b, acc)


def test_gcd_iter():
    """
    This function is to test the function gcd_iter
    to make sure it works correctly. Test cases using
    a variety of numbers to attempt at checking a range
    of possibilities.

    preconditions: gcd_iter(a, b) must be working properly for this function to work properly.

    :return:
    """
    print(gcd_iter(24, 36))
    print(gcd_iter(48, 18))
    print(gcd_iter(72, 8))
    print(gcd_iter(37, 0))
    print(gcd_iter(33, 33))
    print(gcd_iter(43, 76))
    print(gcd_iter(1, 1))
    print(gcd_iter(50, 20))
    print(gcd_iter(30, 60))


def main():
    """
    Main function to run the programs, along with taking user input to choose which
    functions will run. Also, this function takes the user input for which two numbers
    to compute the GCD of.

    preconditions: all functions defined that are being used must function properly. Also the proper
    string conversions must take place for this entire function to work properly.
    :return:
    """
    print("Select the GCD Function to use:\n1. Recursive\n2. Iterative")
    user_input = int(input("Please select a function (please enter the number 1 or 2): "))
    first_num = int(input("Please enter the first number: "))
    second_num = int(input("Please enter the second number: "))
    if user_input == 1:
        print("The GCD is ", gcd_rec(first_num, second_num))
    elif user_input == 2:
        print("The GCD is ", gcd_iter(first_num, second_num))


if __name__ == '__main__':
    main()