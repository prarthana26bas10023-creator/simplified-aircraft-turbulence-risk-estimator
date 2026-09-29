def get_inputs():
    Altitude_1=float(input("Enter Aircraft Altitude (1)(m):"))
    Altitude_2=float(input("Enter Aircraft Altitude(2)(m):"))
    Speed=float(input("Enter Aircraft Speed(m/s):"))
    Temperature_Change=float(input("Enter Temperature Change(C):"))
    Wind_Speed_1=float(input("Enter Initial Wind Speed(1)(m/s):"))
    Wind_Speed_2=float(input("Enter Final Wind Speed(2)(m/s):"))
    Wind_Speed_Change=float(input("Enter wind speed change(m/s):"))

    return{"Altitude_1":Altitude_1,
           "Altitude_2":Altitude_2,
           "Speed":Speed,
           "Temperature_Change":Temperature_Change,
           "Wind_Speed_1":Wind_Speed_1,
           "Wind_Speed_2":Wind_Speed_2,
           "Wind_Speed_Change":Wind_Speed_Change
    }
    
