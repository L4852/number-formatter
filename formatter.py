table = {
    1E3: 'K',
    1E6: 'M',
    1E9: 'B',
    1E12: 'T',
    1E15: 'Q'
}


def format_number(num: int, fraction_rounding=1, print_result=False) -> str:
    """
    Takes in an integer and returns an abbreviated form of the number, similar to the format used for subscriber counts.
    :param num: An integer less than 999 quadrillion.
    :param fraction_rounding: Number of decimal places to round to.
    :param print_result: Whether to print the result or not.
    :return: Returns a string of the formatted number.
    """
    if num > 1E18 - 1:
        print("Number was larger than the max supported unit, returning original number.")
        return str(num)

    final_string = ""
    for scale in table:
        if num >= scale:
            marker_length = len(str(int(scale)))
            scaled_num = num / 10 ** (marker_length - 1)
            final_string = f"{round(scaled_num, fraction_rounding)}{table[scale]}"
    if not final_string:
        final_string = str(num)

    if print_result:
        print(final_string)

    return final_string
