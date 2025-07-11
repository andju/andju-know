---
published: true
---
# Garmin Epix Pro
When I looked for a digital sports watch one thing was important for me: I don't want to upload (sensitive) health and activity data into a cloud. I came across Garmin watches since they provide good quality and the ability to access their files via USB. Almost all data is stored in the [.fit format](https://developer.garmin.com/fit/overview/).

## .fit software
Software products that help managing and/or visualizing the data in .fit files.

### Single file
Open and visualize individual .fit files.

- [fitplotter](https://github.com/karaul/fitplotter)
- [GPXSee](https://www.gpxsee.org/)

### Management
Software to keep track of your activities.

- [Geo Activity Playground](https://martin-ueding.github.io/geo-activity-playground/): Promising solution to keep track of your activities. Unfortunately I wasn't able to get it to work.
- [GoldenCheetah](https://www.goldencheetah.org/): For statistic lovers. Shows various performance statistics, focussing on running and cycling.
- [Turtle Sport](https://turtlesport.sourceforge.io/EN/home.html): Visualize your various outdoor activities on a map. Seems to have problems showing heart rates. No new versions since 2017.

## Tips and tricks

### Wrong altitude in the morning
The watch calibrates the altitude every night. If your phone is not connected (e.g. in flight mode) and you slept at different altitudes in the last days (e.g. during travel) the altitude might be calibrated to a wrong level. This even happens if it was correct when you went to bed.

To fix this, you need to calibrate the altitude [manually](https://www8.garmin.com/manuals/webhelp/GUID-E5C62F3F-DCE3-4197-8CA5-E419B2A55D12/EN-US/GUID-BC734846-01A7-4F33-86D4-DFBDBC06CDB4.html)  (Use DEM). It works best if you are doing this before you go to sleep, outside and on ground level. You might have to open Garmin Connect on your phone during the calibration.