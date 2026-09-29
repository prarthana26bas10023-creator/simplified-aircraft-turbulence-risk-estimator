def validate_inputs(data):
    if data["Altitude_1"]<0 or data["Altitude_2"]<0:
        return "error:-Altitude_(1) and Altitude(2) can't be negative"

    if data["Altitude_1"]== data["Altitude_2"]:
        return "error:-Altitude(1) and Altitude(2) can't be same"

    if data["Speed"]<0:
        return"error:-Speed can't be negative"

    if data["Wind_Speed_1"]<0 or data["Wind_Speed_2"]<0:
        return"error:-Wind speed(1) and Wind speed(2) can't be negative"

    return None

    