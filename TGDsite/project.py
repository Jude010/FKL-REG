from flask import redirect , render_template , Blueprint , request ,session , url_for

from TGDsite.resources import project_parts, readText , tools
import datetime


bp = Blueprint('project',__name__, url_prefix='/project')

@bp.route('/project_results', methods=['POST'])
def project_results():
    results = request.form
    project = session['project']
    date = datetime.date.today()
    for i in range(project['ramp_num']):
        project['ramps'][str(i)]['name'] = results[str(i)]
        project['ramps'][str(i)]['inside'] = results["internal" + str(i)]
        project['ramps'][str(i)]['rise'] = results["rise" + str(i)]
        project['ramps'][str(i)]['width'] = results["width" + str(i)]
        if "part_m" + str(i) in results.keys():
            project['ramps'][str(i)]['part_m'] = True
        else:
            project['ramps'][str(i)]['part_m'] = False

        print(str(project['ramps'][str(i)]['rise']) + "test")
        temp = tools.calc_slope(project['ramps'][str(i)]['rise'], project['ramps'][str(i)]['part_m'] ,project["privacy"])
        project['ramps'][str(i)]['going'] = temp[0]
        project['ramps'][str(i)]['slope'] = temp[1]
        temp = None

    session['project'] = None
    session['project'] = project
    print(project)
    return render_template('project_results.html.jinja', project = project , date = date)

@bp.route('/project_validation' , methods=['POST'])
def project_valid():
    results = request.form
    project = session['project']
    privacy = project['privacy']
    for i in range(project['stair_num']):# for each stair
        stair = project['stairs'][i]
        internal = stair['inside']
        part_m = stair[i]['part_m']
        
        for j in range(['floors']): # for each floor in each stair
            rise = results['floor_rise'+ j + i]
            going = results['floor_going'+ j + i]

            val = tools.vaidate_gait(internal , privacy , part_m , rise , going) # validate the gait rise and going
            stair['floor'+j]['stair_validation'] = val

            if part_m == True: # handrails 
                if results['handrails'+i+j] == True:
                    stair['floor'+j]['handrail_validation'] = True
                else:
                    stair['floor'+j]['handrail_validation'] = False
            else:
                if stair['floor'+j]['risers'] > 3 :
                    if results['handrails'+i+j] == True:
                        stair['floor'+j]['handrail_validation'] = True
                    else:
                        stair['floor'+j]['handrail_validation'] = False
                else:
                    stair['floor'+j]['handrail_validation'] = True


        
        
        if privacy == 'domestic' :
            if internal == "internal" :
                if part_m == True :
                    # internal domestic part m

                    if results['width' + i] > 900: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
                        if results['guarding'+i]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True

                    # Open risers
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]



                else :
                    # internal domestic non part_m

                    if results['width' + i] > 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
                        if results['guarding'+i]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True

                    # Open risers
                    stair['r_validation'] = True
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]
                    
            else :
                if part_m == True :
                    # external domestic part m

                    if results['width' + i] > 900: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
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
                    # external domestic non part_m

                    if results['width' + i] > 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
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
            if internal == "internal" :
                if part_m == True :
                    # internal public part m

                    if results['width' + i] > 1200: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    #handrail width
                    if results['hand_width'+i] >= 1000 :
                        stair['hand_width_val'] = True
                    else:
                        stair['hand_width_val'] = False

                    # guarding specs
                    if stair['rise'] > 600:
                        if results['guarding'+i]:
                            stair['g_validation'] = True
                        else:
                            stair['g_validation'] = False
                    else:
                        stair['g_validation'] = True

                    # Open risers 
                    stair['r_validation'] = False
                    stair['o_riser'] = results['o_riser' + i]

                    #TaperedTreads
                    stair['taper_validation'] = False
                    stair['taper'] = results['taper' + i]

                    #visibility
                    if results['tread_lux'+i] >=100: 
                        stair['vis_validation'] = True
                    else:
                        stair['vis_validation'] = False
                    stair['tread_lux'] = results['tread_lux'+i] 
                    
                else :
                    # internal public non part_m

                    if results['width' + i] > 800: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2000: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
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

                    if results['width' + i] > 1200: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
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

                    #tactile Hazard
                    stair['hazard_validation'] = results['hazard'+i]
                    
                else :
                    # external public non part_m
                    
                    if results['width' + i] > 1200: #width
                        stair['w_validation'] = True
                    else:
                        stair['w_validation'] = False
                    stair['width'] = results['width' + i]

                    if results['headroom' + i] >= 2100: #headroom
                        stair['hdr_validation'] = True
                    else:
                        stair['hdr_validation'] = False
                    stair['headroom'] = results['headroom']

                    # handrail specs pitch
                    if results['handrail_pitch'+i] >= 900 and results['handrail_pitch'+i] <= 1000 :
                        stair['hr_p_validation'] = True
                    else  :
                        stair['hr_p_validation'] = False

                    # handrail specs landing
                    if results['handrail_land'+i] >= 900 and results['handrail_land'+i] <= 1100 :
                        stair['hr_l_validation'] = True
                    else  :
                        stair['hr_l_validation'] = False

                    # guarding specs
                    if stair['rise'] > 600:
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

        project['stairs'][i] = stair


    for i in range(project['ramp_num']):
        ramp = project['ramps'][i]
        part_m = ramp['part_m']

        if part_m == True:
            if privacy == 'domestic':
                #domestic part_M

                # headroom
                if results['r_headroom' + i] >= 2100:
                    ramp['head_val'] = True
                else:
                    ramp['head_val'] = False

                # width
                if results['r_width' + i] >= 900:
                    ramp['width_val'] = True
                else:
                    ramp['width_val'] = False

                # kirb
                if results['kirb' + i] and ramp['rise'] >= 100:
                    ramp['kirb_val'] = True
                elif not results['kirb' + i] and ramp['rise'] >= 100:
                    ramp['kirb_val'] = False
                else: 
                    ramp['kirb_val'] = True

                
            else:
                #non domestic part_M

                # headroom
                if results['r_headroom' + i] >= 2100:
                    ramp['head_val'] = True
                else:
                    ramp['head_val'] = False

                # width
                if results['r_width' + i] >= 1500:
                    ramp['width_val'] = True
                else:
                    ramp['width_val'] = False

                # handrail width
                if results['r_width_h' + i] >= 1200:
                    ramp['width_val'] = True
                else:
                    ramp['width_val'] = False

                #handrails
                if results['r_handrails'+i]:
                    ramp['handrail_val'] = True
                else:
                    ramp['handrail_val'] = False

                #stepped acess route
                if not results['r_stepped'+i] and ramp['rise'] > 300:
                    ramp['stepped_val'] = False
                else:
                    ramp['stepped_val'] = True
                
                #Stair Lift
                if not results['r_lift'+i] and ramp['rise'] > 2000 and ramp['slope'].split(':')[2]  <= 20:
                    ramp['lift'] = False
                else:
                    ramp['lift'] = True
        

        else:
            #non part_M

            #headroom
            if results['r_headroom' + i] >= 2000:
                ramp['head_val'] = True
            else:
                ramp['head_val'] = False

            #width
            if results['r_width' + i] >= 800:
                ramp['width_val'] = True
            else:
                ramp['width_val'] = False

            # handrail width
            if results['r_hand_width' + i] >= 900 and results['r_hand_width' + i] <=1000:
                ramp['hand_width'] = True
            else:
                ramp['hand_width'] = False

            
        
        project['ramps'][i] = ramp
            