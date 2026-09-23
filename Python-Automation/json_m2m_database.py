# Parse a JSON roster file and populate a Many-to-Many relational SQLite database

import json
import sqlite3

# Establish connection and create cursor
conn = sqlite3.connect('roster_m2m.sqlite')
cur = conn.cursor()

# Set up the relational database schema (User, Course, and Member junction table)
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER PRIMARY KEY AUTOINCREMENT,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

fname = input('Enter JSON file name (e.g., roster_data.json): ')
if len(fname) < 1:
    fname = 'roster_data.json'

try:
    with open(fname, 'r') as file:
        str_data = file.read()
        json_data = json.loads(str_data)

    print("Populating relational database from JSON...")

    # Iterate through the JSON array to extract user, course, and role
    for entry in json_data:
        name = entry[0]
        title = entry[1]
        role = entry[2]

        # Insert User and retrieve generated ID
        cur.execute('INSERT OR IGNORE INTO User (name) VALUES ( ? )', (name, ))
        cur.execute('SELECT id FROM User WHERE name = ? ', (name, ))
        user_id = cur.fetchone()[0]

        # Insert Course and retrieve generated ID
        cur.execute('INSERT OR IGNORE INTO Course (title) VALUES ( ? )', (title, ))
        cur.execute('SELECT id FROM Course WHERE title = ? ', (title, ))
        course_id = cur.fetchone()[0]

        # Map User and Course in the Member junction table
        cur.execute('''INSERT OR REPLACE INTO Member
            (user_id, course_id, role) VALUES ( ?, ?, ? )''',
            (user_id, course_id, role))

    # Commit all transactions
    conn.commit()
    print("Database successfully built and populated.")

except FileNotFoundError:
    print(f"Error: Could not locate file {fname}")
except json.JSONDecodeError:
    print("Error: The file is not a valid JSON format.")

# Close connection
conn.close()
