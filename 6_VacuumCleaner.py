class VacuumCleaner:
    def _init_(self):
        self.state = ('A', 'D', 'D')  

    def clean(self):
        current_room = self.state[0]
        if current_room == 'A':
            self.state = (current_room, 'C', self.state[2]) 
            print("Cleaning Room A")
        else:
            self.state = (current_room, self.state[1], 'C') 
            print("Cleaning Room B")

    def move(self):
        current_room = self.state[0]
        if current_room == 'A':
            self.state = ('B', self.state[1], self.state[2])  
            print("Moving to Room B")
        else:
            self.state = ('A', self.state[1], self.state[2]) 
            print("Moving to Room A")

    def run(self):
        while True:
            if self.state[1] == 'C' and self.state[2] == 'C':
                print("Both rooms are clean!")
                break
            
            if self.state[1] == 'D' and self.state[0] == 'A':
                self.clean()
            elif self.state[2] == 'D' and self.state[0] == 'B':
                self.clean()
            else:
                self.move()

vacuum = VacuumCleaner()
vacuum.run()