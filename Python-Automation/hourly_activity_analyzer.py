# Parse a log file to extract the hour from timestamps and analyze peak activity times

fname = input('Enter file name (e.g., mbox-short.txt): ')

try:
    fh = open(fname, 'r')
except FileNotFoundError:
    print(f'Error: File cannot be found or opened: {fname}')
    exit()

hourly_counts = dict()

for line in fh:
    line = line.strip()
    
    # Target lines that indicate a sender and timestamp
    if line.startswith('From '):
        words = line.split()
        
        # Ensure the line has enough data to contain a timestamp at index 5
        if len(words) >= 6:
            time_str = words[5]         
            # Extract only the two-digit hour before the first colon
            hour = time_str.split(':')[0]
            hourly_counts[hour] = hourly_counts.get(hour, 0) + 1

fh.close()

# Display the activity distribution sorted by hour
print("\n--- Hourly Activity Report ---")
print("Hour  |  Event Count")
print("-" * 28)

for hour in sorted(hourly_counts):
    print(f"{hour}    |  {hourly_counts[hour]}")
