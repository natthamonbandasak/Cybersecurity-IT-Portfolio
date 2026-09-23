# Dynamically extract and parse a numeric value from a formatted log string

data = "X-DSPAM-Confidence:    0.8475"

try:
    # Find the position of the colon delimiter
    ipos = data.find(':')
    
    if ipos != -1:
        # Slice everything after the colon and strip any extra whitespaces
        piece = data[ipos + 1:].strip()
        value = float(piece)
        print(f"Extracted Confidence Value: {value}")
    else:
        print("Error: Delimiter ':' not found in string.")
        
except ValueError:
    print("Error: Could not convert the extracted text to a float.")
