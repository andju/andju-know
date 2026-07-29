---
published: true
---
# Crash and Reboot (loop)
If your Garmin watch has been spontaneously restarting this issue can have several possible causes. Below is one fix that has worked in practice, worth trying before you go down the rabbit hole of factory resets or warranty claims.

## The Symptom
The watch behaves normally most of the time, but under specific triggers it reboots unexpectedly:

- **Disconnecting the charging cable:** You unplug the watch and instead of returning to the watch face, it restarts (potentially into a [boot loop](fix-crash-and-reboot-loop.md#end-a-boot-loop-by-factory-reset)).
- **Starting an activity:** You select a sport profile and hit the start button, and the watch reboots instead of beginning to record.

## Too Many Stored Activity Files
Like most software bugs, this one can have multiple root causes, and Garmin's firmware is complex enough that no single explanation covers every case. But there's a pattern worth checking first: **a large backlog of unsynced or unarchived `.fit` activity files sitting on the watch.**

In multiple cases, this reboot issue was resolved by manually deleting old activity files directly from the device. Usually, the watch had accumulated roughly **100 stored activities** before the problem started.

The theory is straightforward: as the number of `.fit` files builds up, something in the watch's internal handling of that storage - indexing, reading, or writing during charge-cycle or activity-start events - gets bogged down or hits an edge case, triggering a crash and reboot.

## How to Fix It

1. **Connect the watch to your computer via USB** and open the drive in a file browser.
2. **Navigate to the activity folder**, typically found at: `GARMIN/ACTIVITY/`
3. **Back up the `.fit` files locally** by copying them to a folder on your computer before deleting anything.
4. **Delete the `.fit` files** for old activities you've backed up. You don't need to remove everything - just clear out the bulk of the backlog.
5. **Safely eject and disconnect** the watch, then test the behavior that used to trigger the reboot (unplug the charger, start an activity).

If you're dealing with random reboots and haven't checked your on-device activity count in a while, it's a five-minute troubleshooting step that's worth trying before anything more drastic.

## End a Boot Loop by Factory Reset

> [!danger] Data loss
> A factory reset will erase data stored on the watch, so use this only as a last resort once you've backed up what you can.

If the reboots have escalated to the point where the watch is stuck in a continuous boot loop and won't respond normally, you can force a factory reset using a button combination. This method comes from [androidauthority.com](https://www.androidauthority.com/garmin-smartwatches-bootloop-issue-3520875/):

1. Power off the watch by holding the **Light** button (top left) for up to thirty seconds.
2. Press and hold the **Back** button (bottom right) and **Start/Stop** button (top right).
3. Press the **Light** button briefly to power on the watch while holding the other buttons.
4. On a beep, release the **Start/Stop** button.
5. Once the second beep, release the **Back** button.