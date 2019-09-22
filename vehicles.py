class vehicle:   # vehicle is the name of the class
    def __init__(self,doors,wheels,name):   # always put self at the beginning insde ()
        self.doors = doors
        self.wheels = wheels
        self.name = name
    def __repr__(self):  
        return "%s: %d doors and %d wheels"%(self.name, self.doors, self.wheels)
    def __eq__(self,aveh):   # comparing two vehicles, self is v1 and ahve is v2
        return self.doors==aveh.doors and self.wheels==aveh.wheels
    def __iadd__(self,aveh):  # add the number of doors and wheels to the 2nd vehicle
        self.doors += aveh.doors  # add the doors of the 2nd vehicle to the 1st vehicle
        self.wheels += aveh.wheels  # add the wheels of the 2nd vehicle to the 1st vehicle
        self.name += "+"
        self.name += aveh.name
        return self


