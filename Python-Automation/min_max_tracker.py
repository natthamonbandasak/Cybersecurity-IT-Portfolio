# Track and output the maximum and smallest numbers entered by the user until 'done'

largest = None
smallest = None

while True:
    sval = input('Enter a number (or type "done" to finish): ')
    
    if sval.lower() == 'done':
        break
        
    try: 
        fval = int(sval)
    except ValueError:
        print('Invalid input. Please enter a valid integer.')
        continue
        
    if largest is None or fval > largest:
        largest = fval
    if smallest is None or fval < smallest:
        smallest = fval

if largest is not None and smallest is not None:
    print(f"\nMaximum is {largest}")
    print(f"Minimum is {smallest}")
else:
    print("No valid numbers were entered.")
