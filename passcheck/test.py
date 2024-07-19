from passcheck.complexi import passcomplexity

def password_strength(mpass):
    length_score = len(mpass) / 16  # Assuming maximum length to be 16 for a full score
    length_score = min(length_score, 1)  # Ensure the length score doesn't exceed 1

    complexity_score = passcomplexity(mpass) / 4  # There are 4 complexity criteria
    complexity_score = min(complexity_score, 1)  # Ensure the complexity score doesn't exceed 1

    strength_percentage = (length_score * 50) + (complexity_score * 50)

    return strength_percentage


def is_password_in_dictionary(password):
    with open("passcheck/rockyou.txt", "r") as file:
        dictionary_words = file.read().splitlines()
    for word in dictionary_words:
        if word.lower() == password.lower():
            return True
    return False


def crack_time(mpass):
    import math

    sym = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "|", "{", "}", "/", "?", "<", ">", "[", "]"]

    pool_size = 0
    if any(char.isupper() for char in mpass):
        pool_size += 26
    if any(char.islower() for char in mpass):
        pool_size += 26
    if any(char.isdigit() for char in mpass):
        pool_size += 10
    symbol_count = sum(char in sym for char in mpass)
    if symbol_count >= 2:
        pool_size += len(sym)

    possible_combinations = pool_size ** len(mpass)
    attempts_per_second = 1e6  # Assumption: 1 million attempts per second

    seconds = possible_combinations / attempts_per_second
    minutes = seconds / 60
    hours = minutes / 60
    days = hours / 24
    years = days / 365.25  # Account for leap years

    if years > 1:
        return f"Estimated time to crack: {years:.2f} years"
    elif days > 1:
        return f"Estimated time to crack: {days:.2f} days"
    elif hours > 1:
        return f"Estimated time to crack: {hours:.2f} hours"
    elif minutes > 1:
        return f"Estimated time to crack: {minutes:.2f} minutes"
    else:
        return f"Estimated time to crack: {seconds:.2f} seconds"
