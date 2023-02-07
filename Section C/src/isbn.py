# ISBN File
# date: 03/02/2023
# name: Ibrahim Sheriff Sururu
# description: The International Standard Book Number (ISBN) is a unique identifying number given to each published 
# book. ISBNs assigned after January 2007 are 13 digits long(ISBN-13), however books with 10-digit ISBNs are still
# in wide use. This file was created to check if a given ISBN number is ISBN-10 or ISBN-13. It also has a function
# to handle validation of input.
#
# The full specification of the source file can be found here: https://edabit.com/challenge/C5mooK3wfdhoooeLw


VALID_CHARACTERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']


def validation(test_val):
    """
    Check if the given input number is in valid ISBN-10 or ISBN-13 format i.e. it contains only numbers and
    the letter X(in the case of ISBN-10) and is either 10 characters long or 13 characters long.

    Note: This function only checks if the number contains valid characters, not that the ISBN number is
    actually valid.

    :param test_val: the input value to check
    :return: 'Valid' if the number is in ISBN-10 or ISBN-13 format and 'Invalid' if it is not.
    """
    # check the object type
    if not isinstance(test_val, str):
        return "Invalid"
    # check the length
    elif len(test_val) != 10 and len(test_val) != 13:
        return "Invalid"

    # check each character to ensure it is valid
    for val in test_val:
        if val not in VALID_CHARACTERS:
            return "Invalid"

    return "Valid"


def valid_isbn10(test_val):
    """
    Check if the given input value is a valid ISBN-10 number.

    :param test_val: the input value to check for validity
    :return: True if the given input value is a valid ISBN-10 number and False otherwise.
    """
    n = 10
    i = 0
    total_sum = 0
    while n >= 1:
        if test_val[i] == "X":
            total_sum = total_sum + (10 * n)
        else:
            total_sum = total_sum + (int(test_val[i]) * n)
        i = i + 1
        n = n - 1

    return total_sum % 11 == 0


def valid_isbn13(test_val):
    """
    Check if the given input value is a valid ISBN-13 number.

    :param test_val: the input value to check for validity
    :return: True if the given input value is a valid ISBN-13 number and False otherwise.
    """
    total_sum = 0
    indicator = -1
    for val in test_val:
        # indicator is used to alternate the 1 and 3
        if indicator == -1:
            total_sum = total_sum + (int(val) * 1)
        else:
            total_sum = total_sum + (int(val) * 3)
        indicator = indicator * -1
    
    return total_sum % 10 == 0


def convert_isbn10_to_isbn13(test_val):
    """
    Converts the given input value that is in ISBN-10 format to a ISBN-13 number.

    :param test_val: the ISBN-10 input number
    :return: the ISBN-13 version of the given ISBN-10 number
    """
    temp_isbn13 = "978" + test_val[0:9]
    total_sum = 0
    indicator = -1
    for val in temp_isbn13:
        # indicator is used to alternate the 1 and 3
        if indicator == -1:
            total_sum = total_sum + (int(val) * 1)
        else:
            total_sum = total_sum + (int(val) * 3)
        indicator = indicator * -1

    checksum = total_sum % 10
    
    return temp_isbn13 + str(checksum)


def isbn13(test_val):
    """
    Checks if the given input is a valid ISBN-10 or ISBN-13 number. If it a valid ISBN-13 number
    the string 'Valid' is returned, else if the string is a valid ISBN-10 number it is converted
    to a ISBN-13 number and the result returned.

    :param test_val: the input to use in the checks/conversion.
    :return: 'Invalid' if it is not a valid ISBN-10 or ISBN-13. 'Valid' if it is a valid ISBN-13.
    If it is a valid ISBN-10, convert it into an ISBN-13 and return the ISBN-13 number.
    """
    if validation(test_val) == "Invalid":
        return "Invalid"
    if valid_isbn10(test_val):
        return convert_isbn10_to_isbn13(test_val)
    elif valid_isbn13(test_val):
        return "Valid"

    return "Invalid"


if __name__ == "__main__":
    print(isbn13("9780330301628"))

