#!/bin/bash

# Define target city and timezone
city="Casablanca"
TZ="Africa/Casablanca"

# Fetch the weather report and save it to a local file
curl -s "wttr.in/$city?T" --output weather_report

# Extract Current Temperature from the downloaded file
obs_temp=$(grep -m 1 '°.' weather_report | grep -Eo -e '-?[[:digit:]].*')
echo "The current temperature of $city: $obs_temp"

# Extract the forecast temperature for noon tomorrow
fc_temp=$(head -23 weather_report | tail -1 | grep '°.' | cut -d 'C' -f2 | grep -Eo -e '-?[[:digit:]].*')
echo "The forecast for noon tomorrow for $city: $fc_temp C"

# Extract current day, month, and year using the specified timezone
day=$(TZ=$TZ date +%d)
month=$(TZ=$TZ date +%m)
year=$(TZ=$TZ date +%Y)

# Record data as a tab-separated row in the log file
record=$(echo -e "$year\t$month\t$day\t$obs_temp\t$fc_temp C")
echo "$record" >> rx_poc.log
