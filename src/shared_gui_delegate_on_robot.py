"""
  Capstone Project.  Code to run on the EV3 robot (NOT on a laptop).
  This code is the delegate for handling messages from the shared GUI.

  Author:  Your professors (for the framework)
    and Hanrui Chen, Shixin Yan, and Weizhou Liu.
  Winter term, 2018-2019.
"""

class Receiver(object):
    def __init__(self,robot):
        """ :type robot: rosebot.Rosebot"""
        self.robot = robot

    def forward(self, left_wheel_speed, right_wheel_speed):
        print("Got forward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.go(int(left_wheel_speed), int(right_wheel_speed))

    def stop(self):
        print("Stop")
        self.robot.drive_system.stop()

    def backward(self, left_wheel_speed, right_wheel_speed):
        print("Backward", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.back(int(left_wheel_speed), int(right_wheel_speed))

    def left(self, left_wheel_speed, right_wheel_speed):
        print("Turn Left", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.left(int(left_wheel_speed), int(right_wheel_speed))

    def right(self, left_wheel_speed, right_wheel_speed):
        print("Turn Right", left_wheel_speed, right_wheel_speed)
        self.robot.drive_system.right(int(left_wheel_speed), int(right_wheel_speed))

#####################################################

    def raise_arm(self):
        print("Raise")
        self.robot.arm_and_claw.raise_arm()

    def lower_arm(self):
        print("Lower")
        self.robot.arm_and_claw.lower_arm()

    def calibrate_arm(self):
        print("Calibrate")
        self.robot.arm_and_claw.calibrate_arm()

    def move_arm_to_position(self, position):
        print("Move to position", position)
        self.robot.arm_and_claw.move_arm_to_position(int(position))