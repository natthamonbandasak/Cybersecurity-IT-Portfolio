#!/bin/bash

# Initialize the historical accuracy report with column headers
echo -e "Year\tMonth\tDay\tToday_Temp\tYesterday_FC\tAccuracy\tAccuracy_Range" > historical_fc_accuracy.tsv

# Count the total number of records in the log file
total_rows=$(wc -l < rx_poc.log)

# Iterate through the log file to calculate accuracy for each consecutive day
for (( i=2 ; i<=$total_rows; i++ ))
do
    # Extract data for consecutive days
    yesterday_row=$(head -n $(( i-1)) rx_poc.log | tail -n 1)
    today_row=$(head -n $i rx_poc.log | tail -n 1)

    # Parse forecasted and actual temperatures
    yesterday_fc=$(echo "$yesterday_row" | cut -f5)
    today_temp=$(echo "$today_row" | cut -f4)

    # Calculate forecast accuracy margin
    accuracy=$((yesterday_fc - today_temp))

    # Categorize the accuracy based on the margin of error
    if [ -1 -le $accuracy ] && [ $accuracy -le 1 ]; then
        accuracy_range="excellent"
    elif [ -2 -le $accuracy ] && [ $accuracy -le 2 ]; then
        accuracy_range="good"
    elif [ -3 -le $accuracy ] && [ $accuracy -le 3 ]; then
        accuracy_range="fair"
    else
        accuracy_range="poor"
    fi

    # Parse date components
    year=$(echo "$today_row" | cut -f1)
    month=$(echo "$today_row" | cut -f2)
    day=$(echo "$today_row" | cut -f3)

    # Append the processed record to the TSV report
    echo -e "$year\t$month\t$day\t$today_temp\t$yesterday_fc\t$accuracy\t$accuracy_range" >> historical_fc_accuracy.tsv
done
