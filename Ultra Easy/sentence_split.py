# Enter sentence
sentence = input("Enter a sentence: ")

# Check for punctuation and remove if any
last_char_letter = True

for character in sentence:
	if character.isalpha():
		last_char_letter = True
	else:
		last_char_letter = False

if last_char_letter == False:
	sentence = sentence[:-1]

sentence = sentence.split();

for word in sentence:
	print (word)