def is_password_strong(self, password):
    with open("rockyou.txt", "r") as file:
        dictionary_words = file.read().splitlines()
    for word in dictionary_words:
        if word.lower() in password.lower():
            return False
    return True