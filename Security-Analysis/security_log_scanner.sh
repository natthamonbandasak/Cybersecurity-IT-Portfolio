#!/bin/bash

# =====================================================================
# Script Name: security_log_scanner.sh
# Description: A security utility to check file integrity (SHA-256 Hash),
#              count total entries, and scan logs for potential threats.
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
echo "[+] Starting Security Analysis on: $LOG_FILE"
echo "====================================================="

# 1. File Integrity Check: Generate and display SHA-256 Hash
echo "[*] Calculating File Integrity (SHA-256 Hash)..."
FILE_HASH=$(sha256sum "$LOG_FILE" | awk '{print $1}')
echo "[+] SHA-256 Hash: $FILE_HASH"
echo "-----------------------------------------------------"

# 2. Count total log entries
TOTAL_LINES=$(wc -l < "$LOG_FILE")
echo "[*] Total Log Entries: $TOTAL_LINES"

# 3. Count failed login or error attempts
FAILED_COUNT=$(grep -i -E "fail|error|unauthorized" "$LOG_FILE" | wc -l)
echo "[!] Potential Threats / Errors Found: $FAILED_COUNT"

echo "-----------------------------------------------------"
echo "[+] Summary of Suspicious Events:"
echo "-----------------------------------------------------"

# 4. Display matching suspicious lines (limited to top 10 for readability)
grep -i -E "fail|error|unauthorized" "$LOG_FILE" | head -n 10

echo "====================================================="
echo "[+] Scan & Integrity Check Completed Successfully."
echo "====================================================="
