

class project:
    def __init__(self, name, privacy , stair_no=0, floors=1 , ramp_no=0):
        self.stairs = []
        self.ramps = []
        self.privacy = privacy
        self.name = name
        self.floors = floors

        # initalise a number of stairs and ramps equal to number and names them stair/ramp_1 to stair/ramp_(number)
        for i in range(int(stair_no)):
            self.stairs.append(stair("stair_" + str(i)))

        for i in range(int(ramp_no)):
            self.ramps.append(ramp("ramp_" + str(i)))


    def stair_add(self, stair):
        self.stairs.append(stair)

    def stair_num(self):
        return len(self.stairs)

    # convert into dict for session purposes
    def serialize(self):
        temp={}
        dict = {"name": self.name,
                "privacy": self.privacy,
                "stair_num": self.stair_num(),
                "floors": self.floors
                }
        for i in range(self.stair_num()):
            temp[str(i)] = self.stairs[i].serialize()
        
        dict['stairs'] = temp

        return dict

    



class stair:
    def __init__(self , name) -> None:
        self.inside = ''
        self.name = name
        self.rise = 0
        self.part_m = False


    # convert to dict for session purposes
    def serialize(self):
        return {"name": self.name,
                "inside": self.inside,
                "rise": self.rise,
                "part_m": self.part_m}
    

class ramp:
    def __init__(self , name) -> None:
        self.inside  = ''
        self.name = name
        self.rise = 0
        self.part_m = False
        self.width = 0

    # conver to dict
    def serialize(self):
        return {"name": self.name,
                "inside": self.inside,
                "rise": self.rise,
                "part_m": self.part_m,
                "width": self.width}



    
