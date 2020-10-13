from pytest import mark
from app.roman_numerals import parse

@mark.parametrize("roman_letter,expected", [("IX", 9), ("X", 10), ("XI", 11), ("XIV", 14), ("XIX", 19), ("XX", 20), ("XXXIV",	34), ("XLI",	41), ("L",	50), ("XCIX",	99), ("C", 100), ("CCCXXXIII", 333), ("DLV"	,555),("CDXLIX", 449), ("MCMLXXII", 1972)])
def test_roman_numeral_parser(roman_letter, expected):
    integer = parse(roman_letter)
    assert integer == expected
