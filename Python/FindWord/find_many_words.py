file_object = open('words.txt')

letters = input("Enter in letters with no space: ").lower()
for word in file_object:
	for i in range(3, len(letters) + 1):
		original_word = word
		score = 0
		if len(word) - 1 == i:
			for letter in letters:
				if letter in word:
					score += 1
					word = word.replace(letter, "", 1)
			if score == i:
				print(original_word)

