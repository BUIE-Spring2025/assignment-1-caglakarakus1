def int_to_roman(num):

    """
    Convert an integer to a Roman numeral.

    :param num: Integer value between 1 and 3999 inclusive.
    :return: A string representing the Roman numeral of the integer.
    """

    roman_dict = {
        1:"I", 4:"IV" , 5:"V", 9:"IX" , 10:"X", 40:"XL", 50:"L",90:"XC",
        100:"C",400:"CD", 500:"D",
        900:"CM", 1000:"M"
    }

    result=""
    for value in sorted(roman_dict.keys(),reverse=True):
        while num>= value:
            result+=roman_dict[value]
            num=num-value


    return result

