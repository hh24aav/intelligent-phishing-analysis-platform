from flask import Flask
from flask import render_template
from flask import request

from services.url_analyser import analyse_url
from services.risk_engine import calculate_risk

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        url = request.form["url"]

        reasons = analyse_url(url)

        score, level = calculate_risk(
            reasons
        )

        result = f"""
        <h2>Analysis Result</h2>

        Risk Score:
        {score}/100

        <br><br>

        Risk Level:
        {level}

        <br><br>

        Reasons:

        <br>

        {'<br>'.join(reasons)}
        """

    return render_template(
        "index.html",
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)