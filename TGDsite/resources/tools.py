
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
    part_m = ramp['part_m']
    rise = ramp['rise']
    internal = ramp['inside']
    min_going = '5'
    max_slope = '1:20'

    
    if part_m :
        if domestic != 'domestic' :
            # external non domestic part m

            if int(rise) <= 166 :
                min_going = '2'
                max_slope = '1:12'
            else:
                min_going = interp_going(rise)
                max_slope = '1:' + str( 10 + min_going)
        else :
            #external domestic part m

            if int(rise)*12 < 5000 :
                min_going = float(int(rise)*12/1000)
                max_slope = '1:12'
            else : 
                min_going = float(int(rise)*20/1000)
                max_slope = '1:15'
            

    else :
        # all nom part m

        if  int(rise)*12 < 10000 :
            min_going = float(int(rise)*12/1000)
            max_slope = "1:12"
        else :
            min_going = float(int(rise)*20/1000)
            max_slope = "1:20"


    

    return (min_going , max_slope)

def interp_going( rise ):
    going = -1(1000*rise)/((rise/100) + 10)

    going = int(going/1000)

    return going