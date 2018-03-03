import random
used_machine = []

class Person():
	"""this is a practical approach to the futurama theorem solution
	I can't and possibly won't ever write it down mathematically so I came up
	with that solution through experiments, this program simulates the mindswapping
	brings in the two helpers and corrects everyone, it should work for "infinite" persons
	WARNING!!! I trust the user (bad idea) giving valid input, due to lack of time 
	my validation is to say the least lacking, maybe in the future...."""

	#object person has 2 attributes, body and mind
	def __init__(self, body, mind):
		self.body = body
		self.mind = mind

	#mindSwitcher checks if 2 characters have used the machine before
	#if not it swaps minds, else it prints that it wont work
	def mindSwitcher(person1, person2):
		if (person1.body, person2.body) in used_machine:
			print "The machine won't work!"
		elif person1 == person2:
			return
		else:
			person1.mind, person2.mind = person2.mind, person1.mind
			used_machine.append((person1.body,person2.body))
			used_machine.append((person2.body, person1.body))
			print person1.body + " now has " + person1.mind + "'s mind and " + person2.body + " has " + person2.mind + "'s mind!"

	#commence_experiment runs 'times' times mindswaps randomly
	#with the characters given by the user
def commence_experiment(times,chars):
	for i in xrange(times):
		random.choice(chars).mindSwitcher(random.choice(chars))

def permToCycles(bodies, minds):
	pi = dict(zip(bodies,minds))
	cycles = []

	while pi:
		elem0 = next(iter(pi))
		this_elem = pi[elem0]
		next_item = pi[this_elem]

		cycle = []
		while True:
			cycle.append(this_elem)
			del pi[this_elem]
			this_elem = next_item
			if next_item in pi:
				next_item = pi[next_item]
			else:
				break
		cycles.append(cycle)
	return cycles



def main():
	num_of_persons = int(raw_input("Give me the number of persons taking part in the 'experiment': "))
	person_names = []
	persons = []
	for i in xrange(num_of_persons):
		char_name = raw_input("Give me the name of person #"+str(i+1)+": ")
		while True:
			if char_name not in person_names:
				persons.append(Person(char_name,char_name))
				person_names.append(char_name)
				break
			else:
				print "you've already registered "+char_name+" for the experiment!\nGive another one: "
				char_name = raw_input("Give me the name of person #"+str(i+1)+": ")
	times = int(raw_input("Lastly give me the number of times you want the experiment to take place: "))
	commence_experiment(times,persons)
	#by now all the characters are shuffled
	#because the mindswapping is done randomly sometimes 2 characters
	#that have used the machine before will attempt to mindswap again so a
	#'Machine won't work' message will appear

	#You have to do some work to save the day though too
	#It's easy though, all you have to do is search the mindswitching data printed
	#and try to find cycles/loops of characters/minds
	#the program will guide you and do the rest
	#it is case-sensitive...
	answer = raw_input("Ready to return everyone to normal? (y/n): ")
	if answer == "y":
		raw_input("Two mathematician-basketball players arrive to save the day \nPress enter to continue...")
		helper1_name = raw_input("Give the 1st helper a name: ")
		helper2_name = raw_input("Give the 2nd helper a name: ")
		helper1 = Person(helper1_name, helper1_name)
		helper2 = Person(helper2_name, helper2_name)
		raw_input("Your help though is crucial too!\nYou have to spot the cycles formed after the permutations and type them down!\nGood luck! Press enter to continue...")
		print "line1: bodies, line2: minds: "
		bodies = []
		minds = []
		perm = []
		for person in persons:
			bodies.append(person.body)
			minds.append(person.mind)
		print bodies
		print minds
		raw_input("Find the cycles/loops! You will have to input them!")
		raw_input("Just kidding, all hail the power of the machine! I will do the rest...")
		#permToCycles writes my permutation as the product of cycles
		cycles = permToCycles(bodies,minds)
		groups = []
		
		#here is the solution of the problem
		#probably deserving a function of its own but its 1:00 am
		#the first thought was, 2 helpers for every cycle
		#but (recalling there were only 2 dudes helping in the episode) the trick is to not
		#mindswap them with eachother up until the last cycle is finished
		#after the end of its cycle they will other be in each others bodies
		#or each in his own, depends if the cycle is even/odd
		for cycle in cycles:
			if len(cycle)==1:
				continue
			else:
				groupy = []
				for name in cycle:
					for person in persons:
						if person.body == name:
							groupy.append(person)
				groups.append(groupy)	
		for groupx in groups:
			helper1.mindSwitcher(groupx[-1])
			for j in groupx:
				helper2.mindSwitcher(j)
			helper1.mindSwitcher(groupx[0])
		if helper1.body != helper1.mind or helper2.body != helper2.mind:
			helper1.mindSwitcher(helper2)
		
		#rejoice!
		print "The day is saved! Here is everyone: "
		for person in persons:
			print person.body+" "+person.mind
		print helper1.body+" "+helper1.mind
		print helper2.body+" "+helper2.mind

	else:
		print("Too bad, your characters are screwed...")





if __name__ == "__main__":
	main()

