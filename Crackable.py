#Crackable? AI Password Analyzer.

from flask import Flask,render_template, request

from utils import utility



app = Flask(__name__)




@app.route('/', methods =["GET", "POST"])


   
def CrackableMain(methods=['GET']):
 if request.method == "POST":
    password = request.form.get("Password")
    hashes = request.form.get("Hashes")
    u = utility()
   #  u.cracktime(crackpassword=password, hps=hashes)
    try: 
     crackfastt,time_,cracked = u.cracktime(crackpassword=password, hps=hashes)
    except Exception:
       pass
    
    try:
       crackfastt,time_, = u.cracktime(crackpassword=password, hps=hashes)
    except Exception:
     pass
    
    try:
       crackfastt = u.cracktime(crackpassword=password, hps=hashes)
    except Exception:
     pass
    
    try:
       time_ = u.cracktime(crackpassword=password, hps=hashes)
    except Exception:
     pass
    

    if crackfastt == False:
      print("Your Password could be cracked in",cracked, time_,"Which means your password is Secure!")
    
    if crackfastt == True:
      print("Your Password could be cracked in",cracked, time_,"Which means your password is NOT Secure!")


 return render_template("Crackable.html")

 


 
if __name__ == '__main__':
   app.run()