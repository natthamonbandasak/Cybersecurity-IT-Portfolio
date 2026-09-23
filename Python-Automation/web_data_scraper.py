# Scrape web page data, parse HTML using BeautifulSoup, and extract numeric values from span tags

import urllib.request
import urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors (useful for internal/testing environments)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter URL: ')

try:
    print(f"Connecting to {url}...")
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Retrieve all <span> tags
    tags = soup('span')
    count = 0
    total = 0
    
    for tag in tags:
        try:
            # Attempt to convert the text inside the span to an integer
            number = int(tag.text)
            total += number
            count += 1
        except ValueError:
            # Skip tags that do not contain valid integers
            continue
            
    print(f"\n--- Scraping Complete ---")
    print(f"Count of valid numbers found: {count}")
    print(f"Total Sum: {total}")
    
except urllib.error.URLError as e:
    print(f"Network/URL Error: Failed to retrieve data. Details: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
