file_object = open('words.txt')

letters = input("Enter in letters with no space: ").lower()
for word in file_object:
	original_word = word
	score = 0
	if len(word) - 1 == len(letters):
		for letter in letters:
			if letter in word:
				score += 1
				word = word.replace(letter, "", 1)
			if score == len(letters):
				print(original_word, end="")
