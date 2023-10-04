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
     
    return u.cracktime(crackpassword=password, hps=hashes)


 return render_template("index.html")

 


 
if __name__ == '__main__':
   app.run()