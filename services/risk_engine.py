def calculate_risk(reasons):

    score = len(reasons) * 15

    score = min(score, 100)

    if score >= 60:
        level = "HIGH"

    elif score >= 30:
        level = "MEDIUM"

    else:
        level = "LOW"

    return score, level