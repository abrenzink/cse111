from pyparsing import null_debug_action
from e6b_flight_computer import compute_wind_correction_angle, compute_true_ground_speed
import pytest
from pytest import approx


def test_compute_wind_correction_angle():

    #wind_speed, wind_direction, desired_course, true_airspeed

    x = compute_wind_correction_angle(250,90,250,100)
    assert isinstance(x, int) or isinstance(x, float)

    assert compute_wind_correction_angle(250,90,250,100) == approx(-59, 1)
    assert compute_wind_correction_angle(50,90,320,100) == approx(23, 1)
    assert compute_wind_correction_angle(0,0,0,100) == 0
    assert compute_wind_correction_angle(110,48,3.6,220) == approx(20, 1)

    #true airspeed should not be 0
    with pytest.raises(ZeroDivisionError):
        compute_wind_correction_angle(120,0,120,0)

    with pytest.raises(NameError):
        compute_wind_correction_angle(a,0,120,100)
        compute_wind_correction_angle(250,a,120,100)
        compute_wind_correction_angle(250,0,a,100)
        compute_wind_correction_angle(250,0,120,a)

    with pytest.raises(TypeError):
        compute_wind_correction_angle("a",0,120,100)
        compute_wind_correction_angle(250,"a",120,100)
        compute_wind_correction_angle(250,0,"a",100)
        compute_wind_correction_angle(250,0,120,"a")

def test_compute_true_ground_speed():

    #wind_speed, wind_direction, desired_course, true_airspeed, wind_correction_angle

    x = compute_true_ground_speed(250,90,100,380,-7)
    assert isinstance(x, int) or isinstance(x, float)

    assert compute_true_ground_speed(250,90,100,380,-7) == approx(131, 1)
    assert compute_true_ground_speed(250,-50,100,380,-7) == approx(575, 1)
    assert compute_true_ground_speed(0,0,0,100,0) == approx(100, 1)

    with pytest.raises(NameError):
        compute_true_ground_speed(a,0,120,100,200)
        compute_true_ground_speed(10,b,120,100,200)
        compute_true_ground_speed(120,0,c,100,200)
        compute_true_ground_speed(250,0,120,d,200)
        compute_true_ground_speed(250,0,120,100,e)

    with pytest.raises(TypeError):
        compute_true_ground_speed("a",0,120,100,200)
        compute_true_ground_speed(10,"b",120,100,200)
        compute_true_ground_speed(120,0,"c",100,200)
        compute_true_ground_speed(250,0,120,"d",200)
        compute_true_ground_speed(250,0,120,100,"e")



# Call the main function that is part of pytest so that the
# computer will execute the test functions in this file.
pytest.main(["-v", "--tb=line", "-rN", __file__])
