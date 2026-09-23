# Parse a log file to extract, accumulate, and calculate the average of specific confidence metrics

fname = input('Enter file name (e.g., mbox-short.txt): ')

try:
    fh = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

count = 0
total = 0.0

for line in fh:
    line = line.strip()
    
    # Filter lines that start with the target metric prefix
    if line.startswith('X-DSPAM-Confidence:'):
        ipos = line.find(':')
        number_str = line[ipos + 1:].strip()
        
        try:
            number = float(number_str)
            total += number
            count += 1
        except ValueError:
            # Skip rows where the value cannot be converted to a float
            continue

fh.close()

# Calculate and display the final average if valid records exist
if count > 0:
    average = total / count
    print(f'\nTotal Records Processed: {count}')
    print(f'Average Confidence Score: {average:.4f}')
else:
    print('No matching lines or valid numeric data found.')
