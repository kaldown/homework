import re

# Can be places in settings. Omit that, because lib is fairy simple.
NORMAL_CASE_PATTERN = r"^[A-Z]{1,2}[0-9][A-Z0-9]? ?[0-9][A-Z]{2}$"
SPECIAL_CASE_PATTERN = r"^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$"
DEFAULT_CASE_PATTERN = NORMAL_CASE_PATTERN

PROG = re.compile(DEFAULT_CASE_PATTERN)


class PostCode:
    def __init__(self, value) -> None:
        self._value = value
        self._validated = False
        self._formatted_code = ""

    def validate(self, raise_exception: bool=False) -> None:
        """Metnod to define validateion.
        Using default regexp pattern.

        Validation is made strict.

        If code is invalid validation will fail.
        No autocorrection involved.
        """
        if result := PROG.match(self._value):
            self._validated = True
            self._formatted_code = result.group()

        elif raise_exception:
            raise ValueError(f"Invalid PostalCode: {self._value}")

    def format(self) -> str:
        """Method to return formatted PostalCode.

        P.S. for smplicity reasons, I return just the postal code,
            rather than object with all areas an groups
        """
        if not self._validated:
            raise ValueError("PostalCode must be validated first.")

        if not self._formatted_code:
            raise ValueError("Given PostalCode is invalid.")

        return self._formatted_code
