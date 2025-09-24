from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template("index.html")

@app.route('/result', methods=['GET','POST'])
def result():

    name = request.form['name']
    gender = request.form['gender']
    location = request.form['location'] 
    language = request.form['language'] 
    comment = request.form['comment']

    return render_template("result.html",
    name = name,gender = gender, language = language, location = location, comment = comment) 

if __name__ == "__main__":
    app.run(debug=True)