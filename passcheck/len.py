def passlen(mpass):
    if len(mpass) >= 8:
        return "Password length is greater than 8 characters"
    else:
        return "Password is weak"
