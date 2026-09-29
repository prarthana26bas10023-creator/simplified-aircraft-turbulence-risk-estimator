#This is an educational model only,not an operational aviation turbulence prediction system.

from input_handler import get_inputs
from validation import validate_inputs
from atmosphere import calculate_atmosphere
from flight_analysis import Calculate_Flight_Analysis 
from scoring import calculate_turbulence_score
from risk import classify_risk 
from output import display_results

def main( ):
    print( "=======SIMPLIFIED AIRCRAFT TURBULENCE RISK ESTIMATOR=======" )

    data=get_inputs( )     #user inputs

    error=validate_inputs(data)     #validate input

    if error:
      print(error)
      return

    #atmospheric conditions
    atmosphere=calculate_atmosphere(data["Altitude_1"])

    #flight related values
    flight=Calculate_Flight_Analysis(
        data["Speed"],atmosphere["Speed_of_Sound"],
        data["Wind_Speed_1"],data["Wind_Speed_2"],
        data["Altitude_1"],data["Altitude_2"]
)

    #turbulence score
    score=calculate_turbulence_score(
       flight["Wind_Shear"],
       data["Wind_Speed_2"],
       data["Wind_Speed_Change"],
       data["Temperature_Change"],
       data["Altitude_2"],
       flight["Mach_Number"]
    )

    #determining risk level
    risk= classify_risk(score)

    #display final results
    display_results(
        data,
        atmosphere,
        flight,
        score,
        risk
)

if __name__ == '__main__':
    main( )
