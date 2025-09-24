from flask import Flask, render_template

app = Flask(__name__)
app.secret_key="Hello"

@ app.route("/")
def default_board(x = 8, y = 8):
    return render_template("index.html", x = x, y = y)

@ app.route("/<int:y>")
def four_by_eight_board(x = 8, y = 4 ):
    return render_template("index.html", x = x, y = y)

@ app.route("/<int:x>/<int:y>")
def x_by_y_board(x, y):
    return render_template("index.html", x = x, y = y)

@ app.route("/<int:x>/<int:y>/<color1>/<color2>")
def colored_board(x, y, color1 , color2):
    return render_template("colored_board.html", x = x, y = y, color1 = color1, color2 = color2)


if __name__ == "__main__" :
    app.run(debug=True)
