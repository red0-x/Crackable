# # #Crackable? AI Password Analyzer.

# # from flask import Flask,render_template, request, redirect

# # from utils import *




# # app = Flask(__name__)




# # @app.route('/', methods =["GET", "POST"])


# # def CrackableMain(methods=['GET']):
# #  if request.method == "POST":
    
# #     password = request.form.get("Password")
    
# #     try:
# #      hashes = request.form.get("dropdown")
# #     except Exception:
# #       print('NO Dropdown!') 
# #     try:
# #      hashes = request.form.get("Hashes")
# #     except Exception:
# #       print('NO Dropdown!')   
    
   
 

# #     u = utility()

# #       #  u.cracktime(crackpassword=password, hps=  hashes)
# #     response = u.cracktime(crackpassword=password, hps=hashes)
# #     parsed = response.split(" ")
# #     cracked = parsed[0]
# #     time = parsed[1]
# #     try:
# #      crackfast = parsed[2]
# #     except Exception:
# #       print('no crackfast! password insecure!')

    
# #     if (response):
# #      print(response)
# #     crackable = (f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating new password!')
# #     secure = (f'Good Job! Your password is secure and could be cracked in {cracked} {time}!')

# #     if crackfast == None:
# #      return redirect('/secure.html')
# #     else:
# #      return redirect('/cracked')
  
 
# #  return render_template("index.html")


# # @app.route('/password-generator', methods =["GET", "POST"])

# # def PasswordGen():
# #    if request.method == "POST":
# #     length = request.form.get("lenght")
# #     lchars = request.form.get("lchars")
# #     uchars = request.form.get("uchars")
# #     nums = request.form.get("nums")
# #     symbols = request.form.get("symbols")
    
# #     password = utility.GeneratePassword(length=length,lchars=lchars,uchars=uchars,nums=nums,symbols=symbols)
# #     return password

    

 

# # @app.route('/advanced', methods =["GET", "POST"])


# # def Advanced():
# #  if request.method == "POST":
# #     password = request.form.get("Password")
# #     hashes = request.form.get("Hashes")
    
# #     u = utility()
# #    #  u.cracktime(crackpassword=password, hps=  hashes)
# #     response = u.cracktime(crackpassword=password, hps=hashes)
# #     print(response)
# #     return str(response)



# #  return render_template("advanced.html")


# # @app.route('/secure', methods =['GET'])
# # def secure():
# #   return render_template('secure.html')

# # @app.route('/crackable', methods =['GET'])
# # def crackable():
# #  return render_template('cracked.html')


 
# # if __name__ == '__main__':
# #    app.run()



# from flask import Flask, render_template, request, redirect
# from utils import utility

# app = Flask(__name__)

# @app.route('/', methods=["GET", "POST"])
# def CrackableMain():
#     if request.method == "POST":
        
#         password = request.form.get("Password")
#         hashes = request.form.get("dropdown")
#         if password == None:
#             return render_template('password-generator.html', error="Invalid input. Please enter a Password.")
#         if hashes == None
#             return render_template('index.html', error="Invalid input. Please enter a Password.")
#         if hashes != int:
#             return render_template('index.html', error="Invalid input. Please enter a Password.")

#         if not hashes:
#             print('No Dropdown!')

#         u = utility()
#         response = u.cracktime(crackpassword=password, hps=hashes)
#         parsed = response.split(" ")
#         cracked, time = parsed[0], parsed[1]

#         try:
#             crackfast = parsed[2]
#         except IndexError:
#             print('No crackfast! Password insecure!')

#         if response:
#             print(response)

#         crackable = f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!'
#         secure = f'Good Job! Your password is secure and could be cracked in {cracked} {time}!'

#         if crackfast is None:
          
#           return render_template("secure.html", response=secure)
#         else:
#           return render_template("cracked.html", response=crackable)
        
#     return render_template("index.html")


# @app.route('/password-generator', methods=["POST", "GET"])
# def PasswordGen():
#     if request.method == "POST":
#         length = int(request.form['length'])
#         lchars = 'lchars' in request.form
#         uchars = 'uchars' in request.form
#         nums = 'nums' in request.form
#         symbols = 'symbols' in request.form

#         if length < 1:
#             return render_template('password-generator.html', error="Invalid input. Please enter a valid length.")

#         generated_password = utility.GeneratePassword(length, lchars, uchars, nums, symbols)
#         return render_template('password-generator.html', password=generated_password)
#     else:
#         return render_template('password-generator.html')



# @app.route('/advanced', methods=["POST"])
# def Advanced():
#     password = request.form.get("Password")
#     hashes = request.form.get("Hashes")
#     u = utility()
#     response = u.cracktime(crackpassword=password, hps=hashes)
#     print(response)
#     return str(response)



# if __name__ == '__main__':
#     app.run()


from flask import Flask, render_template, request, redirect
from utils import utility

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def CrackableMain():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("dropdown")

        if password is None:
            return render_template('index.html', error="Invalid input. Please enter a password.")
        
        if hashes is None:
            return render_template('index.html', error="Invalid input. Please select a hash type.")
        
        # Ensure hashes is an integer
        try:
            hashes = int(hashes)
        except ValueError:
            return render_template('index.html', error="Invalid input. Please select a valid hash type.")
        
        u = utility()
        response = u.cracktime(crackpassword=password, hps=hashes)
        parsed = response.split(" ")
        cracked, time = parsed[0], parsed[1]

        try:
            crackfast = parsed[2]
        except IndexError:
            print('No crackfast! Password insecure!')

        if response:
            print(response)

        crackable = f'Crackable! Your password could be cracked in {cracked} {time}! I recommend generating a new password!'
        secure = f'Good Job! Your password is secure and could be cracked in {cracked} {time}!'

        if crackfast is None:
            return render_template("secure.html", response=secure)
        else:
            return render_template("cracked.html", response=crackable)
        
    return render_template("index.html")

@app.route('/password-generator', methods=["POST", "GET"])
def PasswordGen():
    if request.method == "POST":
        length = int(request.form['length'])
        lchars = 'lchars' in request.form
        uchars = 'uchars' in request.form
        nums = 'nums' in request.form
        symbols = 'symbols' in request.form

        if length < 1:
            return render_template('password-generator.html', error="Invalid input. Please enter a valid length.")
        u = utility()
        generated_password = u.GeneratePassword(length, lchars, uchars, nums, symbols)
        return render_template('password-generator.html', password=generated_password)
    else:
        return render_template('password-generator.html')

@app.route('/advanced', methods=["POST", "GET"])
def Advanced():
    if request.method == "POST":
        password = request.form.get("Password")
        hashes = request.form.get("Hashes")
        
        u = utility()
        response = u.cracktime(crackpassword=password, hps=hashes)
        print(response)
        return str(response)

    return render_template("advanced.html")

if __name__ == '__main__':
    app.run()

