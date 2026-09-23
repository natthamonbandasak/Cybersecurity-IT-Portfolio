# Open, read, and process text files line by line with error handling

fname = input('Enter file name: ')

try: 
    fhand = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

for line in fhand:
    # Clean trailing whitespaces and convert text to uppercase
    processed_line = line.rstrip().upper()
    print(processed_line)

# Ensure the file handle is safely closed
fhand.close()
