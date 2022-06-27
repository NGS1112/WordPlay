"""
File: word_play.py
Name: Nicholas Shinn
Description: Removes letters from a string and matches them with actual words from a file
"""
from os.path import exists

def main():
	"""
	runs the check_deletions function, taking user input for the string and file name
	"""
	word = str(input('Enter word to be checked: '))
	filename = str(input('Enter name of word file to be checked: '))

	if word == '' and filename == '':
		print('Error: No input detected')
	elif word == '':
		print('Error: No string detected')
	elif filename == '':
		print('Error: No file detected')
	elif exists(filename) == False:
		print('Error: File does not exist')
	else:
		file = open(filename)
		check_deletions(word, file)
		file.close()

def check_deletions(string, file):
	"""
	Takes a string, removes letters, and checks them against words within the given file
	:param string: Takes a word with which to remove letters
	:param file: Takes a file to compare words against
	:return: Returns matching words
	"""
	n = 0
	z = 0
	for line in file:
		line = line.strip()
		index = 0
		for n in range(0, len(string)):
			if index < len(line) and line[index] == string[n]:
				index += 1
			#deletion = string[:n] + string[n + 1:]
			#print( deletion )
			#if line.strip() == deletion:
				#z += 1
				#print(str(z) + ' ' + deletion)
		if len(line) == index:
			z += 1
			print(str(z) + ' ' + line)
	print('Found ' + str(z) + ' deletions')


if __name__ == "__main__":
    main()