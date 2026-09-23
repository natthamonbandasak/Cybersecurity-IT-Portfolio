# Query a REST API with URL parameters, parse nested JSON, and extract specific geographical data

import urllib.request
import urllib.parse
import json
import ssl

# Ignore SSL certificate errors (useful for internal corporate networks or testing)
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Using a public test API for demonstration purposes
api_endpoint = 'http://py4e-data.dr-chuck.net/opengeo?'

print("--- Geo-Location API Fetcher ---")
print("Type 'quit' to exit.")

while True:
    address = input('\nEnter location to search: ').strip()
    if address.lower() in ['quit', 'exit', '']: 
        break

    # Safely encode URL parameters
    parms = {'q': address}
    url = api_endpoint + urllib.parse.urlencode(parms)

    try:
        print(f"Retrieving data from API: {url}")
        response = urllib.request.urlopen(url, context=ctx)
        data = response.read().decode('utf-8')
        
        # Parse the JSON response
        js = json.loads(data)

        # Validate the expected JSON structure
        if not js or 'features' not in js or len(js['features']) == 0:
            print("Error: Could not retrieve valid location data. Please try another query.")
            continue

        # Extract the nested plus_code safely
        properties = js['features'][0].get('properties', {})
        plus_code = properties.get('plus_code')
        
        if plus_code:
            print(f"Location Found! Plus Code: {plus_code}")
        else:
            print("Notice: No Plus Code found for this specific location.")

    except urllib.error.URLError as e:
        print(f"Network Error: Failed to connect to the API. Details: {e}")
    except json.JSONDecodeError:
        print("Data Error: The API did not return valid JSON.")
    except IndexError:
        print("Data Error: The API response format was unexpected.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
