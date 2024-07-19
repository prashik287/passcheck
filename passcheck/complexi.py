import string


def passcomplexity(mpass):
    sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "|", "{", "}", "/", "?", "<", ">", "[",
           "]"]

    has_upper = any(char.isupper() for char in mpass)
    has_lower = any(char.islower() for char in mpass)
    has_digit = any(char.isdigit() for char in mpass)
    has_multiple_symbols = sum(char in sym for char in mpass) >= 2

    complexity = sum([has_upper, has_lower, has_digit, has_multiple_symbols])

    return complexity
