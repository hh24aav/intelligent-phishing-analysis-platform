def analyse_url(url):

    reasons = []

    if len(url) > 30:
        reasons.append("Long URL")

    if "-" in url:
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

            reasons.append(
                f"Suspicious keyword: {word}"
            )

    return reasons