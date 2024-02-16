from flask import Flask, url_for, redirect
import settings as stg

app = Flask (__name__, static_folder=stg.PATH_STATIC )
app.config["SECRET_KEY"] = stg.SECRET_KEY

@app.route("/")
def index():
    url = url_for("static", filename="templates/index.html" )
    return redirect(url)



app.run(debug=True)