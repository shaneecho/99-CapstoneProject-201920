"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Hanrui Chen.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as rec


def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    # real_things()
    # tone_test()
    beeper_test()

def real_things():
    robot = rosebot.RoseBot()
    receiver = rec.Receiver(robot)
    mqtt_receiver = com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()

    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

def tone_test():
    robot = rosebot.RoseBot()
    robot.sound_system.tones_until_touch_sensor_is_pressed()

def beeper_test():
    robot = rosebot.RoseBot()
    robot.sound_system.beep_for_given_time(10)

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()