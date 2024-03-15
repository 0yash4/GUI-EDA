from flask import *
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/EDA")
def about():
    return render_template('EDA.html')


if __name__=="__main__":
    app.run(debug=True, port=8501)