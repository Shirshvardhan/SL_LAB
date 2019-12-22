from flask import Flask,render_template,session,request,url_for

app = Flask(__name__)
app.secret_key = "secret"

@app.route("/",methods=["GET","POST"])
def index():
    try:
        balance = session["balance"]
    except KeyError:
        balance = session["balance"]=8000

    if(request.method == "GET"):
        return render_template("index.html",balance=balance,msg="WELCOME TO ATM")
    if(request.method == "POST"):
        if(request.form["action"]=="Withdraw"):

            if int(request.form["amount"])>session["balance"]:
                msg = "CANNOT WITHRAW GREATER THAN BALANCE"
                return render_template("index.html",balance=balance,msg=msg) 
            else:
                balance = balance-int(request.form["amount"])
                session["balance"] = balance
                msg = "WITHDRAW SUCCESSFUL"
                return render_template("index.html",balance=balance,msg=msg) 
        elif(request.form["action"]=="Deposit"): 
                balance = balance+int(request.form["amount"])
                session["balance"] = balance
                msg = "DEPOSIT SUCCESSFUL"
                return render_template("index.html",balance=balance,msg=msg) 
if __name__ == "__main__":
    app.run(debug=True)