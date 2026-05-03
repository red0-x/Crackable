from flask import Flask, render_template, request, flash
import os
from utils import utility
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') or os.urandom(24)


def _crack_result(password, hps):
    u = utility()
    response = u.cracktime(crackpassword=password, hps=int(hps))
    parsed = response.split(" ")
    cracked, time_ = parsed[0], parsed[1]
    crackfast = len(parsed) > 2 and parsed[2] == "True"
    return cracked, time_, crackfast


@app.route('/', methods=['GET', 'POST'])
def crackable_main():
    try:
        if request.method == "POST":
            password = request.form.get("Password")
            hashes = request.form.get("Dropdown")
            cracked, time_, crackfast = _crack_result(password, hashes)
            if crackfast:
                return render_template('cracked.html', response=f'Crackable! Your password could be cracked in {cracked} {time_}! I recommend generating a new password!')
            return render_template('secure.html', response=f'Good Job! Your password is secure and could be cracked in {cracked} {time_}!')
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
            cracked, time_, crackfast = _crack_result(password, hashes)
            if crackfast:
                return render_template('cracked.html', response=f'Crackable! Your password could be cracked in {cracked} {time_}! I recommend generating a new password!')
            return render_template('secure.html', response=f'Good Job! Your password is secure and could be cracked in {cracked} {time_}!')
        return render_template("advanced.html")
    except Exception:
        flash("You Entered a Invalid Input, Try Again")
        return render_template('advanced.html')


if __name__ == '__main__':
    app.run(debug=True)
