# Open a file, extract unique words, sort them alphabetically, and display the result

fname = input('Enter file name (e.g., romeo.txt): ')

try:
    fh = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

words = []

for line in fh:
    line = line.strip()
    line_words = line.split()
    
    for word in line_words:
        # Filter out duplicates and append to the list
        if word not in words:
            words.append(word)

fh.close()

# Sort the unique words alphabetically
words.sort()

print("\nUnique Sorted Words:")
print(words)
