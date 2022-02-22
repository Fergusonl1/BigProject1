import time as t
import vex
from vex import *
 
brain = Brain()

drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()
 

class Drop_Claw:
	def __init__(self, claw_limit_x:int, claw_limit_y:int, claw_limit_z:int):
		""" Takes the maximum distance that the claw can move, claw limit for the x, y, and z will be used to messure the full distance it can go
			The cordinate limits are stored in a dictionary with x, y, z. """
		self.claw_limit = {'x':claw_limit_x, 'y':claw_limit_y, 'z': claw_limit_z}
	
	def move_claw_to_start(self):
		""" moves the claw to the 3rd quadrent on a cordinate plane """
		x_limit = self.claw_limit['x']
		y_limit = self.claw_limit['y']
	

	def drop_claw(self):
		""" Drops the claw making the z value go down, z is set to zero because it hasn't moved down """
		current_pos = 0
		z_limit = self.claw_limit['z']
		while current_pos != z_limit:
			current_pos = current_pos - 1
			t.sleep(0.2)
		return True 
