from flask import Flask, render_template, redirect, request, session, url_for
import random
app = Flask(__name__)
app.secret_key = "secret"

@app.route('/')
def start_game():
    if "number" not in session:
        session["number"] = random.randint(1,100)
        session["guesses"] = 0
        session["message"] = ""
    print("hi")
    return render_template('index.html')

@app.route('/guess', methods=["GET"])
def guess():
    session["my_guess"] = int(request.args["my_guess"])
    if session["my_guess"] == int(session["number"]):
        session["message"] = f"The number is {session['number']}!"
    elif session["my_guess"] > int(session["number"]):
        session["message"] = "Too high!"
    else:
        session["message"] = "Too low!"
    print(session["my_guess"])
    session["guesses"] += 1

    return redirect('/')

@app.route('/reset_session')
def reset_session():
    session.clear()
    return redirect('/')

if __name__ == "__main__":
    app.run(debug=True)