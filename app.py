from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    result = ""

    if request.method == "POST":

        url = request.form["url"]

        score = 0
        reasons = []

        if len(url) > 30:
            score += 20
            reasons.append("Long URL")

        if "-" in url:
            score += 20
            reasons.append("Contains hyphens")

        suspicious_words = [
            "login",
            "verify",
            "secure",
            "account",
            "update",
            "password"
        ]

        for word in suspicious_words:
            if word in url.lower():
                score += 15
                reasons.append(f"Suspicious keyword: {word}")

        if score >= 60:
            level = "HIGH"
        elif score >= 30:
            level = "MEDIUM"
        else:
            level = "LOW"

        result = f'''
        <h2>Analysis Result</h2>

        Risk Score: {score}/100<br>
        Risk Level: {level}<br><br>

        Reasons:<br>
        {"<br>".join(reasons)}
        '''

    return f'''
    <h1>Intelligent Phishing Analysis and Detection Platform</h1>

    <form method="POST">

        <input
            type="text"
            name="url"
            placeholder="Enter URL"
            size="60">

        <button type="submit">
            Analyse
        </button>

    </form>

    <br>

    {result}
    '''

if __name__ == "__main__":
    app.run(debug=True)