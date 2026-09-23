# Calculate gross pay including overtime for hours worked over 40

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    if hrs > 40:
        regular_pay = rate * 40
        overtime = hrs - 40
        overtime_pay = overtime * rate * 1.5
        gross_pay = regular_pay + overtime_pay
    else:
        gross_pay = hrs * rate
        
    print(f"Gross Pay: {gross_pay:.2f}")
    
except ValueError:
    print("Error: Please enter a valid numeric value.")
