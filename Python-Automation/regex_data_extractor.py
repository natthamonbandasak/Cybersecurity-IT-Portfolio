# Extract all numeric values from a text file using Regular Expressions and calculate their sum

import re

fname = input('Enter file name (e.g., sample_data.txt): ')

try:
    # Using 'with open' ensures the file is properly closed automatically after processing
    with open(fname, 'r') as hand:
        total = 0
        
        for line in hand:
            line = line.strip()
            
            # Find all occurrences of one or more digits in the current line
            numbers = re.findall('[0-9]+', line)
            
            # Convert extracted strings to integers and add to the running total
            if numbers:
                total += sum([int(num) for num in numbers])
                
        print(f"\nData Extraction Complete.")
        print(f"Total Sum of all extracted numbers: {total}")
        
except FileNotFoundError:
    print(f"Error: File cannot be found or opened: {fname}")
