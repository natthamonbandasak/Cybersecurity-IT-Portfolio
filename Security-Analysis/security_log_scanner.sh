#!/bin/bash

# =====================================================================
# Script Name: security_log_scanner.sh
# Description: A lightweight Bash script to scan system logs for 
#              failed login attempts, errors, and potential security threats.
# Author: Security Analyst Portfolio Project
# =====================================================================

# Check if a log file was provided as an argument
if [ "$#" -ne 1 ]; then
    echo "[-] Usage: $0 <path_to_log_file>"
    exit 1
fi

LOG_FILE=$1

# Check if the file actually exists
if [ ! -f "$LOG_FILE" ]; then
    echo "[-] Error: File '$LOG_FILE' not found!"
    exit 1
fi

echo "====================================================="
echo "[+] Starting Security Log Analysis on: $LOG_FILE"
echo "====================================================="

# 1. Count total log entries
TOTAL_LINES=$(wc -l < "$LOG_FILE")
echo "[*] Total Log Entries: $TOTAL_LINES"

# 2. Count failed login or error attempts
FAILED_COUNT=$(grep -i -E "fail|error|unauthorized" "$LOG_FILE" | wc -l)
echo "[!] Potential Threats / Errors Found: $FAILED_COUNT"

echo "-----------------------------------------------------"
echo "[+] Summary of Suspicious Events:"
echo "-----------------------------------------------------"

# 3. Display matching suspicious lines (limited to top 10 for readability)
grep -i -E "fail|error|unauthorized" "$LOG_FILE" | head -n 10

echo "====================================================="
echo "[+] Scan Completed Successfully."
echo "====================================================="
