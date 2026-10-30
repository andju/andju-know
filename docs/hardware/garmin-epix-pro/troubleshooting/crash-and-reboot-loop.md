---
published: true
---
# Crash and Reboot (loop)
If your Garmin watch has been spontaneously restarting this issue can have several possible causes. Below is one fix that has worked in practice, worth trying before you go down the rabbit hole of factory resets or warranty claims.

## The Symptom
The watch behaves normally most of the time, but under specific triggers it reboots unexpectedly:

- **Disconnecting the charging cable:** You unplug the watch and instead of returning to the watch face, it restarts (potentially into a [boot loop](fix-crash-and-reboot-loop.md#end-a-boot-loop-by-factory-reset)).
- **Starting an activity:** You select a sport profile and hit the start button, and the watch reboots instead of beginning to record.

## Too Many Stored .fit Files
Like most software bugs, this one can have multiple root causes, and Garmin's firmware is complex enough that no single explanation covers every case. But there's a pattern worth checking first: **a large number of `.fit` files sitting on the watch.**

The theory is straightforward: as the number of `.fit` files builds up, something in the watch's internal handling of that storage - indexing, reading, or writing during charge-cycle or activity-start events - gets bogged down or hits an edge case, triggering a crash and reboot.

Further troubleshooting showed that it's not only the activity files that count towards the limit, but **all `.fit` files on the watch**. In addition, starting with firmware version **26.09**, the `.fit` files in the following folders are no longer cleaned up automatically if they haven't been synced with Garmin Connect:

| Folder             | What it (most likely) stores                                                                                                                                                                                                                                                                                                                       |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `GARMIN/SkinTemp/` | Overnight **skin temperature** readings used for Garmin's skin temperature feature.                                                                                                                                                                                                                                                                |
| `GARMIN/Sleep/`    | **Sleep tracking** data recorded on the watch.                                                                                                                                                                                                                                                                                                     |
| `GARMIN/SlpDisr/`  | **Unconfirmed.** The name most likely abbreviates _sleep disruption(s)_. A plausible candidate is the overnight [breathing variations](https://www8.garmin.com/manuals/webhelp/GUID-E5C62F3F-DCE3-4197-8CA5-E419B2A55D12/EN-US/GUID-636632DF-E3E8-4C15-936A-CFB7EA2B5C39.html) data, which the Epix measures with its pulse oximeter during sleep. |

Normally each of these folders contains only **six files**. If the cleanup doesn't happen, they grow by one file per night and quietly push the total `.fit` count towards the point where the reboots start.

## How to Fix It

1. **Connect the watch to your computer via USB** and open the drive in a file browser. Make sure that the USB Mode of the watch is set to MTP.
2. **Check the number of `.fit` files** in these folders:
    - `GARMIN/ACTIVITY/` - your recorded activities
    - `GARMIN/SkinTemp/`
    - `GARMIN/Sleep/`
    - `GARMIN/SlpDisr/`
3. **Back up the `.fit` files locally** by copying them to a folder on your computer before deleting anything.
4. **Delete the `.fit` files** you've backed up:
    - In `ACTIVITY`, remove old activities. You don't need to remove everything - just clear out the bulk of the backlog.
    - In `SkinTemp`, `Sleep` and `SlpDisr`, keep the six most recent files and delete the older ones.
5. **Safely eject and disconnect** the watch, then test the behavior that used to trigger the reboot (unplug the charger, start an activity).

If you're dealing with random reboots and haven't checked your on-device `.fit` file count in a while, it's a five-minute troubleshooting step that's worth trying before anything more drastic.

## End a Boot Loop by Factory Reset

> [!danger] Data loss
> A factory reset will erase data stored on the watch, so use this only as a last resort once you've backed up what you can.

If the reboots have escalated to the point where the watch is stuck in a continuous boot loop and won't respond normally, you can force a factory reset using a button combination. This method comes from [androidauthority.com](https://www.androidauthority.com/garmin-smartwatches-bootloop-issue-3520875/):

1. Power off the watch by holding the **Light** button (top left) for up to thirty seconds.
2. Press and hold the **Back** button (bottom right) and **Start/Stop** button (top right).
3. Press the **Light** button briefly to power on the watch while holding the other buttons.
4. On a beep, release the **Start/Stop** button.
5. Once the second beep, release the **Back** button.