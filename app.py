from flask import Flask
import pandas
import numpy

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    return "<h2 align='center' style='color:red'>The project representing the ML Pipeline flows. Thank you!</h2>"


if __name__ == "__main__":
    app.run(debug=True)