"""
  Capstone Project.  Code to run on a LAPTOP (NOT the robot).
  Constructs and returns Frame objects for the basics:
  -- teleoperation
  -- arm movement
  -- stopping the robot program

  This code is SHARED by all team members.  It contains both:
    -- High-level, general-purpose methods for a Snatch3r EV3 robot.
    -- Lower-level code to interact with the EV3 robot library.

  Author:  Your professors (for the framework and lower-level code)
    and Hanrui Chen, Shixin Yan, and Weizhou Liu.
  Winter term, 2018-2019.
"""

import tkinter
from tkinter import ttk
import time


def get_teleoperation_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's motion
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Teleoperation")
    left_speed_label = ttk.Label(frame, text="Left wheel speed (0 to 100)")
    right_speed_label = ttk.Label(frame, text="Right wheel speed (0 to 100)")

    left_speed_entry = ttk.Entry(frame, width=8)
    left_speed_entry.insert(0, "100")
    right_speed_entry = ttk.Entry(frame, width=8, justify=tkinter.RIGHT)
    right_speed_entry.insert(0, "100")


    forward_button = ttk.Button(frame, text="Forward")
    backward_button = ttk.Button(frame, text="Backward")
    left_button = ttk.Button(frame, text="Left")
    right_button = ttk.Button(frame, text="Right")
    stop_button = ttk.Button(frame, text="Stop")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    left_speed_label.grid(row=1, column=0)
    right_speed_label.grid(row=1, column=2)
    left_speed_entry.grid(row=2, column=0)
    right_speed_entry.grid(row=2, column=2)

    forward_button.grid(row=3, column=1)
    left_button.grid(row=4, column=0)
    stop_button.grid(row=4, column=1)
    right_button.grid(row=4, column=2)
    backward_button.grid(row=5, column=1)


    # Set the button callbacks:
    forward_button["command"] = lambda: handle_forward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    backward_button["command"] = lambda: handle_backward(
        left_speed_entry, right_speed_entry, mqtt_sender)
    left_button["command"] = lambda: handle_left(
        left_speed_entry, right_speed_entry, mqtt_sender)
    right_button["command"] = lambda: handle_right(
        left_speed_entry, right_speed_entry, mqtt_sender)
    stop_button["command"] = lambda: handle_stop(mqtt_sender)
    return frame

def get_arm_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame
    has Entry and Button objects that control the EV3 robot's Arm
    by passing messages using the given MQTT Sender.
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Arm and Claw")
    position_label = ttk.Label(frame, text="Desired arm position:")
    position_entry = ttk.Entry(frame, width=8)

    raise_arm_button = ttk.Button(frame, text="Raise arm")
    lower_arm_button = ttk.Button(frame, text="Lower arm")
    calibrate_arm_button = ttk.Button(frame, text="Calibrate arm")
    move_arm_button = ttk.Button(frame,
                                 text="Move arm to position (0 to 5112)")
    blank_label = ttk.Label(frame, text="")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    position_label.grid(row=1, column=0)
    position_entry.grid(row=1, column=1)
    move_arm_button.grid(row=1, column=2)

    blank_label.grid(row=2, column=1)
    raise_arm_button.grid(row=3, column=0)
    lower_arm_button.grid(row=3, column=1)
    calibrate_arm_button.grid(row=3, column=2)

    # Set the Button callbacks:
    raise_arm_button["command"] = lambda: handle_raise_arm(mqtt_sender)
    lower_arm_button["command"] = lambda: handle_lower_arm(mqtt_sender)
    calibrate_arm_button["command"] = lambda: handle_calibrate_arm(mqtt_sender)
    move_arm_button["command"] = lambda: handle_move_arm_to_position(
        position_entry, mqtt_sender)
    return frame

def get_control_frame(window, mqtt_sender):
    """
    Constructs and returns a frame on the given window, where the frame has
    Button objects to exit this program and/or the robot's program (via MQTT).
      :type  window:       ttk.Frame | ttk.Toplevel
      :type  mqtt_sender:  com.MqttClient
    """
    # Construct the frame to return:
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    # Construct the widgets on the frame:
    frame_label = ttk.Label(frame, text="Control")
    quit_robot_button = ttk.Button(frame, text="Stop the robot's program")
    exit_button = ttk.Button(frame, text="Stop this and the robot's program")

    # Grid the widgets:
    frame_label.grid(row=0, column=1)
    quit_robot_button.grid(row=1, column=0)
    exit_button.grid(row=1, column=2)

    # Set the Button callbacks:
    quit_robot_button["command"] = lambda: handle_quit(mqtt_sender)
    exit_button["command"] = lambda: handle_exit(mqtt_sender)

    return frame

