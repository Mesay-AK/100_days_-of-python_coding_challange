print('Welcome to the tip calculator!')

total = input('What was the total bill?')

total = float(total[1:])
tip = int(input('How much tip would you liketo give? 10, 12, or 15?'))

tip  = total * tip/100

ppl = int(input('How many people to split the bill?'))

final = round((total + tip)/ppl, 2)
print(f'Each person should pay: ${final}.')
