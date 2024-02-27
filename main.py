from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def initialHomepage():
    return render_template("initial_homepage.html")

@app.route("/log-in/")
def logInPage():
    return render_template("log-in_page.html")

@app.route("/sign-up/")
def signUpPage():
    return render_template("sign-up_page.html")

@app.route("/melody_builder/")
def melodyBuilder():
    return render_template("melody_builder.html")

@app.route("/user_homepage/")
def userHomepage():
    return render_template("user_homepage.html")

@app.route("/piece_output/")
def pieceOutputPage():
    return render_template("piece_output_page.html")

if __name__ == "__main__":
    app.run(debug=True)




