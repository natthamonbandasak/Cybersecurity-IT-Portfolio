#!/bin/bash

# Extract the accuracy values for the last 7 days directly into an array
week_fc=($(tail -7 synthetic_historical_fc_accuracy.tsv | cut -f6))

# Convert all error values to absolute numbers
for i in {0..6}; do
  if [[ ${week_fc[$i]} -lt 0 ]]; then
    week_fc[$i]=$(( -1 * week_fc[$i] ))
  fi
done

# Initialize min and max variables with the first element of the array (index 0)
minimum=${week_fc[0]}
maximum=${week_fc[0]}

# Calculate the minimum and maximum absolute errors
for item in "${week_fc[@]}"; do
   if [[ $minimum -gt $item ]]; then
     minimum=$item
   fi
   if [[ $maximum -lt $item ]]; then
     maximum=$item
   fi
done

# Output the final statistics
echo "Minimum absolute error = $minimum"
echo "Maximum absolute error = $maximum"
