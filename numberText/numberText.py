import math

single_digit = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ten_to_five_zero = ["", "ten", "twenty", "thirty", "forty", "fifty"]
ten_to_one_five = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen"]

scale_magnitudes_list = ["", "thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion",
                         "septillion", "octillion"]


def num_to_text(n):
    if n > 10 ** 30:
        return "too large"
    if n < 1000:
        return three_most_significant_digits_to_text(n)
    else:
        scale_magnitude = math.floor(math.log(n, 1000))
        three_most_sf = n // (10 ** (scale_magnitude * 3))
        the_rest = n % (10 ** (scale_magnitude * 3))

        former_part = f"{three_most_significant_digits_to_text(three_most_sf)} " \
                      f"{scale_magnitudes_list[scale_magnitude]}{s_or_no_s(three_most_sf)}"
        latter_part = (", " if the_rest != 0 else "") + f"{num_to_text(the_rest)}"

        return f"{former_part}{latter_part}"


def three_most_significant_digits_to_text(n):
    if n < 10 and n != 0:
        return single_digit[n]
    elif n < 100:
        return two_digits_to_text(n)
    elif n < 1000:
        return three_digits_to_text(n)


def three_digits_to_text(n):
    hundredth_digit = n // 100
    two_last_digits = n % 100
    former_part = single_digit[hundredth_digit]
    latter_part = ""
    if two_last_digits < 10:
        if two_last_digits != 0:
            latter_part = f" and {single_digit[two_last_digits]}"
    else:
        latter_part = f" and {two_digits_to_text(two_last_digits)}"
    return f"{former_part} hundred{s_or_no_s(hundredth_digit)}{latter_part}"


def two_digits_to_text(n):
    output = ""
    second_digit = n // 10
    first_digit = n % 10

    if second_digit == 1:
        if first_digit <= 5:
            output += ten_to_one_five[first_digit]
        else:
            output += single_digit[first_digit] + ("teen" if first_digit != 8 else "een")
    else:
        if second_digit <= 5:
            output += ten_to_five_zero[n // 10]
        else:
            output += single_digit[second_digit] + ("ty" if second_digit != 8 else "y")

        if first_digit != 0:
            output += f" {single_digit[first_digit]}"
    return output


def s_or_no_s(n):
    return "s" if n >= 2 else ""
