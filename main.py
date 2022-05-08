from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def portfolio():
    return render_template('Portfolio.html')

if __name__ == "__main__":
    app.run(port=3000, debug=True)
