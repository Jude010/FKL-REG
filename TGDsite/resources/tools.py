
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


 # validate the rise going and gait based on passed specifications
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

def validate_project(project , results):
    privacy = project['privacy']
    for i in range(project['stair_num']):# for each stair
        i = str(i)
        stair = project['stairs'][str(i)]
        internal = stair['inside']
        part_m = stair['part_m']
        
        
        for j in range(int(stair['floors'])): # for each floor in each stair
            j = str(j)
            rise = int(results['floor_rise'+ j + i])
            going = int(results['floor_going'+ j + i])
            

            val = vaidate_gait(internal , privacy , part_m , rise , going) # validate the gait rise and going
            stair['floor'+j]['stair_validation'] = val
            stair['floor' + j]['rise'] = rise 
            stair['floor' + j]['going'] = going
            stair['floor' + j]['gait'] = 2*rise + going

            if part_m == True: # handrails 
                if 'handrails'+j+i in results :
                    stair['floor'+j]['handrail_validation'] = True
                else:
                    stair['floor'+j]['handrail_validation'] = False
            else:
                if stair['floor'+j]['risers'] > 3 :
                    if 'handrails'+j+i in results:
                        stair['floor'+j]['handrail_validation'] = True
                    else:
                        stair['floor'+j]['handrail_validation'] = False
                else:
                    stair['floor'+j]['handrail_validation'] = True
            stair['floor' + j]['handrails'] = True

            


        
        
        if privacy == 'domestic' :
            if internal == "internal" :
                if part_m == True :
                    # internal domestic part m

                    if int(results['width' + i])> 900: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom + i']

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding' + i ]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = results['guarding' + i ]

                    # Open risers
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]



                else :
                    # internal domestic non part_m

                    if int(results['width' + i])> 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding' + i ]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = results['guarding' + i ]

                    # Open risers
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]
                    
            else :
                if part_m == True :
                    # external domestic part m

                    if int(results['width' + i])> 900: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if ('guarding' + i) in results :
                            stair['g_validation'] = True
                            stair['guarding'] = True
                        else:
                            stair['g_validation'] = False
                            stair['guarding'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = ('guarding' + i) in results

                    # Open risers -- TODO:make account for rise
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = ('taper' + i) in results
                    
                else :
                    # external domestic non part_m

                    if int(results['width' + i])> 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding' + i ]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = results['guarding' + i ]

                    # Open risers -- TODO:make account for rise
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]
                    
        else :
            if internal == "internal" :
                if part_m == True :
                    # internal public part m

                    # width
                    if int(results['width' + i])> 1200:
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    # headroom
                    if int(results['headroom' + i])>= 2100:
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                    #handrail width
                    if int(results['handrail_width'+i]) >= 1000 :
                        stair['hand_width_val'] = True
                    else:
                        stair['hand_width_val'] = False
                    stair['hand_width'] = results['handrail_width'+i]

                    # Open risers 
                    stair['r_validation'] = False
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]

                    #visibility_lux
                    if int(results['tread_lux'+i]) >=100: 
                        stair['vis_validation'] = True
                    else:
                        stair['vis_validation'] = False
                    stair['tread_lux'] = results['tread_lux'+i] 

                    #visibility_contrast
                    stair['con_validation'] = results['tread_con'+i]
                    stair['tread_con'] = results['tread_con'+i]
                    
                else :
                    # internal public non part_m

                    if int(results['width' + i]) > 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i]) >= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i]) >= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding'+i]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True

                    # Open risers -- TODO:make account for rise
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]
                    
            else :
                if part_m == True :
                    # external public part m

                    if int(results['width' + i])> 1200: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom' + i]

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding' + i ]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = results['guarding' + i ]

                    # Open risers -- TODO:make account for rise
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]

                    #tactile Hazard
                    stair['hazard_validation'] = results['hazard'+i]
                    stair['hazard_tact'] = results['hazard'+i]
                    
                else :
                    # external public non part_m
                    
                    if int(results['width' + i])> 1200: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if int(results['headroom' + i])>= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if int(results['handrail_pitch'+i])>= 900 and int(results['handrail_pitch'+i])<= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False
                    stair['hand_pitch'] = results['handrail_pitch'+i]

                    # handrail specs landing
                    if int(results['handrail_land'+i]) >= 900 and int(results['handrail_land'+i]) <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False
                    stair['hand_land'] = results['handrail_land'+i]

                   # guarding specs
                    if int(stair['rise']) > 600:
                        if results['guarding' + i ]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True
                    stair['guarding'] = results['guarding' + i ]

                    # Open risers -- TODO:make account for rise
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]

        project['stairs'][i] = stair


    for i in range(project['ramp_num']):
        ramp = project['ramps'][i]
        part_m = ramp['part_m']

        if part_m == True:
            if privacy == 'domestic':
                #domestic part_M

                # headroom
                if int(results['r_headroom' + i]) >= 2100:
                    ramp['head_val'] = True
                else:
                    ramp['head_val'] = False
                ramp['headroom'] = results['r_headroom' + i]

                # width
                if int(results['r_width' + i]) >= 900:
                    ramp['width_val'] = True
                else:
                    ramp['width_val'] = False
                ramp['width'] = results['r_width' + i]

                # kirb
                if results['kirb' + i] and int(ramp['rise']) >= 100:
                    ramp['kirb_val'] = True
                elif not results['kirb' + i] and int(ramp['rise']) >= 100:
                    ramp['kirb_val'] = False
                else: 
                    ramp['kirb_val'] = True
                ramp['kirb'] = results['kirb'+i]

                
            else:
                #non domestic part_M

                # headroom
                if int(results['r_headroom' + i]) >= 2100:
                    ramp['head_val'] = True
                else:
                    ramp['head_val'] = False
                ramp['headroom'] = results['r_headroom' + i]

                # width
                if int(results['r_width' + i]) >= 1500:
                    ramp['width_val'] = True
                else:
                    ramp['width_val'] = False
                ramp['width'] = results['r_width' + i]

                # handrail width
                if int(results['r_width_h' + i]) >= 1200:
                    ramp['h_width_val'] = True
                else:
                    ramp['h_width_val'] = False
                ramp['h_width'] = results['r_width_h' + i]

                #handrails
                if results['r_handrails'+i]:
                    ramp['handrail_val'] = True
                else:
                    ramp['handrail_val'] = False
                ramp['handrails'] = results['r_handrails'+i]

                #stepped acess route
                if not results['r_stepped'+i] and int(ramp['rise']) > 300:
                    ramp['stepped_val'] = False
                else:
                    ramp['stepped_val'] = True
                ramp['stepped'] = results['r_stepped'+i] 
                
                #Stair Lift
                if not results['r_lift'+i] and int(ramp['rise']) > 2000 and int(ramp['slope'].split(':')[2])  <= 20:
                    ramp['lift'] = False
                else:
                    ramp['lift'] = True
                ramp['lift'] = results['r_lift'+i]
        

        else:
            #non part_M

            #headroom
            if int(results['r_headroom' + i]) >= 2000:
                ramp['head_val'] = True
            else:
                ramp['head_val'] = False
            ramp['headroom'] = results['r_headroom' + i]

            #width
            if int(results['r_width' + i]) >= 800:
                ramp['width_val'] = True
            else:
                ramp['width_val'] = False
            ramp['width'] = results['r_width' + i]

            # handrail height
            if int(results['r_hand_height' + i]) >= 900 and int(results['r_hand_height' + i]) <=1000:
                ramp['hand_height'] = True
            else:
                ramp['hand_height'] = False
            ramp['h_height'] = results['r_hand_height' + i]

            
        
        project['ramps'][i] = ramp
    
    return project