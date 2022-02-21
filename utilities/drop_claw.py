from timer import Timer
from vexcode import *


drivetrain = Drivetrain()
magnet = Electromagnet("magnet", 0)
pen = Pen()
brain = Brain()
left_bumper = Bumper("leftBumper", 1)
right_bumper = Bumper("rightBumper", 2)
distance = Distance()
front_eye = EyeSensor("fronteye", 3)
down_eye = EyeSensor("downeye", 4)
location = Location()


class Drop_Claw:
	def __init__(self, claw_limit):
		""" Takes the maximum distance that the claw can move """
		self.claw_limit = claw_limit
	
	def move_claw_to_start(self):
		""" moves the claw to the 3rd quadrent on a cordinate plane """
