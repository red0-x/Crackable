import re
import random


class utility:

    def __init__(self) -> None:
        pass

    def cracktime(self, crackpassword, hps):
        entropy = 0
        crack_speed = int(hps)

        policies = {
            'Uppercase characters': 0,
            'Lowercase characters': 0,
            'Special characters': 0,
            'Numbers': 0,
        }

        entropies = {
            'Uppercase characters': 26,
            'Lowercase characters': 26,
            'Special characters': 33,
            'Numbers': 10,
        }

        password = str(crackpassword)
        pass_len = len(password)

        for char in password:
            if re.match("[0-9]", char):
                policies["Numbers"] += 1
            elif re.match("[a-z]", char):
                policies["Lowercase characters"] += 1
            elif re.match("[A-Z]", char):
                policies["Uppercase characters"] += 1
            else:
                policies["Special characters"] += 1

        for policy in policies:
            if policies[policy] > 0:
                entropy += entropies[policy]

        time_ = "seconds"
        cracked = (entropy ** pass_len) / crack_speed

        if cracked > 60:
            cracked /= 60
            time_ = "minutes"
        if cracked > 60:
            cracked /= 60
            time_ = "hours"
        if cracked > 24:
            cracked /= 24
            time_ = "days"
        if cracked > 365:
            cracked /= 365
            time_ = "years"
        if time_ == "years" and cracked > 100:
            cracked /= 100
            time_ = "centuries"
        if time_ == "centuries" and cracked > 1000:
            cracked /= 1000
            time_ = "millennia"

        crackfastt = time_ in ("seconds", "minutes", "hours", "days")
        return f"{int(cracked)} {time_} {crackfastt}"

    @staticmethod
    def GeneratePassword(length, lchars, uchars, nums, symbols):
        uuchars = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
        llchars = list("abcdefghijklmnopqrstuvwxyz")
        nnums = list("1234567890")
        ssymbols = list("!@$#?&")

        total = []

        if uchars:
            total.extend(uuchars)
        if lchars:
            total.extend(llchars)
        if nums:
            total.extend(nnums)
        if symbols:
            total.extend(ssymbols)

        return ''.join(random.choices(total, k=length))
