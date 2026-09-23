# Extract and count sender email addresses from a mail log file

fname = input('Enter file name (e.g., mbox-short.txt): ')

try:
    fh = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

count = 0

for line in fh:
    line = line.strip()
    
    # Filter lines starting with 'From ' (note the space to target sender lines)
    if line.startswith('From '):
        words = line.split()
        
        # Ensure the list has enough elements to avoid IndexError
        if len(words) >= 2:
            print(words[1])
            count += 1

fh.close()

print(f'\nTotal processed: There were {count} lines in the file with "From" as the second word indicator.')
