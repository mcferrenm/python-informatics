inp = input("Enter f: ")
try:
	f = float(inp)
	c = (f - 32.0) * 5.0 / 9.0
	print(c)
except:
	print('enter a NUMBER!')