#Crackable? AI Password Analyzer.

from flask import Flask,render_template, request, redirect

from utils import *




app = Flask(__name__)




@app.route('/', methods =["GET", "POST"])


def CrackableMain(methods=['GET']):
 if request.method == "POST":
    password = request.form.get("Password")
    hashes = request.form.get("dropdown")
    
   
 

    u = utility()

      #  u.cracktime(crackpassword=password, hps=  hashes)
    response = u.cracktime(crackpassword=password, hps=hashes)
    print(response)
    return str(response)
  
 
 return render_template("index.html")


@app.route('/password-generator', methods =["GET", "POST"])

def PasswordGen():
   if request.method == "POST":
    length = request.form.get("lenght")
    lchars = request.form.get("lchars")
    uchars = request.form.get("uchars")
    nums = request.form.get("nums")
    symbols = request.form.get("symbols")
    
    password = utility.GeneratePassword(length=length,lchars=lchars,uchars=uchars,nums=nums,symbols=symbols)
    return password

    

 

@app.route('/advanced', methods =["GET", "POST"])


def Advanced(methods=['GET']):
 if request.method == "POST":
    password = request.form.get("Password")
    hashes = request.form.get("Hashes")
    
    u = utility()
   #  u.cracktime(crackpassword=password, hps=  hashes)
    response = u.cracktime(crackpassword=password, hps=hashes)
    print(response)
    return str(response)



 return render_template("advanced.html")

 


 
if __name__ == '__main__':
   app.run()