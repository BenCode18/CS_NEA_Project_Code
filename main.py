from flask import Flask, render_template

app = Flask(__name__)

@app.route("/home")
def websiteHomePage():
    return render_template("website_home_page.html")

@app.route("/")
def melodyBuilder():
    return render_template("melody_builder.html")

if __name__ == "__main__":
    app.run(debug=True)