---
published: true
---
# Backup and Restore
A Garmin watch is a fully functional USB storage device on its own, which allows you to create a truly local backup.

## The Core Idea
Plug the watch into a PC or Mac via USB and it mounts as an MTP storage device, exposing its internal file system. Everything the watch tracks (workouts, sleep, daily stats, settings) lives here as ordinary files, mostly in Garmin's `.fit` format.

Garmin publishes a support article covering part of this process, _[Can I Copy or Back Up My Information and Settings on My Garmin Device?](https://support.garmin.com/en-US/?faq=AXV7LuWgc73v21nq6nbDa6)_, but it only documents a subset of what actually works. In practice, the `NEWFILES` restore mechanism also brings back activity history, HRV data, and sleep data - not just the settings and locations officially listed.

Caveats to keep in mind:

- **Not all state is file-based.** Some configuration lives in an internal database not exposed over MTP, so a few settings simply can't be captured this way.
- **Firstbeat analytics and cumulative totals (e.g. lifetime step counts) don't restore:** They're recalculated over time rather than stored as a static file.
- **Wi-Fi and Bluetooth pairings never restore automatically**, even with the `SETTINGS` folder copied back - you'll re-pair these by hand.

## How it works

1. **Connect the watch via USB.**
2. **Copy the whole `GARMIN` folder** to your computer. This is your complete offline backup.
3. **To restore** (after a reset, or onto a replacement unit of the same model): Connect the watch and copy `.fit` files from your saved folders into `NEWFILES`.
4. **Disconnect and let the watch process the folder.** It imports what it can and empties `NEWFILES` on its own.