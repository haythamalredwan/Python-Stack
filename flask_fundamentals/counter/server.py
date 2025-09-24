from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'hello'

@app.route('/')
def counter():
    if 'count' not in session:
        session['count'] = 0
    session['count'] += 1
    return render_template("index.html", count = session['count'])

@app.route('/add2')
def add2():
    session['count'] += 2
    return render_template("index.html", count = session['count'])     

@app.route('/destroy_session')
def reset():
    session.pop('count')
    return redirect('/')
    
if __name__ == "__main__":
    app.run(debug=True)