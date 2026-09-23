# Recursively crawl web pages by extracting and following specific anchor tags

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (useful for internal/testing environments)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter starting URL: ')

try:
    count = int(input('Enter count (how many links to follow): '))
    position = int(input('Enter position (which link to click on each page): '))
except ValueError:
    print("Error: Count and position must be valid integers.")
    exit()

print(f"\nStarting sequence from: {url}")

for i in range(count):
    try:
        html = urllib.request.urlopen(url, context=ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        
        tags = soup('a')
        
        # Verify if the page contains enough anchor tags
        if len(tags) < position:
            print(f'Error: Page only contains {len(tags)} links, cannot reach position {position}.')
            break
            
        # Adjust position for Python's zero-based indexing
        tag = tags[position - 1]
        url = tag.get('href', None)
        print(f"Retrieving step {i + 1}: {url}")
        
        # Display the final target data on the last iteration
        if i == count - 1:
            print("\n--- Crawl Complete ---")
            print(f"Target data found: {tag.text}")
            
    except urllib.error.URLError as e:
        print(f"Network Error: Failed to retrieve {url}. Details: {e}")
        break
