import math
from constants import T0,P0,L,R,g,gamma

def calculate_atmosphere(Altitude):
    Atmospheric_Temperature=T0-(L*Altitude)

    Atmospheric_Pressure=P0*(Atmospheric_Temperature/T0)**(g/(R*L))

    Air_Density=Atmospheric_Pressure/(R*Atmospheric_Temperature)

    Speed_of_Sound=math.sqrt(gamma*R*Atmospheric_Temperature)

    return{"Atmospheric_Temperature":Atmospheric_Temperature,
           "Atmospheric_Pressure":Atmospheric_Pressure,
           "Air_Density":Air_Density,
           "Speed_of_Sound":Speed_of_Sound
    }