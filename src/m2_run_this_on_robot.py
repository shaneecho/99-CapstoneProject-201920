"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  Author:  Your professors (for the framework)
    and Weizhou Liu.
  Winter term, 2018-2019.
"""

import rosebot
import mqtt_remote_method_calls as com
import time
import shared_gui_delegate_on_robot as sgd

def main():
    """
    This code, which must run on the EV3 ROBOT:
      1. Makes the EV3 robot to various things.
      2. Communicates via MQTT with the GUI code that runs on the LAPTOP.
    """
    #real_thing()
    #run_test_go_stright_for_seconds()
    #run_test_go_stright_for_inches_using_time()
    #run_test_go_stright_for_inches_using_encoder()
    run_test_1()


def real_thing():
    robot=rosebot.RoseBot()
    receiver=sgd.Receiver(robot)
    mqtt_receiver=com.MqttClient(receiver)
    mqtt_receiver.connect_to_pc()
    while True:
        time.sleep(0.01)
        if receiver.is_time_to_stop:
            break

def run_test_go_stright_for_seconds():
    robot=rosebot.RoseBot()
    robot.drive_system.go_straight_for_seconds(3,50)

def run_test_go_stright_for_inches_using_time():
    robot=rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_time(3,50)

def run_test_go_stright_for_inches_using_encoder():
    robot=rosebot.RoseBot()
    robot.drive_system.go_straight_for_inches_using_encoder(40,50)

def run_test_1():
    robot=rosebot.RoseBot()
    robot.drive_system.go_straight_until_intensity_is_less_than(10,50)
# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()