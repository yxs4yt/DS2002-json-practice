
#retrieve data
curl -s "https://aviationweather.gov/api/data/metar?ids=KMCI&format=json&taf=false&hours=12&bbox=40%2C-90%2C45%2C-85" > aviation.json

#print first 6 receipt times"
jq -r '.[].receiptTime' aviation.json | head -6

#calculate average temperature
avg=$(jq '[.[].temp | select(. != null)] | add / length' aviation.json)
printf "Average Temperature: %.1f\n" "$avg"


#cloudy conditions
clear_count=$(jq -r '.[].clouds[0].cover' aviation.json | grep -c "CLR")
total=$(jq 'length' aviation.json)
cloudy_count=$(( total - clear_count ))
if [ " $cloudy_count" -gt $(( total / 2 )) ]; then
  echo "Mostly Cloudy: true"
else
  echo "Mostly Cloudy: false"
fi

