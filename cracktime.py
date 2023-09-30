from getpass import getpass
import sys
import re

def cracktime(crackpassword = str, hps = int):
    entropy = 0
    crack_speed = hps # Default

    if len(sys.argv) > 1:
        if sys.argv[1].isdigit():
            crack_speed = int(sys.argv[1])

    policies = {'Uppercase characters': 0,
                'Lowercase characters': 0,
                'Special characters': 0,
                'Numbers': 0}

    entropies = {'Uppercase characters': 26,
                'Lowercase characters': 26,
                'Special characters': 33,
                'Numbers': 10}

   
    print("Based on password cracking at: {:,d} MH/s.\n".format(int(crack_speed/1000000))) # Hashes/second to MH/s

    password = crackpassword
    pass_len = len(password)

    for char in password:

        if re.match("[0-9]", char):
            policies["Numbers"] += 1

        elif re.match("[a-z]", char):
            policies["Lowercase characters"] += 1

        elif re.match("[A-Z]", char):
            policies["Uppercase characters"] += 1

        else: # elif re.match("[\[\] !\"#$%&'()*+,-./:;<=>?@\\^_`{|}~]", char): # This regex can be used, but everything else should be considered special char
            policies["Special characters"] += 1

    del password # Remove password from memory

    

    for policy in policies.keys():

        num = policies[policy] if policies[policy] > 0 else '-' # Handle missing policies

        if policies[policy] > 0:
            entropy += entropies[policy]

  

    # Calculate the time to crack
    time_ = "hours"
    cracked = ((entropy**pass_len) / crack_speed) / 60 # Hours in seconds

    if cracked > 60:
        cracked = cracked / 60
        time_ = "minutes"
        
    if cracked > 24:
        cracked = cracked / 24
        time_ = "days"

    if cracked > 365:
        cracked = cracked / 365
        time_ = "years"

    if time_ == "years" and cracked > 100:
        cracked = cracked / 100
        time_ = "centuries"

    if time_ == "centuries" and cracked > 1000:
        cracked = cracked / 1000
        time_ = "millennia"
    result2 = ("Based on password cracking at: {:,d} MH/s.\n".format(int(crack_speed/1000000)))
    result1 = ("Time to crack password:   {:,.2f} {}".format(cracked, time_))
    return(str(result1+"   "+result2))
result = cracktime(crackpassword="POOPYFACE!", hps=1000000000)
print(result)