def calculate_turbulence_score(Wind_Shear,Wind_Speed_2,Wind_Speed_Change,Temperature_Change,Altitude_2,Mach_Number):
    score=0

    #wind shear
    if Wind_Shear>=0.005:
        score+=2
    elif Wind_Shear>=0.002:
        score+=1
    else:
        score+=0

    #wind speed
    if Wind_Speed_2>=25:
        score+=3
    elif Wind_Speed_2>=15:
        score+=2
    else:
        score+=1

    #temperature change
    if Temperature_Change>=20:
        score+=3
    elif Temperature_Change>=10:
        score+=2
    else:
        score+=1

    #wind speed change
    if Wind_Speed_Change>=6:
        score+=3
    elif Wind_Speed_Change>=3:
        score+=2
    else:
        score+=1

    #Mach number
    if Mach_Number>=0.9:
        score+=3
    elif Mach_Number>=0.6:
        score+=2
    else:
        score+=1

    #Altitude
    if Altitude_2>=10000:
        score+=3
    elif Altitude_2>=5000:
        score+=2
    else:
        score+=1

    return score

