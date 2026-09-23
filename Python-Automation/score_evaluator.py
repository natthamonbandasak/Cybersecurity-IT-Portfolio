# Evaluate student score and assign a grade based on predefined criteria

try:
    score = float(input("Enter Score: "))
    
    # Check if the score is within the valid range (0.0 to 1.0)
    if 0.0 <= score <= 1.0:
        if score >= 0.9:
            print('Grade: A')
        elif score >= 0.8:
            print('Grade: B')
        elif score >= 0.7:
            print('Grade: C')
        elif score >= 0.6:
            print('Grade: D')
        else:
            print('Grade: F')
    else:
        print("Error: Score must be between 0.0 and 1.0.")
        
except ValueError:
    print("Error: Please enter a valid numerical score.")
