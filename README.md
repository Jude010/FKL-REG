Website to aid in the use of the irish TGD's

Technology used

Flask - webserver \
Postgres - database \
Vagrant + Virtualbox - VM hosting \
jinja/html/css - web design


project dict shape in session

project{name, privacy, floors, stair_num, ramp_num, stairs{ i{name, inside, rise, part_m, floor(j){rise, flights} }}, ramps{ i{name, inside, rise, width, part_m, going, slope}}}