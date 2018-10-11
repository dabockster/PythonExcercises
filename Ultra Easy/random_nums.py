# Randomizer needs import in Python
import random

# Set globals
global x
global y
global z

x = random.randint(0, 20)
y = random.randint(0, 20)
z = random.randint(0, 20)

# Re-randomize if any two numbers are the same
# Do this until all numbers are unique
def check_same():
	global x
	global y
	global z
	if (x == y) or (y == z) or (x == z):
		x = random.randint(0, 20)
		y = random.randint(0, 20)
		z = random.randint(0, 20)
		check_same()

check_same()

print ("x = " + str(x))
print ("y = " + str(y))
print ("z = " + str(z) + "\n")

# Largest number
if (x > y) and (x > z):
	print ("x = " + str(x) + " is largest")
elif (y > x) and (y > z):
	print ("y = " + str(y) + " is largest")
elif (z > x) and (z > y):
	print ("z = " + str(z) + " is largest")
else:
	print ("Your program took the L! Fix it.")

# Smallest number
if (x < y) and (x < z):
	print ("x = " + str(x) + " is smallest")
elif (y < x) and (y < z):
	print ("y = " + str(y) + " is smallest")
elif (z < x) and (z < y):
	print ("z = " + str(z) + " is smallest")
else:
	print ("Your program took the L! Fix it.")
# Average
print ("Average: " + str(int((x + y + z) / 3)))

