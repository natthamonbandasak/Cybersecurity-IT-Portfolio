# Parse email logs to extract sender domains and track their frequency in an SQLite database

import sqlite3

# Connect to the SQLite database (creates the file if it doesn't exist)
conn = sqlite3.connect('domain_activity.sqlite')
cur = conn.cursor()

# Initialize the database table
cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

fname = input('Enter log file name (e.g., mbox.txt): ')

try:
    with open(fname, 'r') as fh:
        print("Parsing log file and updating database...")
        for line in fh: 
            line = line.strip()
            
            # Extract sender email domain from lines starting with 'From '
            if line.startswith('From '):
                words = line.split()
                if len(words) >= 2:
                    email = words[1]
                    domain = email.split('@')[1]

                    # Check if the domain already exists in the database
                    cur.execute('SELECT count FROM Counts WHERE org = ?', (domain,))
                    row = cur.fetchone()
                    
                    if row is None:
                        # Insert a new domain record
                        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain,))
                    else:
                        # Update the existing domain's count
                        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain,))

        # Commit the transaction to save changes
        conn.commit()
        
        # Display the top 5 results to verify success
        print("\n--- Top 5 Active Domains ---")
        for row in cur.execute('SELECT org, count FROM Counts ORDER BY count DESC LIMIT 5'):
            print(f"{row[0]}: {row[1]}")

except FileNotFoundError:
    print(f"Error: File cannot be found or opened: {fname}")

# Close the connection securely
cur.close()
conn.close()
