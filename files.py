class TextFile:
	def __init__(self, name):
		self.name = name

	def read_entire_file(self, x=None):
		with open(self.name, "r") as file:
			if(x is None):
				return file.read()
			else:
				return file.read(x)

	def returnXCharacters(x):
		return read_entire_file(x)

	def numberOfLines(self):
		aantal = 0
		with open(self.name, "r") as file:
			lines = file.readlines()
			for line in lines:
				aantal+=1
			return aantal

	def GeefAantalLijnenAlsListVanStrings(self,n=0):
		with open(self.name, "r") as file:
			lines = file.readlines()
			newList = []
			negativeNewList = []
			for line in lines:
				newList.append(line.strip(", \n"))
			if n<0:
				negativeNewList = newList[n:]
				return negativeNewList
			else:
				newList = newList[:n]
				return newList

	def GeefLijnWeer(self,i):
		with open(self.name, "r") as file:
			lines = file.readlines()
			for line_nr, line in enumerate(lines):
				if line_nr==i-1:
					return line.strip(", \n")

	def DictMetWords(self):
		with open(self.name, "r") as file:
			lines = file.readlines()
			dictWords = {}
			for line in lines:
				words = line.split()
				for word in words:
					clean_word = word.strip(" ,.?!\"'").lower()
					dictWords[clean_word] = dictWords.get(clean_word,0) + 1
			return dictWords
	
	def returnLongestWord(self):
		with open(self.name, "r") as file:
			listWords = []
			lines = file.readlines()
			for line in lines:
				words = line.split()
				for word in words:
					clean_word = word.strip(" ,?!\"'").lower()
					listWords.append(clean_word)
			listWords = sorted(listWords, key=len, reverse=True)
			return listWords[0]