def get_drive_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Special Driving Operation")
    GSFS_button = ttk.Button(frame, text="Go straight for seconds")
    GSFIUT_button = ttk.Button(frame, text="Go straight for inches using time")
    GSFIUE_button = ttk.Button(frame, text="Go straight for inches using encoder")

    frame_label.grid(row=0, column=1)
    GSFS_button.grid(row=2, column=2)
    GSFIUT_button.grid(row=3, column=2)
    GSFIUE_button.grid(row=4, column=2)

    time_label = ttk.Label(frame, text="Time/Distance for running")
    distance_label = ttk.Label(frame, text="Speed for running")
    time_label.grid(row=1, column=0)
    distance_label.grid(row=1, column=1)

    time_entry = ttk.Entry(frame, width=8)
    distance_entry1 = ttk.Entry(frame, width=8)
    distance_entry2 = ttk.Entry(frame, width=8)
    speed_entry1 = ttk.Entry(frame, width=8)
    speed_entry2 = ttk.Entry(frame, width=8)
    speed_entry3 = ttk.Entry(frame, width=8)

    time_entry.grid(row=2, column=0)
    speed_entry1.grid(row=2, column=1)
    distance_entry1.grid(row=3, column=0)
    speed_entry2.grid(row=3, column=1)
    distance_entry2.grid(row=4, column=0)
    speed_entry3.grid(row=4, column=1)

    GSFS_button["command"] = lambda : handle_go_straight_for_second(time_entry, speed_entry1, mqtt_sender)
    GSFIUT_button["command"] = lambda: handle_go_straight_for_inches_using_time(distance_entry1, speed_entry2, mqtt_sender)
    GSFIUE_button["command"] = lambda: handle_go_straight_for_inches_using_encoder(distance_entry2, speed_entry3, mqtt_sender)
    return frame

def get_sound_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Sound System")
    BFS_button = ttk.Button(frame, text="Beep for seconds")
    TWFAD_button = ttk.Button(frame, text="Tone with specific frequency and duration")
    SFK_button = ttk.Button(frame, text="Speak specific frames")

    time_label = ttk.Label(frame, text="Time")
    frequency_label = ttk.Label(frame, text="Frequency")
    duration_label = ttk.Label(frame, text="Duration")
    sframe_label = ttk.Label(frame, text="Frame")

    time_entry = ttk.Entry(frame, width=8)
    frequency_entry = ttk.Entry(frame, width=8)
    sframe_entry = ttk.Entry(frame, width=8)
    duration_entry = ttk.Entry(frame, width=8)

    frame_label.grid(row=0, column=1)
    BFS_button.grid(row=1, column=0)
    TWFAD_button.grid(row=1, column=1)
    SFK_button.grid(row=1, column=2)

    time_label.grid(row=2, column=0)
    frequency_label.grid(row=2, column=1)
    sframe_label.grid(row=2, column=2)
    time_entry.grid(row=3, column=0)
    frequency_entry.grid(row=3, column=1)
    sframe_entry.grid(row=3, column=2)
    duration_label.grid(row=4, column=1)
    duration_entry.grid(row=4, column=1)

    BFS_button["command"] = lambda : handle_beep_for_seconds(time_entry, mqtt_sender)
    TWFAD_button["command"] = lambda: handle_tone_with_specific_frequency_and_duration(frequency_entry, duration_entry, mqtt_sender)
    SFK_button["command"] = lambda: handle_speak_specific_frames(sframe_entry, mqtt_sender)
    return frame

