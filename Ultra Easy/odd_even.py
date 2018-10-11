# Modulo
for i in range(0, 101):
	if i % 2 == 0:
		print (str(i) + " is even")
	else:
		print (str(i) + " is odd")

print ("----------------------")

# Without modulo
for i in range (0,101):
	num = int(i/2)

	if (num * 2 == i):
		print (str(i) + " is even")
	else:
		print (str(i) + " is odd")

