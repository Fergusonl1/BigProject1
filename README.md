# BigProject1
Vexcode project for engineering

	Pseudocode

class Claw_Control:
  def __init__(self, claw_limit):
    self.claw_limit = claw_limit
  
  def move_claw_pos_x(self, claw_location):
    if claw_location != self.claw_limit:
      move_claw_x(+1)
    else:
      return None
  
  def move_claw_neg_x(self, claw_location):
    if claw_location != self.claw_limit:
      move_claw_x(-1)
    else:
      return None
  def move_claw_pos_y(self, claw_location):
    if claw_location != self.claw_limit:
      move_claw_y(+1)
    else:
      return None
   def move_claw_neg_y(self, claw_location):
    if claw_location != self.claw_limit:
      move_claw(-1)
    else:
      return None
 class Drop_claw:
    def __init__(self)
      pass
    
    def drop_claw(self, claw_input):
      if claw_input == True:
        drop_claw
      else:
        None
