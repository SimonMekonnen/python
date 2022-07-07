print("wlcome to tip calculator")
bill = int(input('what is the total bill?  '))
percent = int(input('what percentage of tip would you like to give?  '))
people = int(input ('what are the no of peopele?  '))
tip =  round((bill + (bill*percent)/100)/people,2)
print(f'the tip is {tip}')

