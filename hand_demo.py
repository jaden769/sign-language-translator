from sensor_demo import describe_bend

finger_readings = {
    "thumb": 299,
    "index": 300,
    "middle": 649,
    "ring": 650,
    "pinky": 700
}

for finger, reading in finger_readings.items():
    print(f"{finger} ({reading}) is {describe_bend(reading)}")