def get_color_frame(window, mqtt_sender):
    frame = ttk.Frame(window, padding=10, borderwidth=5, relief="ridge")
    frame.grid()

    frame_label = ttk.Label(frame, text="Color")
    intensity_color_label = ttk.Label(frame, text="Intensity/Color")
    speed_label = ttk.Label(frame, text="Speed")

    intensity_color1_entry = ttk.Entry(frame, width=8)
    intensity_color2_entry = ttk.Entry(frame, width=8)
    intensity_color3_entry = ttk.Entry(frame, width=8)
    intensity_color4_entry = ttk.Entry(frame, width=8)
    speed1_entry = ttk.Entry(frame, width=8)
    speed2_entry = ttk.Entry(frame, width=8)
    speed3_entry = ttk.Entry(frame, width=8)
    speed4_entry = ttk.Entry(frame, width=8)

    SBLI_button = ttk.Button(frame, text="stop by less intensity")
    SBMI_button = ttk.Button(frame, text="stop by more intensity")
    GUCI_button = ttk.Button(frame, text="go until color is")
    GUCIN_button = ttk.Button(frame, text="go until color is not")

    frame_label.grid(row=0, column=1)
    intensity_color_label.grid(row=1, column=0)
    speed_label.grid(row=1, column=1)
    intensity_color1_entry.grid(row=2, column=0)
    intensity_color2_entry.grid(row=3, column=0)
    intensity_color3_entry.grid(row=4, column=0)
    intensity_color4_entry.grid(row=5, column=0)
    speed1_entry.grid(row=2, column=1)
    speed2_entry.grid(row=3, column=1)
    speed3_entry.grid(row=4, column=1)
    speed4_entry.grid(row=5, column=1)
    SBLI_button.grid(row=2, column=2)
    SBMI_button.grid(row=3, column=2)
    GUCI_button.grid(row=4, column=2)
    GUCIN_button.grid(row=5, column=2)

    SBLI_button["command"]=lambda:handle_stop_by_less_intensity(intensity_color1_entry, speed1_entry, mqtt_sender)
    SBMI_button["command"]=lambda:handle_stop_by_more_intensity(intensity_color2_entry, speed2_entry, mqtt_sender)
    GUCI_button["command"]=lambda:handle_go_until_color_is(intensity_color3_entry, speed3_entry, mqtt_sender)
    GUCIN_button["command"]=lambda:handle_go_until_color_is_not(intensity_color4_entry, speed4_entry, mqtt_sender)
    return frame
###############################################################################
###############################################################################
# The following specifies, for each Button,
# what should happen when the Button is pressed.
###############################################################################
###############################################################################

