import random

class MontyHall:
	def __init__(self):
		self.runs_switched = 0.0
		self.runs_not_switched = 0.0
		self.wins_switched = 0.0
		self.wins_not_switched = 0.0

	def run(self,num_runs):
		for i in range(num_runs):
			win,switch = self.simulate_game()
			if switch == 1:
				self.runs_switched += 1
				if win:
					self.wins_switched += 1
			else:
				self.runs_not_switched += 1
				if win:
					self.wins_not_switched += 1
		print("percentage of won switched",self.wins_switched/self.runs_switched)
		print("percentage of won not switched",self.wins_not_switched/self.runs_not_switched)


	def simulate_game(şelf):
		car_position = random.choice([0,1,2])
		goat_positions = [0,1,2]
		goat_positions.remove(car_position)
		possible_player_choices = [0,1,2]
		#print("goats:",goat_positions)
		#print("car:",car_position)
		#player makes choice
		player_choice = random.choice(possible_player_choices)
		#print("player chose",player_choice)
		#host opens a random goat door (that is not what the player chose!)
		if player_choice in goat_positions:
			goat_positions.remove(player_choice)
		host_choice = random.choice(goat_positions)
		#print("host chose",host_choice)
		#new available player choices
		possible_player_choices.remove(host_choice)
		#player switches if he wants to
		switch = random.choice([0,1])
		if switch == 1:
			if player_choice == possible_player_choices[0]:
				player_choice = possible_player_choices[1]
			else:
				player_choice = possible_player_choices[0]
		#	print("Player switched to",player_choice)
		else:
		#	print("Player did not switch")
			pass

		if player_choice == car_position:
			#print("win")
			return (True,switch)
		#print("lose")
		return (False,switch)


m = MontyHall()
m.run(10000000)