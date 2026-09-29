def classify_risk(score):
    if score <= 7:
        return "LOW"
    elif score <= 10:
        return "MODERATE"
    else:
        return "HIGH"
