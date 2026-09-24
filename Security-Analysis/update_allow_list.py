# =====================================================================
# Project: Algorithm for file updates in Python
# Description: Automates the removal of restricted IP addresses from an allow list.
# =====================================================================

# List of IP addresses that need to be removed from the access list
remove_list = ["192.168.97.225", "192.168.158.170", "192.168.201.40", "192.168.58.57"]

# Assign the file name to a variable
import_file = "allow_list.txt"

# Open the file and read its contents
with open(import_file, "r") as file:
    ip_addresses = file.read()

# Convert the string into a list to easily remove individual IPs
ip_addresses = ip_addresses.split()

# Iterate through the remove_list and remove matching IPs
for element in remove_list:
    if element in ip_addresses:
        ip_addresses.remove(element)

# Convert the updated list back into a string, each IP on a new line
ip_addresses = "\n".join(ip_addresses)

# Overwrite the original file with the updated string
with open(import_file, "w") as file:
    file.write(ip_addresses)

print("[+] Security Update Complete: Unauthorized IPs have been removed from allow_list.txt")
