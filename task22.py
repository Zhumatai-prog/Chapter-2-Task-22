fah = int(input("Enter fahrenheit to convert to Celsius: "))
def fah_to_cel(f):
	return ((f - 32) / 1.8)
print(fah_to_cel(fah))

cel = int(input("Enter Celsius to convert to fahrenheit: "))
def cel_to_fah(c):
	return((c * 1.8) + 32)
print(cel_to_fah(cel))