###############################################################################
# Handlers for Buttons in the Teleoperation frame.
###############################################################################
def handle_forward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    with the speeds used as given.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print("Forward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("forward", [left_entry_box.get(), right_entry_box.get()])



def handle_backward(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negatives of the speeds in the entry boxes.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """

    print("Backward", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("backward", [left_entry_box.get(), right_entry_box.get()])

def handle_left(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the left entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Turn left", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("left", [left_entry_box.get(), right_entry_box.get()])

def handle_right(left_entry_box, right_entry_box, mqtt_sender):
    """
    Tells the robot to move using the speeds in the given entry boxes,
    but using the negative of the speed in the right entry box.
      :type  left_entry_box:   ttk.Entry
      :type  right_entry_box:  ttk.Entry
      :type  mqtt_sender:      com.MqttClient
    """
    print("Turn right", left_entry_box.get(), right_entry_box.get())
    mqtt_sender.send_message("right", [left_entry_box.get(), right_entry_box.get()])


def handle_stop(mqtt_sender):
    """
    Tells the robot to stop.
      :type  mqtt_sender:  com.MqttClient
    """

    print("stop")
    mqtt_sender.send_message("stop")

def handle_go_straight_for_second(time_entry_box,speed_entry_box,mqtt_sender):
    """
    Tell the robot to go straight for specific seconds using given speed
    :param mqtt_sender:
    :return:
    """
    print("Go straight for seconds", time_entry_box.get(),speed_entry_box.get())
    mqtt_sender.send_message("GSFS", [time_entry_box.get(), speed_entry_box.get()])

def handle_go_straight_for_inches_using_time(distance_entry_box, speed_entry_box, mqtt_sender):
    """
    Tell the robot to go straight for specific distance using given speed
    :param distance_entry_box:
    :param speed_entry_box:
    :param mqtt_sender:
    :return:
    """
    print("Go straight for inches using time", distance_entry_box.get(), speed_entry_box.get())
    mqtt_sender.send_message("GSFIUT", [distance_entry_box.get(), speed_entry_box.get()])

def handle_go_straight_for_inches_using_encoder(distance_entry_box, speed_entry_box, mqtt_sender):
    """
    Tell the robot to go straight for specific distance using given speed, but using sensor
    :param distance_entry_box:
    :param speed_entry_box:
    :param mqtt_sender:
    :return:
    """
    print("Go straight for inches using endoer", distance_entry_box.get(), speed_entry_box.get())
    mqtt_sender.send_message("GSFIUE", [distance_entry_box.get(), speed_entry_box.get()])

###############################################################################
# Handlers for Buttons in the ArmAndClaw frame.
###############################################################################
def handle_raise_arm(mqtt_sender):
    """
    Tells the robot to raise its Arm until its touch sensor is pressed.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Raise")
    mqtt_sender.send_message("raise_arm")

def handle_lower_arm(mqtt_sender):
    """
    Tells the robot to lower its Arm until it is all the way down.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Lower")
    mqtt_sender.send_message("lower_arm")


def handle_calibrate_arm(mqtt_sender):
    """
    Tells the robot to calibrate its Arm, that is, first to raise its Arm
    until its touch sensor is pressed, then to lower its Arm until it is
    all the way down, and then to mark taht position as position 0.
      :type  mqtt_sender:  com.MqttClient
    """
    print("Calibrate")
    mqtt_sender.send_message("calibrate_arm")

def handle_move_arm_to_position(arm_position_entry, mqtt_sender):
    """
    Tells the robot to move its Arm to the position in the given Entry box.
    The robot must have previously calibrated its Arm.
      :type  arm_position_entry  ttk.Entry
      :type  mqtt_sender:        com.MqttClient
    """
    print("Move to", arm_position_entry.get())
    mqtt_sender.send_message("move_arm_to_position", [arm_position_entry.get()])

###############################################################################
# Handlers for Buttons in the Control frame.
###############################################################################
def handle_quit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
      :type  mqtt_sender:  com.MqttClient
    """
    print('quit')
    mqtt_sender.send_message('quit')

def handle_exit(mqtt_sender):
    """
    Tell the robot's program to stop its loop (and hence quit).
    Then exit this program.
      :type mqtt_sender: com.MqttClient
    """
    print('exit')
    handle_quit(mqtt_sender)
    exit()

###############################################################################
# Handlers for Buttons in the Sound frame.
###############################################################################
def handle_beep_for_seconds(time_entry, mqtt_sender):
    print("Beep for seconds", time_entry.get())
    mqtt_sender.send_message('beep', [time_entry.get()])

def handle_tone_with_specific_frequency_and_duration(frequency_entry, duration_entry, mqtt_sender):
    print("Tone with specific frequency and duration", frequency_entry.get(), duration_entry.get())
    mqtt_sender.send_message('tone', [frequency_entry.get(), duration_entry.get()])

def handle_speak_specific_frames(sframe_entry, mqtt_sender):
    print("Speak specific frames", sframe_entry.get())
    mqtt_sender.send_message('speaker', [sframe_entry.get()])

###############################################################################
# Handlers for Buttons in the Color frame.
###############################################################################
def handle_stop_by_less_intensity(intensity_entry, speed_entry, mqtt_sender):
    print("Stop by less intensity", intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message('stop_by_less_intensity', [intensity_entry.get(), speed_entry.get()])

def handle_stop_by_more_intensity(intensity_entry, speed_entry, mqtt_sender):
    print("Stop by more intensity", intensity_entry.get(), speed_entry.get())
    mqtt_sender.send_message("stop_by_more_intensity", [intensity_entry.get(), speed_entry.get()])

def handle_go_until_color_is(color_entry, speed_entry, mqtt_sender):
    print("Go until color is", color_entry.get(), speed_entry.get())
    mqtt_sender.send_message("go_until_color_is", [color_entry.get(), speed_entry.get()])

def handle_go_until_color_is_not(color_entry, speed_entry, mqtt_sender):
    print("Go until color is not", color_entry.get(), speed_entry.get())
    mqtt_sender.send_message("go_until_color_is_not", [color_entry.get(), speed_entry.get()])
