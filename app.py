from src.logger import logging


from flask import *
from wtforms import SubmitField
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename
from wtforms.validators import InputRequired
import os

    
app = Flask(__name__)
app.config['SECRET_KEY'] = 'a random string'
app.config['UPLOAD_FOLDER'] = "static/files"

class uploadFile(FlaskForm):
    file = FileField("File", validators=[InputRequired()])
    submit = SubmitField("Upload File")

@app.route("/", methods = ['GET', 'POST'])
@app.route("/home", methods = ['GET', 'POST'])
def home():
    form = uploadFile()
   
    if form.validate_on_submit():
        f = form.file.data
        filename = secure_filename(f.filename)                
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        f.save(file_path)
        return redirect(url_for('home'))
    
        
    return render_template('home.html', form=form)


@app.route("/EDA")
def about():
    return render_template('EDA.html')


if __name__=="__main__":
    app.run(debug=True, port=8501)