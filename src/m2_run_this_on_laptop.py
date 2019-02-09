"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Displays the Graphical User Interface (GUI) and communicates with the robot.

  Authors:  Your professors (for the framework)
    and Weizhou Liu.
  Winter term, 2018-2019.
"""

import mqtt_remote_method_calls as com
import tkinter
from tkinter import ttk
import shared_gui


def main():
    """
    This code, which must run on a LAPTOP:
      1. Constructs a GUI for my part of the Capstone Project.
      2. Communicates via MQTT with the code that runs on the EV3 robot.
    """
    # -------------------------------------------------------------------------
    # Construct and connect the MQTT Client:
    # -------------------------------------------------------------------------
    mqtt_sender=com.MqttClient()
    mqtt_sender.connect_to_ev3()


    # -------------------------------------------------------------------------
    # The root TK object for the GUI:
    # -------------------------------------------------------------------------
    root=tkinter.Tk()
    root.title("Hello")


    # -------------------------------------------------------------------------
    # The main frame, upon which the other frames are placed.
    # -------------------------------------------------------------------------
    main_frame=ttk.Frame(root, padding=10, borderwidth=5, relief="groove")
    main_frame.grid()


    # -------------------------------------------------------------------------
    # Sub-frames for the shared GUI that the team developed:
    # -------------------------------------------------------------------------
    teleop_frame,arm_frame,control_frame=get_shared_frames(main_frame,mqtt_sender)


    # -------------------------------------------------------------------------
    # Frames that are particular to my individual contributions to the project.
    # -------------------------------------------------------------------------
    # TODO: Implement and call get_my_frames(...)

    # -------------------------------------------------------------------------
    # Grid the frames.
    # -------------------------------------------------------------------------
    grid_frames(teleop_frame,arm_frame,control_frame)


    # -------------------------------------------------------------------------
    # The event loop:
    # -------------------------------------------------------------------------
    root.mainloop()



def get_shared_frames(main_frame, mqtt_sender):
    teleop_frame=shared_gui.get_teleoperation_frame(main_frame,mqtt_sender)
    arm_frame=shared_gui.get_arm_frame(main_frame,mqtt_sender)
    control_frame=shared_gui.get_control_frame(main_frame,mqtt_sender)
    return teleop_frame,arm_frame,control_frame


def grid_frames(teleop_frame, arm_frame, control_frame):
    teleop_frame.grid(row=0,column=0)
    arm_frame.grid(row=1,column=0)
    control_frame.grid(row=2,column=0)


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()


def go_straight_for_seconds(self, seconds, speed):
    """
    Makes the robot go straight (forward if speed > 0, else backward)
    at the given speed for the given number of seconds.
    """
    self.go(speed, speed)
    time.sleep(seconds)
    self.stop()


def go_straight_for_inches_using_time(self, inches, speed):
    """
    Makes the robot go straight at the given speed
    for the given number of inches, using the approximate
    conversion factor of 10.0 inches per second at 100 (full) speed.
    """
    self.go(speed, speed)
    time.sleep(inches / 10)
    self.stop()


def go_straight_for_inches_using_encoder(self, inches, speed):
    """
    Makes the robot go straight (forward if speed > 0, else backward)
    at the given speed for the given number of inches,
    using the encoder (degrees traveled sensor) built into the motors.
    """
    self.right_motor.reset_position()
    self.left_motor.reset_position()
    inches_per_degree = self.left_motor.WheelCircumference / 360
    degrees_to_move = inches // inches_per_degree
    self.go(speed, speed)
    while True:
        self.left_motor.get_position()
        if abs(self.left_motor.get_position()) >= degrees_to_move:
            self.stop()
            break