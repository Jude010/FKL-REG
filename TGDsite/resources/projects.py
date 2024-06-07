

class project:
    def __init__(self, privacy):
        self.stairs = []
        self.privacy = privacy

    def stair_add(self, stair):
        self.stairs.append(stair)
    



class stair:
    def __init__(self , inside) -> None:
        self.inside = inside
    
