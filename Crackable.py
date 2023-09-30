#Crackable? AI Password Analyzer.

from flask import Flask,render_template, request


app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])

def CrackableMain(methods=['GET']):
 if request.method == "POST":
    form = request.form.get("Password")
    print(form)
    return form

 return render_template("Crackable.html")

 


 
if __name__ == '__main__':
   app.run()