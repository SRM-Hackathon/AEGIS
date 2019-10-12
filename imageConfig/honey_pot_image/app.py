from flash import Flash 
app =Flash(__name__)

@app.route("/")
def honeypot():
    return('Hi from honeypot!')

if __name__=="main":
    app.run(debug=True,port=2222)     