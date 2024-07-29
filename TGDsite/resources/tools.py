
#tool to calculate minimum flights given a stari object conveted to a dict and if the project is private or public
def calc_flights(stairs, domestic):
    min_flights = ''

    if domestic == 'domestic' :
        if stairs['part_m'] == True :
            temp = float(stairs['rise']) / float(1800)
        else:
            temp = float(stairs['rise']) / float(3520)
    else:
        if stairs['part_m'] == True :
            if stairs['inside'] == 'internal':
                temp = float(stairs['rise']) / float(2880)
            else:
                temp = float(stairs['rise']) / float(3240)
        else:
            if stairs['inside'] == 'internal':
                temp = float(stairs['rise']) / float(2880)
            else:
                temp = float(stairs['rise']) / float(1800)
            
    # round temp up accounting for bit inaccuracy
    if (temp - int(temp)) > 0.0001:
        return int(temp) + 1
    else:
        return temp   
    

def calc_slope(ramp , domestic):
    internal = ramp['inside']
    rise = ramp['rise']
    max_going = '5'
    max_slope = '1/20'

    if domestic != domestic :
        if internal == "external":
            # external non domestic

            if rise <= 166 :
                max_going = '2'
                max_slope = '1/12'
            else:
                max_going = interp_going(rise)
                max_slope = '1/' + str( 10 + max_going)


    

    return (max_going , max_slope)

def interp_going( rise ):
    going = - (1000*rise)/((rise/100) + 10)

    going = int(going/1000)

    return going