readings = [299, 300, 649, 650]

def describe_bend(reading):
    if reading < 300:
         return "straight"
    elif reading < 650:
         return "curved"
    else:
         return "bent"

if __name__ == "__main__":
    for reading in readings:
        print(reading, describe_bend(reading))