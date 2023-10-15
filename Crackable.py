#Crackable? AI Password Analyzer.

from flask import Flask,render_template, request, redirect

from utils import *



app = Flask(__name__)




@app.route('/', methods =["GET", "POST"])


def CrackableMain(methods=['GET']):
 if request.method == "POST":
    password = request.form.get("Password")
    hashes = request.form.get("dropdown")
    
    modea = request.form.get("modea")
    print(modea)
    if modea == 'True':
      redirect('/advanced')
    else:
    
      u = utility()
      #  u.cracktime(crackpassword=password, hps=  hashes)
      response = u.cracktime(crackpassword=password, hps=hashes)
      print(response)
      return str(response)
  
 
 return render_template("index.html")

 

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