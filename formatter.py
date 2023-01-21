table = {
    1E3: 'K',
    1E6: 'M',
    1E9: 'B',
    1E12: 'T',
    1E15: 'Q'
}

def format(num) -> str:
    final_string = ""
    for scale in table:
        if num >= scale:
            marker_length = len(str(int(scale)))
            scaled_num = num / 10 ** (marker_length - 1)
            final_string = f"{round(scaled_num, 1)}{table[scale]}"
    if not final_string:
        final_string = str(num)

    return final_string