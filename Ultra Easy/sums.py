# 0 to 1000
print ("Summing all ints 0 -> 1000:")

sum = 0;

for i in range(0,1000):
	sum += i

print (sum)

# X to Y
x = int(input("Enter a value for X: "))
y = int(input("Enter a value for Y: "))

sum = 0

for i in range (x, y):
	sum += i

print (sum)