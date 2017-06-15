import math

input_number = float(input('Enter number to find the square root of: '))
return_number = input_number
expected_number = math.sqrt(input_number)


while not(expected_number - 1e-10 < return_number < expected_number + 1e-10):
	return_number = return_number - ((return_number ** 2 - input_number)/(2*return_number))

print("The square root of {} is {}".format(input_number, return_number))