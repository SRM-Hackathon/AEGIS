#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - For Running Flask Server

from flask import Flask,render_template,request,jsonify
import urllib3
urllib3.disable_warnings()

from flask_content.vault_deploy import (create_user,on_page_load,authenticate_user_pass)
app = Flask(__name__)
count = 0
@app.route("/")
def index():
    return render_template("register.html")


@app.route('/process', methods=['POST'])
def process():
    if globals() ["count"] == 0:
        on_page_load()
        globals() ["count"] +=1
    Confirmpassword = request.form['Confirmpassword']
    
    email = request.form['email']
    name = request.form['name']
    if name and email and Confirmpassword:
        if Confirmpassword != name:
            return jsonify({'error' : "Password doesn't match"})
        print(Confirmpassword,"*****************")
        client_token=""
        print(name,email)
        try:
            response = create_user(email,name)
            print(response)

            if response ==200:
                try:
                    client_token = authenticate_user_pass(email,name)
                except Exception as e:
                    print(e)
                if client_token:
                    return jsonify({"client_token":str("The vault generated token is "+client_token)})
                else:
                    return jsonify({"error":"client authentication failed"})
            else:
                return jsonify({"error":"User is not created"})
        except Exception as e:
            print(e)
    return jsonify({'error' : 'Missing data'})

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    name = request.form['name']
    client_token=""
    if name and email:
        try:
            client_token = authenticate_user_pass(email,name)
        except Exception as e:
            print(e)
        print(client_token,"**********")
        print(client_token)
        if client_token:
            return jsonify({"client_token":str("The vault generated token is "+client_token)})
        else:
            return jsonify({"error":"client authentication failed"})
    else:
        return jsonify({"error":"User is not created"})

    return jsonify({'error' : 'Missing data!'})


if __name__ == "__main__":
    app.run(debug=True)     
