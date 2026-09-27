from sensor_demo import describe_bend

a_readings = {
    "thumb": 219,
    "index": 310,
    "middle": 659,
    "ring": 660,
    "pinky": 710
}

b_readings = {
    "thumb": 229,  
    "index": 320,
    "middle": 669,
    "ring": 670,
    "pinky": 720
}

c_readings = {
    "thumb": 239,   
    "index": 330,
    "middle": 679,
    "ring": 680,
    "pinky": 730
}

for key, readings in {"A": a_readings, "B": b_readings, "C": c_readings}.items():
    print(f"For {key}, ")
    for finger, reading in readings.items():
        print(f"{finger} ({reading}) is {describe_bend(reading)}")

