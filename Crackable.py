from flask import Flask, render_template, request, flash
import os
from utils import utility  # Import the utility class or module
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def crackable_main():
   try:
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("Dropdown")


        u = utility()  # Make sure 'utility' is correctly defined
        response = u.cracktime(crackpassword=password, hps=int(hashes))
        parsed = response.split(" ")
        cracked = parsed[0]
        time = parsed[1]
        crackfast = None  # Initialize crackfast

        if len(parsed) > 2:
            try:
                crackfast = parsed[2]
            except ValueError:
                print('no crackfast! password insecure')

        if response:
            print(response)

        if crackfast is None:
            return render_template('secure.html', response=f'Good Job! Your password is secure and could be cracked in {cracked} {time}!')
        else:
            return render_template('cracked.html', response=f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!')

    return render_template("index.html")
   
   except Exception:
        
         flash("You Entered a Invalid Input, Try Again")
         return render_template('index.html') 
      
@app.route('/password-generator', methods=["POST", "GET"])
def password_gen():

    try:
        if request.method == "POST":
            length = int(request.form['length'])
            lchars = 'lchars' in request.form
            uchars = 'uchars' in request.form
            nums = 'nums' in request.form
            symbols = 'symbols' in request.form

            if length < 1:
                return render_template('password-generator.html', error="Invalid input. Please enter a valid length.")

            generated_password = utility.GeneratePassword(length, lchars, uchars, nums, symbols)
            return render_template('password-generator.html', password=generated_password)
        else:
            return render_template('password-generator.html')
    except Exception:    
     flash("You Entered a Invalid Input, Try Again")
     return render_template('password-generator.html')


@app.route('/advanced', methods=["GET", "POST"])

def advanced():
  try: 
    if request.method == "POST":
        password = request.form.get("Password")

       
        hashes = request.form.get("Hashes")

        u = utility()  # Make sure 'utility' is correctly defined
        response = u.cracktime(crackpassword=password, hps=int(hashes))
        parsed = response.split(" ")
        cracked = parsed[0]
        time = parsed[1]
        crackfast = None

        if len(parsed) > 2:
            try:
                crackfast = parsed[2]

            except ValueError:
                app.logger.error('No crackfast! Password insecure')

        if response:
            app.logger.info(response)

        if crackfast is None:
            return render_template('secure.html', response=f'Good Job! Your password is secure and could be cracked in {cracked} {time}!')
        else:
            return render_template('cracked.html', response=f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!')
    return render_template("advanced.html")

  except Exception:
         flash("You Entered a Invalid Input, Try Again")
         return render_template('advanced.html')

if __name__ == '__main__':
    app.run(debug=True)
