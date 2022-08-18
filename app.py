import sys
from flask import Flask
from housing.logger import log
from housing.exception import HousingException

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def home():
    try:
        # raise Exception("Here the testing is going on...")
        a = 3/0
        log.info(a)
    except Exception as e:
        housing = HousingException(e, sys)
        log.info(housing.error_message)
        log.info("Home page successfully created")
    return "<h2 align='center' style='color:red'>The project representing the ML Pipeline flows. Thank you!</h2>"


if __name__ == "__main__":
    app.run(debug=True)