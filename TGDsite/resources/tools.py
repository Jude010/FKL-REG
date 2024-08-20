
#tool to calculate minimum flights given a stari object conveted to a dict and if the project is private or public
def calc_flights(rise, domestic , part_m , inside):
    min_flights = ''

    if domestic == 'domestic' :
        if part_m == True :
            temp = float(rise) / float(1800)
        else:
            temp = float(rise) / float(3520)
    else:
        if part_m == True :
            if inside == 'internal':
                temp = float(rise) / float(1800)
            else:
                temp = float(rise) / float(1500)
        else:
            if inside == 'internal':
                temp = float(rise) / float(2880)
            else:
                temp = float(rise) / float(2880)
            
    # round temp up accounting for bit inaccuracy
    if (temp - int(temp)) > 0.0001:
        return int(temp) + 1
    else:
        return temp   
    

def calc_slope(rise , part_m , domestic):
    part_m = part_m
    rise = rise
    min_going = '5'
    max_slope = '1:20'

    
    if part_m :
        if domestic != 'domestic' :
            # non domestic part m

            if int(rise) <= 166 :
                min_going = '2'
                max_slope = '1:12'

            elif int(rise) > 500:
                float(int(rise)*20/1000)

            else:
                temp = interp_slope(int(rise))
                max_slope = '1:' + str(temp)
                min_going = temp - 10
        else :
            # domestic part m

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

    if slope - int(slope) > 0 : # round fractions up
        slope +=1
    
    slope= int(slope)

    return slope

def vaidate_gait( internal , privacy, part_m , rise , going):
    r_val = False
    g_val = False
    ga_val = False
    gait = 2*rise + going

    if privacy == 'domestic' :
        if internal == "internal" :
            if part_m == True :
                # internal domestic part m
                if rise <= 175 :
                    r_val = True

                if going >= 280 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
            else :
                # internal domestic non part_m
                if rise <= 220 :
                    r_val = True

                if going >= 220 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
        else :
            if part_m == True :
                # external domestic part m
                if rise <= 175 :
                    r_val = True

                if going >= 280 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
            else :
                # external domestic non part_m
                if rise <= 220 :
                    r_val = True

                if going >= 220 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
    else :
        if internal == "internal" :
            if part_m == True :
                # internal public part m
                if rise <= 180 and rise >= 150 :
                    r_val = True

                if going >= 250 and going <= 300 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
            else :
                # internal public non part_m
                if rise <= 190 :
                    r_val = True

                if going >= 280 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
        else :
            if part_m == True :
                # external public part m
                if rise <= 180 and rise >= 150 :
                    r_val = True

                if going >= 300 and going <= 450 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True
            else :
                # external public non part_m
                if rise <= 180 :
                    r_val = True

                if going >= 280 : 
                    g_val = True

                if  gait > 550 and gait < 700 :
                    ga_val = True


    return (r_val , g_val , ga_val)