from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def show_homepage():
    return render_template('index1.html')

if __name__ == "__main__":
    app.run(debug=True)