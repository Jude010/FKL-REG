

class project:
    def __init__(self, name, privacy , number=0):
        self.stairs = []
        self.privacy = privacy
        self.name = name

        # initalise a number of stairs equal to number and names them stair1 to stair(number)
        for i in range(int(number)):
            self.stairs.append(stair("stair" + str(i+1)))


    def stair_add(self, stair):
        self.stairs.append(stair)

    def stair_num(self):
        return len(self.stairs)

    def serialize(self):
        dict = {"name": self.name,
                "privacy": self.privacy}
        
        for i in range(self.stair_num):
            dict['stair' + i] = self.stairs[i].serialize()
        
        return dict




class stair:
    def __init__(self , name) -> None:
        self.inside = ''
        self.name = name

    def serialize(self):
        return {"name": self.name,
                "inside": self.inside}

    
