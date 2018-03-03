import random
used_machine = []

class Person():
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
	#'Machine won't work message will appear

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
		raw_input("Your help though is crucial too!\nYou have to spot the cycles formed after the permutations and type them down!\ne.g. If Zapp changed with Fry and with no once else just enter Zapp then Fry in group1 and then enter '' as a character when prompted to add another person. When you are finished with your cycles just answer 'n' in the appropriate question.\nGood luck! Press enter to continue...")
		groups = []
		group_ans = "n"
		count = 0
		print("First group:")
		cycle_element = raw_input("Enter character: ")
		while group_ans != "y":
			groupx = []
			while cycle_element != "":
				if cycle_element not in groupx:
					#print "Entered cycle-groupx if" ~DEBUGGING
					groupx.append(cycle_element)
				else:
					print "Already in group\nGive another: "
					cycle_element = raw_input("Enter character: ")
					continue
				cycle_element = raw_input("Enter next character: ")
			if groupx not in groups:
				groups.append(groupx)
				group_ans = raw_input("Are you done with your groups? (y/n) ")
			else:
				print "You have already submitted that cycle dummy! Don't lose it now!"
		print ("Good job, well if you actually did a good job the mathematicians-basketball players will do the rest!\nYour groups are: "+groups
		for group in groups:
			helper1.mindSwitcher(group[-1])
			for j in group:
				helper2.mindSwitcher(j)
			helper1.mindSwitcher(group[0])
		if helper1.mind != helper1.name:
			helper1.mindSwitcher(helper2)
		print "The day is saved! Here is everyone: "
		for person in persons:
			print person.name+" "+person.mind
			print helper1.name+" "+helper1.mind
			print helper2.name+" "+helper2.mind

	else:
		print("Too bad, your characters are screwed...")





if __name__ == "__main__":
	main()

