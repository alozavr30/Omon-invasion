from random import randint

class Die():
	def __init__(self, sides=6):
		self.sides = sides
	    
	def roll_die(self, rolls=1):
		print(*[randint(1, self.sides) for _ in range(rolls)])

kybik = Die()
kybik.roll_die(10)

kybik2 = Die(10)
kybik2.roll_die(10)

kybik3 = Die(20)
kybik3.roll_die(10)



