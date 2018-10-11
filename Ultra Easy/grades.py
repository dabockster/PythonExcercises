global percent

# Ask the user for a percentage from 0 to 100
percent = input("Enter grade percentage: ")

# Cast to int
percent = int(percent)

def check_range():
	global percent

	if (percent < 0) or (percent > 100):
		print ("Percentage is either below 0 or greater than 100\n")

		# Ask the user for a percentage from 0 to 100
		percent = input("Enter grade percentage: ")

		# Cast to int
		percent = int(percent)

		check_range()

# Check the percentage range
check_range()

# Ask for project completion
project = input("Was the project completed? Y/N: ")

# Add 10% to reflect a full letter bump if the project was completed
if project == "Y" or "y":
	percent += 10

# Fix grade if over 100
if percent > 100:
	percent = 100

print ("\nStudent's grade is below: ")

if percent < 50:
	print ("YOU FAILED THE ASSIGNMENT!")
elif percent in range(50, 69):
	print ("You have earned a C grade.")
elif percent in range(70, 89):
	print ("You have earned a B grade.")
elif percent in range(90, 100):
	print ("You have earned an A grade")
else:
	print ("\nERORR: Took the L!")
	print ("percentage = " + str(percentage))