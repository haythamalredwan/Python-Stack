from flask import Flask, render_template  

app = Flask(__name__)
app.secret_key = "Hello"

@app.route('/')          
def hello_world():
    return "hello world!"

@app.route('/Champion')
def champion():
    return "Champion!"

@app.route('/say/<name>')
def say_hi(name):
    return "Hi "+name+"!"

@app.route('/repeat/<count>/<word>')
def repeat_word(count, word):
   return render_template("index.html",count= int(count), word = word)

@app.errorhandler(404)
def page_not_found(error):
    return render_template("error.html", error=404)
    


if __name__=="__main__":   
    app.run(debug=True)    