
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
                temp = interp_slope(int(rise))
                max_slope = '1:' + str(temp)
                min_going = temp - 10
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

def interp_slope( rise ):
    print(str(rise) + " test")
    if rise == None:
        rise = 1
    elif rise == 1000:
        rise = 1
    else:
        rise = float(rise)
    
    slope = -10000/(rise - 1000)

    slope= int(slope)

    return slope