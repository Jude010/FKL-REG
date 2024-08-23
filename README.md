Website to aid in the use of the irish TGD's

Technology used

Flask - webserver \
Postgres - database \
Vagrant + Virtualbox - VM hosting \
jinja/html/css - web design


project dict shape in session

project{name:str, privacy:str, floors:int, stair_num:int, ramp_num:int, stairs{ i{name:str, inside:str, rise:int, part_m:bool, floor(j){rise:str, flights:int , validation:(bool , bool , bool)} }}, ramps{ i{name:str, inside:str, rise:int, width:int, part_m:bool, going:int, slope:str}}}