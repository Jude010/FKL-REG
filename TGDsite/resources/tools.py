
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
