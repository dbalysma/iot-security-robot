# IoT Home-Security Robot

A mobile home-security robot built on a Raspberry Pi 3 B+ for my BEng Electromechanical Engineering final-year
project at Coventry University (2022–23, dissertation: *IoT-Based Home Security Systems*).

The robot attempts autonomous obstacle avoidance, driving forward and turning away when its ultrasonic sensor
detects something close. It was designed to take a photo when its PIR sensor detects movement and email it to
the owner.

> **Status:** university prototype from 2023. The code in [`original-2023/`](original-2023/) is the code as it
> was in June 2023, recovered from emails I sent at the time. Only an email app password and the email
> addresses were removed before publishing. See [PROVENANCE.md](PROVENANCE.md).

## Project timeline

Dates come from emails I sent at the time, which carry the files and videos listed.

| Date | What happened | Evidence |
|---|---|---|
| 2022–23 | BEng Electromechanical Engineering final year at Coventry University. Dissertation: *IoT-Based Home Security Systems* | Dissertation |
| 1 Jun 2023 | Ultrasonic distance sensing started: a reference example saved for study (not my code, so not included) | Email |
| 5 Jun 2023 | Motor test filmed: two videos, emailed as "Robot motors" | Email with the videos |
| 9 Jun 2023 | First drafts of the motor, PIR, camera and ultrasonic scripts | Emails |
| 13 Jun 2023 | PIR motion sensor and camera combined in one script (`Human Detector 3.py`) | Email |
| 15 Jun 2023 | Final set of eight scripts, adding obstacle-avoidance navigation and email alerts | Email |
| 23 Jun 2023 | Dissertation final write-up done: the file `Dissertation Final WriteUp.docx` existed by this date | Email with the file attached |
| 2023 | BEng awarded (2:1) | Degree result |
| Nov 2026 | Code recovered from those emails and documented here (see [PROVENANCE.md](PROVENANCE.md)) | This repository |

## What it does

| Function | Hardware | Script |
|---|---|---|
| Motion detection | PIR motion sensor | [`PIR Sensor.py`](original-2023/PIR%20Sensor.py) |
| Photo on motion | PIR sensor and Raspberry Pi camera module | [`MotionSensorCamera.py`](original-2023/MotionSensorCamera.py) |
| Email alert with the photo | Gmail SMTP over TLS | [`EmailCommunication.py`](original-2023/EmailCommunication.py) |
| Obstacle avoidance (attempted) | HC-SR04 ultrasonic sensor, motor driver, two drive motors | [`ObstacleAvoidanceNavigation.py`](original-2023/ObstacleAvoidanceNavigation.py) |
| Distance test | HC-SR04 ultrasonic sensor | [`Ultrasonic Sensor.py`](original-2023/Ultrasonic%20Sensor.py) |
| Drive test | Motor driver and motors | [`Motors.py`](original-2023/Motors.py) |
| Camera tests | Camera module, OpenCV | [`Camera Module.py`](original-2023/Camera%20Module.py), [`Test.py`](original-2023/Test.py) |

Each subsystem is a separate script. [original-2023/README.md](original-2023/README.md) describes every file.

**What the recovered code does and doesn't show:** `MotionSensorCamera.py` takes a photo when the PIR sensor
fires. `EmailCommunication.py` takes a photo and emails it whenever it is run, with no PIR input. None of the
recovered scripts joins the two, so the full motion-to-email alert can't be reproduced from this code. The
dissertation reports that alert working (see Results), but the code that connected the steps wasn't among the
files recovered.

## Wiring

Taken from the pin numbers in the code (15 June 2023 versions). This is the software pin assignment, not a
verified wiring diagram or a build guide.

| Signal | GPIO (BCM) | Physical pin |
|---|---|---|
| PIR output | 5 | 29 |
| Ultrasonic TRIG | 19 | 35 |
| Ultrasonic ECHO | 26 | 37 |
| Motor driver A-1A | 18 | 12 |
| Motor driver A-1B | 17 | 11 |
| Motor driver B-1A | 12 | 32 |
| Motor driver B-1B | 6 | 31 |

The PIR sensor was on physical pin 37 in the 13 June version (`Human Detector 3.py`). By 15 June it had moved to
pin 29, and pin 37 had become the ultrasonic echo input.

> **Electrical safety:** a standard HC-SR04 runs on 5 V and its ECHO pin outputs 5 V, but Raspberry Pi GPIO
> inputs take 3.3 V at most. ECHO needs a voltage divider or level shifter before it reaches the Pi. Whether the
> 2023 build used one isn't recorded in the recovered code and hasn't been verified, so don't copy this table
> as a wiring guide.

## How the obstacle avoidance was designed to work

1. Drive forward.
2. Send a 10 µs trigger pulse to the HC-SR04 and time the echo.
3. Distance (cm) = echo time × 17,150, which is half the speed of sound (34,300 cm/s) because the pulse travels
   there and back.
4. If an obstacle is closer than 60 cm: stop, rotate, then pivot left or right, alternating with a counter.
   Otherwise keep driving.

In testing this wasn't reliable: see the turning bugs in the code review below and the furniture stall in the
results.

The motors are driven through an H-bridge driver, so each move (forward, pivot, rotate, stop) is one combination
of the four driver inputs.

## Results and limitations

Reported in the dissertation (the recovered code alone doesn't reproduce the first point; see *What it does*):

- Motion-triggered photos were captured and sent as email alerts, with screenshots of the notifications recorded.
- Sensor tests and the Pi's hardware and software resource use were measured and documented.
- In one short test in a home, the robot stalled against furniture while navigating.
- Running all the functions together strained the Pi's processor and memory.

## Notes from a 2026 review of the code

Found while preparing this showcase. The code is published as it was, not fixed.

- In `Motors.py`, `ChangeDirectionLeft` and `ChangeDirectionRight` set the same pin states, so both turn the
  same way. The same applies to `RotateClockwise` and `RotateAntiClockwise` in `ObstacleAvoidanceNavigation.py`.
- In `ObstacleAvoidanceNavigation.py`, the movement functions take a duration argument but don't use it.
- The echo-timing loops have no timeout, so a missed echo would stall the program.
- The email script held the app password in the source file. It has been removed here.

## Provenance

See [PROVENANCE.md](PROVENANCE.md) for where each file came from and what was changed.

---
BEng Electromechanical Engineering, Coventry University (2022–23)
