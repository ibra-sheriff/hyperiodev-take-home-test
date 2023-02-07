# Test ISBN File
# date: 03/02/2023
# name: Ibrahim Sheriff Sururu
# description: This is the test suite that uses Python's nose to test the functions found in the isbn.py file.
# The following aspects are tested:
#    - Input validation
#    - Checking ISBN-10 validity
#    - Checking ISBN-13 validity
#    - Converting a ISBN-10 number to a ISBN-13 number.
import isbn


def test_validation1():
    # Check that the validation function does not accept types that are not str.
    assert isbn.validation(5) == "Invalid"
    assert isbn.validation(3.142) == "Invalid"
    assert isbn.validation(3.142) == "Invalid"
    assert isbn.validation(["123456789X"]) == "Invalid"


def test_validation2():
    # Check that the validation function does not accept ISBN numbers of the wrong length.
    assert isbn.validation("123456") == "Invalid"
    assert isbn.validation("12345678X") == "Invalid"
    assert isbn.validation("12345678991") == "Invalid"
    assert isbn.validation("123456789100") == "Invalid"


def test_validation3():
    # Check that the validation function does accept correctly formated ISBN numbers.
    assert isbn.validation("123456789X") == "Valid"
    assert isbn.validation("1234567891000") == "Valid"


def test_valid1():
    # Check that the main ISBN function can deem valid ISBN numbers valid.
    assert isbn.isbn13("9780316066525") == "Valid"
    assert isbn.isbn13("0330301826") == "Valid"
    assert isbn.isbn13("9780136091813") == "Valid"
    assert isbn.isbn13("9783161484100") == "Valid"


def test_valid2():
    # Check that the ISBN-10 validity function is working correctly.
    assert isbn.valid_isbn10("0136091814") == True
    assert isbn.valid_isbn10("0136091812") == False
    assert isbn.valid_isbn10("123456789X") == True
    assert isbn.valid_isbn10("0590764845") == True


def test_valid3():
    # Check that the ISBN-13 validity function is working correctly.
    assert isbn.valid_isbn13("9780136091813") == True
    assert isbn.valid_isbn13("9780136091817") == False
    assert isbn.valid_isbn13("9783161484100") == True
    assert isbn.valid_isbn13("9783161484100") == True


def test_invalid1():
    # Check that the main ISBN function can deem invalid ISBN numbers invalid.
    assert isbn.isbn13("0136091815") == "Invalid"
    assert isbn.isbn13("9783161484101") == "Invalid"
    assert isbn.isbn13("1234567890") == "Invalid"
    assert isbn.isbn13("9780136091812") == "Invalid"


def test_isbn10_conversion():
    # Check that the main ISBN function  an correctly convert ISBN-10 numbers to ISBN-13.
    assert isbn.convert_isbn10_to_isbn13("0316066524") == "9780316066525"
    assert isbn.isbn13("0136091814") == "9780136091817"
    assert isbn.isbn13("0136091814") == "9780136091817"
    assert isbn.isbn13("123456789X") == "9781234567893"
    assert isbn.isbn13("0590764845") == "9780590764849"

