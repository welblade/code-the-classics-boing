from pgzero.actor import Actor

class Impact(Actor):
    
   def __init__(self, pos):
      super().__init__("blank", pos)
      self.time = 0
      
   def update(self):
        self.image = "impact" + str(self.time // 2)
        self.time += 1