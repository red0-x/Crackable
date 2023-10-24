from flask import Flask, render_template, request, flash
import os
from dotenv import load_dotenv
from utils import utility

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.secret_key = SECRET_KEY

@app.route('/', methods=['GET', 'POST'])
def crackable_main():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("Dropdown")

        u = utility()
        response = u.cracktime(crackpassword=password, hps=hashes)
        parsed = response.split(" ")
        cracked = parsed[0]
        time = parsed[1]
        try:
            crackfast = parsed[2]
        except Exception:
            print('no crackfast! password insecure!')

        if response:
            print(response)
        
        crackable = f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!'
        secure = f'Good Job! Your password is secure and could be cracked in {cracked} {time}!'

        if crackfast is None:
            return render_template('secure.html', response=secure)
        else:
            return render_template('cracked.html', response=crackable)

    return render_template("index.html")

@app.route('/password-generator', methods=["POST", "GET"])
def password_gen():
    if request.method == "POST":
        passwordlength = int(request.form['length'])
        lchars = 'lchars' in request.form
        uchars = 'uchars' in request.form
        nums = 'nums' in request.form
        symbols = 'symbols' in request.form

        if passwordlength < 1:
            flash("Invalid input. Please enter a valid length.", 'error')
            return render_template('password-generator.html')

        generated_password = utility.GeneratePassword(passwordlength, lchars, uchars, nums, symbols)  # The arguments should not have 'passwordlength=', etc.
        flash("Password generated successfully!", 'success')
        return render_template('password-generator.html', output=generated_password)
    return render_template('password-generator.html')
    

@app.route('/advanced', methods=["GET", "POST"])
def advanced():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("Dropdown")
        try:
            hashes = request.form.get("Hashes")
        except Exception:
            print('NO Hashes!')

        u = utility()
        response = u.cracktime(crackpassword=password, hps=hashes)
        parsed = response.split(" ")
        cracked = parsed[0]
        time = parsed[1]
        try:
            crackfast = parsed[2]
        except Exception:
            print('no crackfast! password insecure!')

        if response:
            print(response)
        
        crackable = f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!'
        secure = f'Good Job! Your password is secure and could be cracked in {cracked} {time}!'

        if crackfast is None:
            return render_template('secure.html', response=secure)
        else:
            return render_template('cracked.html', response=crackable)

    return render_template("advanced.html")

if __name__ == '__main__':
    app.run()
