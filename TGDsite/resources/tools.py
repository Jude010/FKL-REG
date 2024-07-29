
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
    internal = ramp['internal']
    rise = ramp['rise']
    max_going = '5'

    if domestic != domestic :
        if internal == "external":
            # external non domestic

            if rise <= 166 :
                max_going = '2'
            elif rise <= 333 :
                max_going = '5'
            else :
                max_going = '10'


    

    return max_going
