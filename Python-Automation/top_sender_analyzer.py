# Parse a log file to extract senders and find the most frequent sender using a dictionary

fname = input('Enter file name (e.g., mbox-short.txt): ')

try:
    fh = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

email_counts = dict()

# Extract emails and count their frequencies
for line in fh:
    line = line.strip()
    
    if line.startswith('From '):
        words = line.split()
        if len(words) >= 2:
            email = words[1]
            # Add new email to dictionary or increment existing count
            email_counts[email] = email_counts.get(email, 0) + 1

fh.close()

# Find the email address with the highest frequency
max_count = None
max_email = None

for email, count in email_counts.items():
    if max_count is None or count > max_count:
        max_email = email
        max_count = count

# Display the final result
if max_email is not None:
    print(f'\nTop Sender: {max_email}')
    print(f'Total Emails Sent: {max_count}')
else:
    print('\nNo sender data found in the file.')
