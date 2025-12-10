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
- [Fit ConVerter](https://www.pinns.co.uk/osm/fit.html): Version 4.6 seems to have various problems with visualizing and exporting data
- [GPXSee](https://www.gpxsee.org/)

### Management
Software to keep track of your activities.

- [Garmin Grafana](https://github.com/arpanghosh8453/garmin-grafana): Fetch data from Garmin servers and store the data in a local database for visualization with Grafana. ⚠ You need to upload your data to the Garmin servers first.
- [Geo Activity Playground](https://martin-ueding.github.io/geo-activity-playground/): Promising solution to keep track of your activities. Unfortunately I wasn't able to get it to work.
- [GoldenCheetah](https://www.goldencheetah.org/): For statistic lovers. Shows various performance statistics, focussing on running and cycling.
- [Turtle Sport](https://turtlesport.sourceforge.io/EN/home.html): Visualize your various outdoor activities on a map. Version 2.0 seems to have problems showing heart rates. No new versions since 2017.

## Troubleshooting
Helpful links:

- [Owner's manual](https://www8.garmin.com/manuals/webhelp/GUID-E5C62F3F-DCE3-4197-8CA5-E419B2A55D12/EN-US/GUID-CA57BF17-793A-403C-B89E-F7B2E93D340A-homepage.html)
- [Garmin Watch Optical Heart Rate Accuracy Tips](https://support.garmin.com/en-US/?faq=xQwjQjzUew4BF1GYcusE59)
- [Can I Copy or Back Up My Information and Settings on My Garmin Device?](https://support.garmin.com/en-US/?faq=AXV7LuWgc73v21nq6nbDa6)

### Boot loop
If the watch is stuck in a boot loop, it can be factory reset the following way (based on [androidauthority.com](https://www.androidauthority.com/garmin-smartwatches-bootloop-issue-3520875/)):

1. Power off the watch by holding the *Light* button (top left) for up to thirty seconds.
2. Press and hold the *Back* button (bottom right) and *Start/Stop* button (top right).
3. Press the *Light* button briefly to power on the watch while holding the other buttons.
4. On a beep, release the *Start/Stop* button.
5. Once the second beep, release the *Back* button.

### Wrong altitude in the morning
**Problem:** The watch calibrates the altitude every night. If your phone is not connected (e.g. in flight mode) and you slept at different altitudes in the last days (e.g. during travel) the altitude might be calibrated to a wrong level. This even happens if it was correct when you went to bed.

**Solution:** Calibrate the altitude [manually](https://www8.garmin.com/manuals/webhelp/GUID-E5C62F3F-DCE3-4197-8CA5-E419B2A55D12/EN-US/GUID-BC734846-01A7-4F33-86D4-DFBDBC06CDB4.html)  (Use DEM). It works best if you are doing this before you go to sleep, outside and on ground level. You might have to open Garmin Connect on your phone during the calibration.