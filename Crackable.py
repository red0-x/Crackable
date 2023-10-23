from flask import Flask, render_template, request, redirect, flash
import os
import utils 
from utils import *
from dotenv import load_dotenv
load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY')
app = Flask(__name__)
app.secret_key = SECRET_KEY


@app.route('/', methods=["GET", "POST"])
def CrackableMain():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("dropdown")

        if password is None:
            flash("Invalid input. Please enter a password.", 'error')
            return redirect(request.url)

        if hashes is None:
            flash("Invalid input. Please select a hash type.", 'error')
            return redirect(request.url)

        try:
            hashes = int(hashes)
        except ValueError:
            flash("Invalid input. Please select a valid hash type.", 'error')
            return redirect(request.url)
    return render_template('index.html')    

        # Your existing code continues...

@app.route('/password-generator', methods=["POST", "GET"])
def PasswordGen():
    if request.method == "POST":
        passwordlength = int(request.form['length'])
        lchars = 'lchars' in request.form
        uchars = 'uchars' in request.form
        nums = 'nums' in request.form
        symbols = 'symbols' in request.form

        if passwordlength < 1:
            flash("Invalid input. Please enter a valid length.", 'error')
            return render_template('password-generator.html')

        generated_password = utility.GeneratePassword(passwordlength=passwordlength, lchars=lchars, uchars=uchars, nums=nums, symbols=symbols)
        flash("Password generated successfully!", 'success')
        return render_template('password-generator.html', output=generated_password)
    

    # Your existing code continues...

if __name__ == '__main__':
    app.run()



@app.route('/Advanced', methods=["GET", "POST"])
def Advanced():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("Hash")

        if password is None:
            flash("Invalid input. Please enter a password.", 'error')
            return redirect(request.url)

        if hashes is None:
            flash("Invalid input. Please select a hash type.", 'error')
            return redirect(request.url)

        try:
            hashes = int(hashes)
        except ValueError:
            flash("Invalid input. Please select a valid hash type.", 'error')
            return redirect(request.url)
    return render_template('advanced.html')    