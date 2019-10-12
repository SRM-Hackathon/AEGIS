#Author Name - Imaya Bharathi
#Date - 11-10-2019 -  12-10-2019
#purpose - sample flask app to keep the container running
from flash import Flash 
app =Flash(__name__)

@app.route("/")
def honeypot():
    return('Hi from honeypot!')

if __name__=="main":
    app.run(debug=True,port=2222)     
