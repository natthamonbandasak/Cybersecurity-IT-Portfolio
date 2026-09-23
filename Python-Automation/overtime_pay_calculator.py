# Calculate gross pay including overtime using a modular function

def computepay(hours, rate):
    if hours <= 40:
        return hours * rate
    else:
        regular_pay = 40 * rate
        overtime_pay = (hours - 40) * rate * 1.5
        return regular_pay + overtime_pay

try:
    hrs = float(input("Enter Hours: "))
    rate = float(input("Enter Rate: "))
    
    gross_pay = computepay(hrs, rate)
    print(f"Pay: {gross_pay:.2f}")
    
except ValueError:
    print("Error: Please enter a valid numeric value.")
