"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Shixin Yan.
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
    real_thing()
#     # run_test_raise_arm()
#     # run_test_calibrate_arm()
#     # run_test_move_arm_to_position()
#     # run_test_lower_arm()
#
#
# def run_test_raise_arm():
#     robot = rosebot.RoseBot()
#     robot.arm_and_claw.raise_arm()
#
# def run_test_calibrate_arm():
#     robot = rosebot.RoseBot()
#     robot.arm_and_claw.calibrate_arm()
#
# def run_test_move_arm_to_position():
#     robot = rosebot.RoseBot()
#     robot.arm_and_claw.move_arm_to_position()
#
# def run_test_lower_arm():
#     robot = rosebot.RoseBot()
#     robot.arm_and_claw.lower_arm()


def real_thing():
    robot=rosebot.RoseBot()
    receiver=rec.Receiver(robot)
    mqtt_receiver=com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()