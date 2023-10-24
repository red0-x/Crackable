from getpass import getpass
import sys
import re
import random 

class utility:
 
    def __init__(self) -> None:
         pass

    
    


    def cracktime(self,crackpassword,hps):
            
            # Analyze the password  and get the time to crack the user's password
            entropy = 0
           
            crack_speed = int(hps) # Hashes Per second inputted by user

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

        

            password = str(crackpassword)
          
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
            
        
            
            result1 = ("Time to crack password:   {:,.2f} {}".format(cracked, time_))
            
            
            if time_ == "days":
                crackfastt=True
                print(cracked, time_, crackfastt)
                return(str(f"{int(cracked,)} {(time_)} {crackfastt}"))   
            
            if time_ == "minutes":
                crackfastt=True
                print(cracked, time_, crackfastt)
                return(str(f"{int(cracked,)} {(time_)} {crackfastt}"))  
            
            if time_ == "hours":
                crackfastt=True
                print(cracked, time_, crackfastt)
                return(str(f"{int(cracked,)} {(time_)} {crackfastt}"))
            else:
                 crackfastt=False
                 return(str(f"{int(cracked,)} {(time_)} {crackfastt}"))
                



            


    def GeneratePassword(length,lchars,uchars,nums,symbols,self):
            
            uuchars = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
            llchars = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","q","y","z"]
            nnums = ["1","2","3","4","5","6","7","8","9","0"]
            ssymbols = ["!","@","$","#","?","&"]
            
            passwd = []

            total = []

            if uchars == True:

                total.extend(uuchars)
                

                
            if lchars == True:

                total.extend(llchars)

            
            if nums == True:

                total.extend(nnums)

                
            
            if symbols == True:

                total.extend(ssymbols)
                
            x = [i for i in (total)]
            random.shuffle(x)

            for i in range(length):
            
                passwd += random.choices(x)[0]  
                passwd = ''.join(list(passwd))
                
            return passwd

            
                
            # GeneratePassword(length=11,lchars=True,uchars=True,nums=True,symbols=True)
            # cracktime(crackpassword='asdfasdfaw',hps='1000000000')


