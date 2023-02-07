# Say Number File
# date: 03/02/2023
# name: Ibrahim Sheriff Sururu
# description: This source file contains a function that takes a numeral (just digits without separators
# (e.g. 19093 instead of 19,093) and returns the standard way of reading a number, complete with punctuation.
#
# The full specification can be found here: https://edabit.com/challenge/4E9gTrRWErpTCA2FQ
import num2words


def say_number(num):
    """
    Takes a numeral (just digits without separators(e.g. 19093 instead of 19,093) and returns the standard
    way of reading a number, complete with punctuation.

    :param num: the numeric representation of the number to convert
    :return: a string containing words that relate to the standard way of reading a number, complete with punctuation.
    """
    # get the string from the num2words and then clean it up into the correct format(post-processing)
    temp_result = num2words.num2words(num)
    temp_result = temp_result.replace("-", " ") + "."
    return temp_result.capitalize()


def test():
    temp = ""
    for num_i in range(0, 21):
        print(say_number(num_i))
        temp = temp + say_number(num_i) + " "

    temp = ""
    for num_i in range(21, 100):
        temp = temp + say_number(num_i) + " "
    print(temp + "\n")
    print(say_number(221))
    print(say_number(2210))
    print(say_number(19093))
    print(say_number(190932))
    print(say_number(1043283))
    print(say_number(90376000010012))


if __name__ == "__main__":
    test()

