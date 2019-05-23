
try:
	hours = int(input("Enter hours: "))
	rate = int(input("Enter rate: "))

	if hours > 40:
		overtimePay = (hours - 40) * rate * 1.5
		pay = 40 * rate + overtimePay
		print(pay)
	else:
		pay = hours * rate
		print(pay)
except:
	print("Enter numbers")