---
published: true
---
# Course not synced
You plan a route, tap **Send to Device**, the app cheerfully tells you it will be on your watch after the next sync - and then nothing. The watch is connected. Notifications work. The sync animation runs. But `Navigation → Courses` stays exactly as empty as it was yesterday. No error, no warning, no clue.

If you use a Garmin watch deliberately _offline_ - sync to Garmin Connect disabled - you are more likely to run into this situation.

> [!info] Synchronization
> Garmin does not document the internals of its sync pipeline, so the mechanism described here is inferred from reproducible external behavior - not from source code. The fix, however, is reproducible, and that is what counts at 6 a.m. when the route is supposed to be on your wrist.

## How Synchronization works
The important thing to understand: **"Send to Device" is not a direct transfer.** Nothing is pushed the moment you tap it. The item is placed in a queue, and that queue is only drained during a regular device sync - the same sync session that pulls new activity files off the watch, updates settings, and pushes the weather.

That is a single pipeline, and it is strictly sequential. Which means one wedged item at the head of the queue takes down _everything_ behind it: courses, workouts, training calendar, settings changes. And because the app has already told you "it'll be there after the sync," it never sees a reason to complain again.

## A missing error as the actual symptom
Here is the counter-intuitive part, and the strongest evidence for a stuck sync session.

The **"Sync Failed"** toast only ever appears at _disconnect_ — when you walk away from the phone while the watch is carrying activities that did not exist when the connection was established. It never appears during an active connection. That is exactly the signature of a sync session that was started, ran into an aborted Bluetooth link, and was then properly cleaned up: the app noticed the transfer died, reported it, and reset its state machine to idle. Annoying message, healthy app.

The failure mode is the _silent_ disconnect. When you walk away under the same conditions and **no** message appears, the abort went unnoticed. From the app's point of view the sync never ended — it is still "in progress" for a device that is long gone. Every later sync request is either short-circuited ("already running") or queued behind a transfer that can never complete. Your course joins that queue and stays there.

There is a second deduction worth spelling out: **this state survives force-closing the app or rebooting the phone.** If it did not, killing the app would fix it — and it doesn't. So the wedged sync state is not merely in memory; it lives in the app's local, per-account device data. Which is precisely why the fix below works and the usual advice (toggle Bluetooth, restart the phone, restart the watch) does not.

## How to Fix It
To fix this issue, **Log out of the Garmin Connect app, then log back in**. After logging in, the app will drop you into a **"searching for your device"** screen. You do not need it - your watch is already paired at the operating-system level and registered to your account. **Close the app and reopen it**, and it will come up with the device already in place.

Logging out tears down the local account session together with the cached device state and its pending transfer queue; logging back in rebuilds a clean one, and the next sync delivers everything you sent in the meantime.