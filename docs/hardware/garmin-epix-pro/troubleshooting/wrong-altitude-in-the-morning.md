---
published: true
---
# Wrong altitude in the morning
You get home from a hike, phone goes into flight mode overnight (or just loses connection), and by morning the altimeter has quietly recalibrated itself to the wrong elevation - even though it was reading correctly when you went to bed.

## What's Happening
Garmin watches auto-calibrate the altimeter every night, correcting for barometric drift using GPS and phone-assisted elevation data. If the phone isn't reachable, the watch falls back on recent elevation history instead - including the point where you went to bed the day before. Result: it wakes up "calibrated" to your previous nights altitude instead of your actual home elevation.

## How to Fix It
Calibrate manually before bed, using **DEM** ([instructions here](https://www8.garmin.com/manuals/webhelp/GUID-E5C62F3F-DCE3-4197-8CA5-E419B2A55D12/EN-US/GUID-BC734846-01A7-4F33-86D4-DFBDBC06CDB4.html)):

- **Do it in the evening**, after you're back and settled - not in the morning after the damage is done.
- **Do it outside**, so the watch gets a clean GPS fix.
- **Do it at ground level**, not upstairs - DEM data reflects terrain, not floor height.
- **Make sure the watch is connected to your phone**, with Garmin Connect open. The DEM lookup requires that connection to fetch elevation data.