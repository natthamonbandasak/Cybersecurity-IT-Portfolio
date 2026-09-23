# Accumulate numbers, count inputs, and calculate the average until 'done' is entered

num = 0
tot = 0.0

while True:
    sval = input('Enter a number (or type "done" to finish): ')
    
    if sval.lower() == 'done':
        break
        
    try:
        fval = float(sval)
    except ValueError:
        print('Invalid input. Please enter a valid number.')
        continue
        
    num += 1
    tot += fval
    
if num > 0:
    average = tot / num
    print(f"\nTotal Sum: {tot}")
    print(f"Total Count: {num}")
    print(f"Average: {average:.2f}")
else:
    print("No valid numbers were entered.")
