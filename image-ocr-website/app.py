from flask import Flask,render_template,url_for,request,redirect
from werkzeug.utils import secure_filename
from image_ocr import translate_text,extract_text,LANGUAGES
import os



app=Flask(__name__)

upload_folder = os.path.join('static', 'uploads')
app.config['UPLOAD'] = upload_folder

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')


@app.route('/handle_image',methods=["GET","POST"])
def handle_uploaded_image():
    if request.method=="POST":
        file=request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD'], filename))
            img = os.path.join(app.config['UPLOAD'], filename)
            return render_template('handle_image_upload.html',img=img)
    return redirect(url_for('home_page'))


@app.route('/image_ocr/<img>',methods=["GET","POST"])
def image_ocr(img):
    if request.method=="POST":
        text=extract_text(img)
        return render_template("text.html",text=text)
    return redirect(url_for("handle_uploaded_image"))


# @app.route("/translate_text")
# def translate():
#     pass

app.run(debug=True)