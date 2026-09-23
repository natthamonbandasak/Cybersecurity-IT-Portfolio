# Fetch XML data from a URL, parse the XML tree, and extract specific node values

import urllib.request
import urllib.error
import xml.etree.ElementTree as ET

url = input('Enter XML data URL: ')

try:
    print(f"Connecting to: {url}...")
    response = urllib.request.urlopen(url)
    data = response.read()
    
    print(f"Successfully retrieved {len(data)} characters.")
    
    # Parse the raw data into an XML tree
    tree = ET.fromstring(data)
    
    # Find all elements named 'count' anywhere in the tree
    counts = tree.findall('.//count')
    
    total = 0
    valid_nodes = 0
    
    for count in counts:
        try:
            total += int(count.text)
            valid_nodes += 1
        except ValueError:
            # Skip nodes where the text isn't a valid integer
            continue

    print("\n--- Extraction Complete ---")
    print(f"Total <count> nodes processed: {valid_nodes}")
    print(f"Sum of all counts: {total}")

except urllib.error.URLError as e:
    print(f"Network Error: Failed to retrieve data. Details: {e}")
except ET.ParseError as e:
    print(f"XML Parsing Error: The retrieved data is not a valid XML format. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
