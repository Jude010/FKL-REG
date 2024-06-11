

class project:
    def __init__(self, name, privacy , number=0, floors=1):
        self.stairs = []
        self.privacy = privacy
        self.name = name
        self.floors = floors

        # initalise a number of stairs equal to number and names them stair1 to stair(number)
        for i in range(int(number)):
            self.stairs.append(stair("stair" + str(i+1)))


    def stair_add(self, stair):
        self.stairs.append(stair)

    def stair_num(self):
        return len(self.stairs)

    # convert into dict for session purposes
    def serialize(self):
        dict = {"name": self.name,
                "privacy": self.privacy,
                "stair_num": self.stair_num(),
                "floors": self.floors
                }
        for i in range(self.stair_num()):
            dict['stair' + str(i)] = self.stairs[i].serialize()
        
        return dict




class stair:
    def __init__(self , name) -> None:
        self.inside = ''
        self.name = name
        self.steps = 0

    # convert to dict for session purposes
    def serialize(self):
        return {"name": self.name,
                "inside": self.inside,
                "steps": self.steps}

    
