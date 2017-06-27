__author__ = 'Adamlieberman'
from flask import Flask, render_template, request,flash
app = Flask(__name__)
import os
app.config['UPLOAD_FOLDER'] = 'test_images'
app.secret_key = 'blahblahuploaderblahhhh'
#index has a form that links to /classify_upload then we go below and handle what happens there and return stuff
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/classify_upload',methods=['GET','POST'])
def index2():
    if request.method == 'POST':
        f = request.files['file']
        f.filename = 'image1.png'
        f.save(os.path.join(app.config['UPLOAD_FOLDER'],f.filename))
    #imagefile.save('image1.png')
        #return '<center><h1>successful upload</h1></center>'
        message = '<center><font color="green"><h1>Successful Upload!</h1></font></center>'
        flash(message)
        return render_template('index.html')
    else:
        message = '<center><font color="red">Upload Failed Please Try Again</font></center>'
        flash(message)
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True,port=5000)