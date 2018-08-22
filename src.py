import re, os

class Game:
	"""docstring for Game"""
	def __init__(self, sects_passes):
		self.sects = sects_passes[0]
		self.passes = sects_passes[1]
		self.default = self.sects[0]
	def start(self):
		self.default.display(self.default.parse())
		pass

	def run(self, nm, kind):
		if kind == 1:
			for i in self.passes:
				print "The passage's name is "+i.nm+". The required one is "+nm+"."
				if i.nm == nm: 
					i.display(i.parse())
		elif kind == 2:
			for i in self.sects:
				print "The passage's name is "+i.nm+". The required one is "+nm+"."
				if i.nm == nm: i.display(i.parse())

	def end(self):
		return "You have reached the end!"
		


class Section:
	"""docstring for Section"""
	def __init__(self, nm, info, line):
		self.info = info
		self.nm = nm
		self.line = line
		self.options = []
		self.choice = 1
		self.numoptions = 0

	def display(self,printinfo):
		os.system("cls")
		valid = False
		while not valid:
			print printinfo
			self.choice = raw_input(">")
			try:
				self.choice = int(self.choice)
				valid = True
			except: 
				print "Please enter a number between 1 and "+self.numoptions+" as your choice."
				continue
			for i in self.options:
				if i[2] == int(self.choice):
					game.run(i[0],i[1])


	def parse(self):
		total = "\n".join(self.info)
		if total.find("[") != -1:
			index = 1
			for i in re.findall(r"\[(.*?)\]{1,2}",total): 
				if i.find("[") != -1:
					self.options.append([i[1:],2,index])
				else:
					self.options.append([i,1,index])
				index += 1
			self.numoptions = index

		total = total.replace("[","]")
		return total.replace("]","")
		

class Passage:
	"""docstring for Passage"""
	def __init__(self, nm, info, line):
		self.info = info
		self.nm = nm
		self.line = line
		self.options = []
		self.numoptions = 0

	def display(self,printinfo):
		valid = False
		while not valid:
			print printinfo
			if self.options != []:
				self.choice = raw_input(">")
			else:
				print game.end()
			try:
				self.choice = int(self.choice)
				valid = True
			except: 
				print "Please enter a number between 1 and "+self.numoptions+" as your choice."
				continue
			for i in self.options:
				if i[2] == int(self.choice):
					print i[0],i[1]
					game.run(i[0],i[1])

	def parse(self):
		total = "\n".join(self.info)
		if total.find("[") != -1:
			index = 1
			if total.find("[") != -1:
				for i in re.findall(r"\[{1,2}(.*?)\]{1,2}",total):
					if i.find("[") != -1:
						self.options.append([i[1:],2,index])
					else:
						self.options.append([i,1,index])
				index += 1
			self.numoptions = index

		total = total.replace("[","]")
		return total.replace("]","")
		


def main_parse(filename):
	sections = []
	passages = []

	with open(filename, "r") as f:
		prevFound = None
		default = Section("default",[],0)
		sections.append(default)
		index = 0
		for line in f:
			if prevFound == None:
				if line[-1:] == "\n":
					default.info.append(line[:-1])
				else:
					default.info.append(line)
			if line.endswith("]]:\n"):
				section = Section(line[2:line.find("]]")],[],index)
				sections.append(section)
				prevFound = section

			
			if line.endswith("]:\n") and not line.endswith("]]:\n"):
				passage = Passage(line[1:line.find("]")],[],index)
				passages.append(passage)
				prevFound = passage
			if line.find("\t") == 0 and prevFound != None:
				if line[-1:] == "\n":
					prevFound.info.append(line[1:-1])
				else:
					prevFound.info.append(line[1:])
			index += 1
	try: default.info = default.info[:-2]
	except: pass
	return sections, passages

game = Game(main_parse("game.puf"))
game.start()
end = input("Press any key to continue...")
