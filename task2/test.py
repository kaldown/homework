"""
As far as there is no input and no dynamic variables.
Then it maskes sense to test the programm for a certain values.
No mocks needed.
"""

from numbers import numbers_generator, NumbersMultiplier


# setUp
VALUES_TO_TEST = list(numbers_generator())

def test_three():
    # test for Three
    value_to_check = NumbersMultiplier.THREE.value
    assert VALUES_TO_TEST[2] == value_to_check
    assert VALUES_TO_TEST[11] == value_to_check
    assert VALUES_TO_TEST[98] == value_to_check


def test_five():
    # test for Five
    value_to_check = NumbersMultiplier.FIVE.value
    assert VALUES_TO_TEST[4] == value_to_check
    assert VALUES_TO_TEST[24] == value_to_check
    assert VALUES_TO_TEST[99] == value_to_check


def test_threefive():
    # test for ThreeFive
    value_to_check = NumbersMultiplier.THREEFIVE.value
    assert VALUES_TO_TEST[14] == value_to_check
    assert VALUES_TO_TEST[44] == value_to_check
    assert VALUES_TO_TEST[29] == value_to_check


def main():
    test_three()
    test_five()
    test_threefive()


if __name__ == '__main__':
    main()
