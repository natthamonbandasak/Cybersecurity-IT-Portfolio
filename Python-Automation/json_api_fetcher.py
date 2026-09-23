# Fetch JSON data from a REST API endpoint and parse specific key-value pairs

import urllib.request
import urllib.error
import json

url = input('Enter API endpoint URL (JSON format): ')

try:
    print(f"Connecting to: {url}...")
    response = urllib.request.urlopen(url)
    
    # Read and decode the response to a UTF-8 string
    data = response.read().decode('utf-8')
    print(f"Successfully retrieved {len(data)} characters.")
    
    # Parse the JSON data into a Python dictionary
    info = json.loads(data)
    
    total = 0
    valid_records = 0
    
    # Check if the expected key exists in the JSON structure
    if 'comments' in info:
        for item in info['comments']:
            try:
                # Use .get() to avoid KeyError if 'count' is missing
                total += int(item.get('count', 0))
                valid_records += 1
            except ValueError:
                continue
                
        print("\n--- JSON Parsing Complete ---")
        print(f"Total records processed: {valid_records}")
        print(f"Sum of counts: {total}")
    else:
        print("Error: The expected 'comments' key was not found in the JSON payload.")

except urllib.error.URLError as e:
    print(f"Network Error: Failed to retrieve data. Details: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Parsing Error: The retrieved data is not valid JSON. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
