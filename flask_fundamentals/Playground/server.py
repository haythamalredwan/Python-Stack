from flask import Flask, render_template  

app = Flask(__name__)
app.secret_key = "Hello"

@ app.route("/play")
def three_boxes(x = 3, color = "#9fc5f8" ):
    return render_template("index.html", x = x, color = color)

@ app.route("/play/<int:x>")
def x_boxes(x, color = "#9fc5f8"):
    return render_template("index.html",x=x , color = color)

@ app.route("/play/<int:x>/<color>")
def x_color_boxes(x,color):
    return render_template("index.html",x=x , color = color)



if __name__=="__main__":   
    app.run(debug=True)    