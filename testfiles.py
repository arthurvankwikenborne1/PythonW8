from files import TextFile

try:
	file = TextFile("logfile.txt")
	print(file.returnLongestWord())
except ValueError as err:
	print(err)
finally:
	print("altijd")

#wijzigingen