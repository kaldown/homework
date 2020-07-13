from enum import Enum


class NumbersMultiplier(Enum):
    THREE = "Three"
    FIVE = "Five"
    THREEFIVE = "ThreeFive"


def numbers_generator():
    """Generator yielding numbers from 1 to 100.
    If number is multiples of 3, yield "Three",
    If number is multiples of 5, yield "Five",
    If number is multiples of 3 and 5, yield "ThreeFive",
    Yield number otherwise.
    """
    start_number = 1
    end_number = 100

    for number in range(start_number, end_number+1):
        if not number % 15:
            yield NumbersMultiplier.THREEFIVE.value
        elif not number % 3:
            yield NumbersMultiplier.THREE.value
        elif not number % 5:
            yield NumbersMultiplier.FIVE.value
        else:
            yield number


def print_numbers(numbers_producer):
    """Consumer of a numbers generator.
    Only prints given values.
    """
    for number in numbers_producer:
        print(number)


def main():
    """Main entry point to run a programm.
    """
    numbers_producer = numbers_generator()
    print_numbers(numbers_producer)


if __name__ == '__main__':
    main()
