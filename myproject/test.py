import math

def main():

    print(compute_wind_correction_angle("a",0,0,0))

def compute_wind_correction_angle(wind_speed, wind_direction, desired_course, true_airspeed):
    x = math.pi * (wind_direction - desired_course) / 180

    y = (wind_speed / true_airspeed) * math.sin(x)

    z = math.asin(y)

    wind_correction_angle = (180 / math.pi) * z
    print(wind_correction_angle)
    return wind_correction_angle


if __name__ == "__main__":
    main()
