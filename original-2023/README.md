# Original 2023 code

These files are the code from June 2023, as recovered from emails I sent while building the robot.
File names are unchanged. Nothing was edited except the redactions noted in `EmailCommunication.py`.

| File | Date | What it does |
|---|---|---|
| `MotionSensorCamera.py` | 15 Jun 2023 | Polls the PIR sensor. On motion, takes a photo and saves it with the time as the file name |
| `EmailCommunication.py` | 15 Jun 2023 | Takes a photo and emails it with a short message through Gmail SMTP over TLS. App password and addresses redacted |
| `ObstacleAvoidanceNavigation.py` | 15 Jun 2023 | Drives forward, measures distance with the HC-SR04, and stops, rotates and pivots when an obstacle is closer than 60 cm |
| `Motors.py` | 15 Jun 2023 | Motor driver functions (forward, stop, pivot, change direction) and a short drive sequence |
| `Ultrasonic Sensor.py` | 15 Jun 2023 | Continuous HC-SR04 distance readings |
| `PIR Sensor.py` | 15 Jun 2023 | Prints whether the PIR sensor sees motion |
| `Camera Module.py` | 15 Jun 2023 | Takes one photo and saves it with the time as the file name |
| `Test.py` | 15 Jun 2023 | Captures a frame into an array and shows it with OpenCV |
| `Human Detector 3.py` | 13 Jun 2023 | Earlier combined PIR and camera script (PIR on physical pin 37) |

Earlier drafts from 9 June 2023 (`Motors.py`, `PIR Sensor.py`, `Camera Module.py`, `Ultrasonic Sensor.py`) were
also recovered. They aren't included because the 15 June versions replace them.

The code targets Python 3 on Raspberry Pi OS with the `RPi.GPIO` and `picamera` libraries (`Test.py` also uses
OpenCV). It needs the robot's hardware to run.
