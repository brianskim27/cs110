class LSystem:
    #You may add additional methods and break methods up.
    #Below is the interface that I am expecting in the driver.
    def __init__(self,filename):
        """
        sets up variables and reads in the text files
        args: self, filename
        return: none
        """
        file = open(filename, 'r')
        
        self.angle = int(file.readline())
        self.iteration = int(file.readline())
        self.distance = int(file.readline())
        self.axiom = file.readline()
        self.file_dict = file.readlines()
        self.result = self.axiom
        self.rules = {}
        
        for line in self.file_dict:
            line = line.split(" : ")
            self.rules[line[0].strip()] = line[1].replace('\n', '').strip()
        
        file.close()

    def createLSystem(self):
        """
        Uses the rules to create an lsystem
        args: self
        return: none
        """
        for i in range(self.iteration):
            new_str = ''
            
            for ch in self.result:
                new_str += self.rules.get(ch, ch)
            
            self.result = new_str

    def drawLSystem(self, snap):
        """
        Uses the rules to visualize the lsystem via turtle
        args: self, snap
        return: none
        """
        state_list = []
        
        for cmd in self.result:
            if (cmd == 'F'):
                snap.forward(self.distance)

            elif (cmd ==  '-'):
                snap.left(self.angle)

            elif (cmd == '+'):
                snap.right(self.angle)

            elif (cmd == '['):
                state_list.append({key:value for key, value in snap.__dict__.items()})

            elif (cmd == ']'):
                snap.__dict__ = state_list.pop()
