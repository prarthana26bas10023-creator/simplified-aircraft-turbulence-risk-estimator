#This is a simplied/educational woring model.It does not claim the operational aviation turbulence prediction sysytem

import math

print("-------SIMPLIFIED AIRCRAFT TURBULENCE RISK ESTIMATOR-------")


#Required inputs
Altitude_1=float(input("Enter aircraft altitude(1) (m):"))       #Intial altitude
Altitude_2=float(input("Enter aircraft altitude(2) (m):"))       #Final altitude
Speed=float(input("Enter aircraft speed (m/s):"))
Temperature_change=float(input("Enter temperature change(C):"))
Wind_speed_1=float(input("Enter initial wind speed(1)(m/s):"))   #Initial wind speed
Wind_speed_2=float(input("Enter final wind speed(2)(m/s):"))     #Final wind speed
Wind_speed_change=float(input("Enter wind speed change(m/s):"))

if Altitude_1<0 or Altitude_2<0:
    print("error:-Altitude(1) and Altitude(2) can't be negative")
    exit()

if Altitude_1==Altitude_2:
    print("error:-Altitude(1) and altitude(2) can't be the same")
    exit()

if Speed<0:
    print("error:-speed can't be negative")
    exit()

if Wind_speed_1 <0 or Wind_speed_2<0:
    print("error:- wind speed(1) and wind speed(2) can't be negative")
    exit()

#Constants
T0=288.15      #Sea-level temperature in kelvin(K)
P0=101325      #Sea-level pressure in pascal(Pa)
L=0.0065       #Temperature lapse rate(K/m)
R=287.05       #Specific gas constant(J/Kg.K)
g=9.81         #Acceleration due to gravity(m/s^2)
gamma=1.4      #Heat capacity ratio

#Calculating atmospheric temperature
Atmospheric_temperature=T0-(L*Altitude_1)

#Calculating atmospheric pressure
Atmospheric_pressure=P0*(Atmospheric_temperature/T0)**(g/(R*L))

#Calculating air density
Air_density=Atmospheric_pressure/(R*Atmospheric_temperature)

#Calculating speed of sound
Speed_of_sound=math.sqrt(gamma*R*Atmospheric_temperature)

#Calculating mach number
Mach_number=Speed/Speed_of_sound

#Calculating wind shear
Wind_shear=abs((Wind_speed_2-Wind_speed_1)/(Altitude_2-Altitude_1))


#Calculating turbulence score
score=0

if Wind_shear>=0.005:
    score+=2
elif Wind_shear>=0.002:
    score+=1
else:
    score+=0

if Wind_speed_2>=25:
    score+=3
elif Wind_speed_2>=15:
    score+=2
else:
    score+=1

if Wind_speed_change>=6:
    score+=3
elif Wind_speed_change>=3:
    score+=2
else:
    score+=1

if Temperature_change>=20:
    score+=3
elif Temperature_change>=10:
    score+=2
else:
    score+=1

if Altitude_2>=10000:
    score+=2
elif Altitude_2>=5000:
    score+=1
else:
    score+=0

if Mach_number>=0.9:
    score+=3
elif Mach_number>=0.6:
    score+=2
else:
    score+=1 

#Determining the risk factoR
if score<=7:
    risk="LOW"
elif score<=10:
    risk="MODERATE"
else:
    risk="HIGH"


#outputs(results)
print("-------RESULT-------")
print("Altitude               :",round(Altitude_2,2),"m")
print("Atmospheric Temperature:",round(Atmospheric_temperature,2),"K")
print("Atmospheric Pressure   :",round(Atmospheric_pressure,2),"Pa")
print("Air Density            :",round(Air_density,2),"Kg/m^3")
print("Speed of Sound         :",round(Speed_of_sound,2),"m/s")
print("Aircraft Speed         :",round(Speed,2),"m/s")
print("Mach Number            :",round(Mach_number,3))

#finding flight regime
if Mach_number<0.8:
    print("Flight Regime          : Subsonic")
elif Mach_number<1.2:
    print("Flight Regime          : Transonic")
elif Mach_number<5:
    print("Flight Regime          : Supersonic")
else:
    print("Flight Regime          : Hypersonic")

print("Wind Speed             :",round(Wind_speed_2,2),"m/s")
print("Wind Speed Change      :",round(Wind_speed_change,2),"m/s")
print("wind Shear             :",round(Wind_shear,3),"s^-1")
print("Turbulence Score       :",score)
print("Temperature Change     :",round(Temperature_change,2),"C")
print("Estimated Risk         :",risk)
            
