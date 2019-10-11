from flask import Flask,render_template,request,jsonify
from flask_content.vault_deploy import (create_user,on_page_load,authenticate_user_pass)
app = Flask(__name__)
@app.route("/")
def index():
    return render_template("register.html")
    print("Getting vault credentials")
    
    # vault_response = vault_deploy()
    if vault_response != 200 :
        return "vault_doesn't recognize your key"
    else:
        return "some prompt"
  

@app.route("/register",methods=['POST'])
def register():
    print("from register *************************")
    username=request.form['reg_username']
    password=request.form['reg_password']
    print(username,password)
    # client_token = create_user(username,password)
    return render_template("register.html",client_token=jsonify(client_token))

@app.route('/process', methods=['POST'])
def process():
	username = request.form['reg_username']
	password = request.form['reg_password']
    # print(username)
	if username and password:
        print(username)
		newName = username[::-1]
		return jsonify({'name' : newName})
	return jsonify({'error' : 'Missing data!'})

@app.route('/process', methods=['POST'])
def process():
    username = request.form["nameInput"]
    password = request.form["passwordInput"]

    # password = request.form["passwordInput"]
    print(username)
    return jsonify({'error' : 'Missing data!'}) 
    password


@app.route('/process', methods=['POST'])
def process():
    #it should be load only ones 
    on_page_load()
    Confirmpassword = request.form['Confirmpassword']
    email = request.form['email']
    name = request.form['name']
    if name and email and Confirmpassword:
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
                    return jsonify({"client_token":str(client_token)})
                else:
                    return jsonify({"error":"client authentication failed"})
            else:
                return jsonify({"error":"User is not created"})
        except Exception as e:
            print(e)

    return jsonify({'error' : 'Missing data!'})

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
        print(client_token,"*****hai*****")
        print(client_token)
        if client_token:
            return jsonify({"client_token":str(client_token)})
        else:
            return jsonify({"error":"client authentication failed"})
    else:
        return jsonify({"error":"User is not created"})

    return jsonify({'error' : 'Missing data!'})


if __name__ == "__main__":
    app.run(debug=True)