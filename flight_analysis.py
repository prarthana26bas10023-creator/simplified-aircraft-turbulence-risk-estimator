def Calculate_Flight_Analysis(Speed,Speed_of_Sound,Wind_Speed_1,Wind_Speed_2,Altitude_1,Altitude_2):
    #Calculate Mach number
    Mach_Number=Speed/Speed_of_Sound

    #Calculate Wind Shear
    Wind_Shear=abs((Wind_Speed_2-Wind_Speed_1)/(Altitude_2-Altitude_1))

    #Determining Flight Regime
    if Mach_Number<0.8:
        Flight_Regime="Subsonic"
    elif Mach_Number<1.2:
        Flight_Regime="Transonic"
    elif Mach_Number<5:
        Flight_Regime="Supersonic"
    else:
        Flight_Regime="Hypersonic"

    return{"Mach_Number":Mach_Number,
           "Flight_Regime":Flight_Regime,
           "Wind_Shear":Wind_Shear
    }

    