from flask import Flask, render_template, url_for


# Create an instance of our Flask app.
app = Flask(__name__)

@app.route("/")
def index():

    # Return template and data
    return render_template("index_final.html")

@app.route("/humidity")
def humidity():

    # Return template and data
    return render_template("humidity_final.html")

@app.route("/cloudiness")
def cloudiness():

    # Return template and data
    return render_template("cloudiness_final.html")

@app.route("/windspeed")
def windspeed():

    # Return template and data
    return render_template("windspeed_final.html")

@app.route("/temperature")
def temperature():

    # Return template and data
    return render_template("temp_final.html")

@app.route("/data")
def data():

    # Return template and data
    return render_template("data_final.html")

@app.route("/comparisons")
def comparisons():

    # Return template and data
    return render_template("comparisons_final.html")


if __name__ == "__main__":
    app.run(debug=True)
