import math
from tkinter import *

def main():

    def get_input():

        try:
            desired_course = float(course_entry.get())
            true_speed = float(true_airspeed_entry.get())
            wind_direction = float(wind_direction_entry.get())
            wind_speed = float(wind_speed_entry.get())

            correction_angle = compute_wind_correction_angle(wind_speed,wind_direction,desired_course,true_speed)
            true_ground_speed = compute_true_ground_speed(wind_speed, wind_direction, desired_course, true_speed, correction_angle)

            wind_correction_label.config(text=f"Wind correction angle: {round(correction_angle)}")
            true_ground_speed_label.config(text=f"True ground speed: {round(true_ground_speed)}")

            posx = 150
            posy = 125
            angle = desired_course + correction_angle

            canvas.create_line(posx, posy, math.cos(angle), math.sin(angle), fill="white", width=5)    


        except ValueError:
            wind_correction_label.config(text="Value Error.")
            true_ground_speed_label.config(text=f"Value Error.")

        except ZeroDivisionError:
            wind_correction_label.config(text="Division by Zero.")
            true_ground_speed_label.config(text=f"Division by Zero.")


    window = Tk()
    window.title("E6B Virtual Flight Computer")
    window.geometry("1200x700")
    window.config(bg="lightblue")
    window.maxsize(1200,700)

    title = Label(window, text="E6B Virtual Flight Computer", bg="black", fg="white", \
        font=("Helvetica", 25, "bold"))
    title.pack(anchor=N, pady=(20,10))

    frame_right = Frame(window)
    frame_right.pack(side=RIGHT, padx=(0,250))

    frame_left = Frame(window)
    frame_left.pack(side=LEFT, padx=(250,0))

    #-----------------------------------left elements------------------------------------

    course_label = Label(frame_left, text="Enter course below:")
    course_label.pack(pady=5)

    course_entry = Entry(frame_left)
    course_entry.pack(pady=5)
   
    true_airspeed_label = Label(frame_left, text="Enter true airspeed below:")
    true_airspeed_label.pack(pady=5)

    true_airspeed_entry = Entry(frame_left)
    true_airspeed_entry.pack(pady=5)

    wind_direction_label = Label(frame_left, text="Enter wind direction below:")
    wind_direction_label.pack(pady=5)

    wind_direction_entry = Entry(frame_left)
    wind_direction_entry.pack(pady=5)

    wind_speed_label = Label(frame_left, text="Enter wind speed below:")
    wind_speed_label.pack(pady=5)

    wind_speed_entry = Entry(frame_left)
    wind_speed_entry.pack(pady=5)

    #-----------------------------------right elements------------------------------------


    canvas = Canvas(frame_right, width=300, height=250)
    canvas.pack()

    x1=50
    y1=25
    x2=250
    y2=225

    oval = canvas.create_oval(x1, y1, x2, y2, fill="blue")
                
    wind_correction_label = Label(frame_right, width=30, text="", borderwidth=5, relief="groove")
    wind_correction_label.pack(pady=(0,5))

    true_ground_speed_label = Label(frame_right, width=30, text="", borderwidth=5, relief="groove")
    true_ground_speed_label.pack(pady=(0,15))

    button = Button(frame_left, 
        text="CALCULATE", 
        command=get_input)

    button.pack(pady=5)

    window.mainloop()

def compute_wind_correction_angle(wind_speed, wind_direction, desired_course, true_airspeed):
    x = math.pi * (wind_direction - desired_course) / 180

    wind_correction_angle = 180 / math.pi * math.asin(wind_speed / true_airspeed * math.sin(x))

    return wind_correction_angle

def compute_true_ground_speed(wind_speed, wind_direction, desired_course, true_airspeed, wind_correction_angle):
    x = math.pi * (desired_course - wind_direction + wind_correction_angle) /180

    ground_speed = math.pow(true_airspeed * true_airspeed + wind_speed * wind_speed - 
        2 * true_airspeed * wind_speed * math.cos(x), 1/2)

    return ground_speed



if __name__ == "__main__":
    main()
