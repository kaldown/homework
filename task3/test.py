"""Simple test cases, no need to use PyTest.
"""

from postcodes import PostCode


CODES = [
    "EC1A 1BB", "W1A 0AX", "M1 1AE",
    "B33 8TH", "CR2 6XH", "DN55 1PT",
]

def test_valid_codes():
    for code in CODES:
        pc = PostCode(code)
        pc.validate()
        assert pc.format()


def test_valid_codes_not_validated():
    for code in CODES:
        pc = PostCode(code)
        try:
            pc.format()
        except ValueError:
            # test passed
            pass
        else:
            # must not be here (simulate PyTest assertException)
            raise Exception("Test failed")


def test_invalid_codes():
    for code in CODES:
        pc = PostCode(code)
        pc.validate()
        assert pc.format()


def test_invalid_codes_raised():
    for code in CODES:
        pc = PostCode(code + "1")
        try:
            pc.validate(raise_exception=True)
        except ValueError:
            # test passed
            pass
        else:
            # must not be here (simulate PyTest assertException)
            raise Exception("Test failed")


def main():
    test_valid_codes()
    test_valid_codes_not_validated()

    test_invalid_codes()
    test_invalid_codes_raised()


if __name__ == '__main__':
    main()
