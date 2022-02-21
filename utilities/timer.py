import time as t
import threading as th

class Timer:
	""" Timer class time limit is defaulted to 45 seconds """
	def __init__(self, time_limit=45):
		self.time_limit = time_limit
	
	def timer(self):
		""" Timer method returns True when the timer is done """
		while self.time_limit != 0:
			t.sleep(1)
			self.time_limit = self.time_limit -1
		return True
	
	def main(self):
		""" Starts the timer method in the background """
		thread = th.Thread(target=self.timer, args=())
		thread.start()

if __name__ == '__main__':
	T = Timer()
	T.main()